/**
 * Headless render entry point.
 *
 * `render.mjs` starts a Vite dev server, opens this page in headless Chromium,
 * and calls `window.__mc.render()`. This deliberately does NOT load the
 * `@motion-canvas/ui` editor: the editor's render button is a preact component
 * whose DOM is not a stable automation surface, whereas `Renderer` is the class
 * the button itself drives.
 *
 * Frames leave the browser over Vite's HMR socket (`motion-canvas:export`) and
 * are written to disk by the vite-plugin's exporter partial. That is why the
 * render runs against the DEV server and not a production build — the image
 * exporter is gated on `import.meta.hot`.
 */
import type {LogPayload} from '@motion-canvas/core';
import {Renderer, RendererResult, Vector2} from '@motion-canvas/core';
import project from './project?project';
import {type PipelineTiming, setRenderFps, timing, totalDuration} from './timing';

export interface RenderRequest {
  fps: number;
  width: number;
  height: number;
  resolutionScale?: number;
  /** Directory name under the vite plugin's `output` dir. Defaults to the project name. */
  name?: string;
}

export interface RenderReport {
  result: 'success' | 'error' | 'aborted';
  frames: number;
  fps: number;
  expectedSeconds: number;
  measured: boolean;
  logs: {level: string; message: string}[];
}

declare global {
  interface Window {
    __mc: {
      ready: boolean;
      /** Re-quantize the scene table for `fps` and return the resulting plan. */
      plan(fps: number): PipelineTiming;
      render(request: RenderRequest): Promise<RenderReport>;
    };
  }
}

const logs: {level: string; message: string}[] = [];
project.logger.onLogged.subscribe((payload: LogPayload) => {
  logs.push({level: payload.level ?? 'info', message: payload.message ?? ''});
  if (payload.level === 'error') {
    // Mirror to the console so render.mjs sees it even if the promise resolves.
    // eslint-disable-next-line no-console
    console.error(`[motion-canvas] ${payload.message}`, payload.stack ?? '');
  }
});

const renderer = new Renderer(project);

window.__mc = {
  // Flipped only once the font set has settled — see the `document.fonts.ready`
  // gate at the bottom of this file.
  ready: false,
  plan(fps: number): PipelineTiming {
    return setRenderFps(fps);
  },
  async render(request: RenderRequest): Promise<RenderReport> {
    // Scene boundaries are quantized to the fps we are about to render at.
    setRenderFps(request.fps);
    let frames = 0;
    renderer.onFrameChanged.subscribe(frame => {
      frames = frame;
    });

    const done = new Promise<RendererResult>(resolve => {
      const unsubscribe = renderer.onFinished.subscribe(result => {
        unsubscribe();
        resolve(result);
      });
    });

    void renderer.render({
      name: request.name ?? project.name,
      // `to` is clamped to the project duration by Renderer.run, so a large
      // upper bound simply means "render everything".
      range: [0, Number.MAX_SAFE_INTEGER],
      fps: request.fps,
      size: new Vector2(request.width, request.height),
      resolutionScale: request.resolutionScale ?? 1,
      colorSpace: 'srgb',
      background: null,
      exporter: {
        name: '@motion-canvas/core/image-sequence',
        options: {
          fileType: 'image/png',
          quality: 100,
          groupByScene: false,
        },
      },
    });

    const result = await done;
    return {
      result:
        result === RendererResult.Success
          ? 'success'
          : result === RendererResult.Aborted
            ? 'aborted'
            : 'error',
      frames: frames + 1,
      fps: request.fps,
      expectedSeconds: totalDuration(),
      measured: timing().measured,
      logs,
    };
  },
};

/**
 * Font-readiness gate.
 *
 * `brand.tsx` currently resolves to a system stack, so on this machine the fonts
 * are ready immediately. The gate is here for the moment a deck bundles a brand
 * webfont — which is the fix the assay-decks field report landed deck-side: if
 * the render starts before the faces are loaded, the opening frames rasterize in
 * whatever fallback family the machine happens to have. That is off-brand, and
 * worse, it is the one part of this pipeline that is genuinely non-deterministic
 * — the frames you get depend on how fast the font decoded. Waiting costs
 * nothing (render.mjs already caps readiness at 60s and fails closed).
 */
document.fonts.ready.then(() => {
  window.__mc.ready = true;
  // eslint-disable-next-line no-console
  console.log(`[motion-canvas] render entry ready (fonts settled: ${document.fonts.status})`);
});
