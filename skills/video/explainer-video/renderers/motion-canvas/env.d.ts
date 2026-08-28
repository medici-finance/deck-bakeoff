/// <reference types="vite/client" />
/// <reference path="./node_modules/@motion-canvas/core/project.d.ts" />

/**
 * Injected by vite.config.ts `define`. `null` when no scene-durations file was
 * resolved (standalone dev), otherwise the parsed contents of that file.
 * `src/timing.ts` is the only module that should read it.
 */
declare const __PIPELINE_TIMING__: unknown;

/**
 * `import project from './project?project'` — the vite-plugin rewrites this
 * specifier into a bootstrapped project. `@motion-canvas/core/project.d.ts`
 * declares `*?scene` but not `*?project`, so declare it here.
 */
declare module '*?project' {
  const value: import('@motion-canvas/core').Project;
  export default value;
}
