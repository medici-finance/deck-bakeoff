#!/usr/bin/env python3
"""Generate the 8 scene narration clips with Qwen3-TTS-12Hz-1.7B-Base,
voice-cloned from the Aussie reference (audio/aussie_voice.wav +
audio/aussie_voice.txt). CRITICAL: --max_tokens 4096 (default 1200 ~14.6s
silently truncates the long scenes 2,4,5,7)."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AUDIO = ROOT / "audio"
MODEL = "mlx-community/Qwen3-TTS-12Hz-1.7B-Base-bf16"
REF_AUDIO = AUDIO / "aussie_voice.wav"
REF_TEXT = (AUDIO / "aussie_voice.txt").read_text().strip()

# Narration verbatim from SCRIPT.md "Narration (voice-over)" column. The Aussie
# voice clone pronounces "Medici" correctly, so scenes 1/3/8 use the real spelling
# (reverted 2026-07-21 from a phonetic "Meddy-chee" workaround that's no longer needed).
SCENES = [
    ("scene1_title", "Every DeFi lending platform shares one hidden flaw — liquidation. Medici removes it, by design."),
    ("scene2_problem", "Traditional synthetic assets and stablecoins run on debt. You over-collateralize, and when the price moves against you, keepers liquidate your position — often at the worst possible moment. Liquidations cascade, triggering more liquidations. It takes real-time oracles and an emergency de-leveraging queue just to stay standing."),
    ("scene3_split", "Medici replaces debt with options. Take one unit of collateral and split it into two tokens: P, the protected side, and N, the amplified side. P plus N always equals one. Always."),
    ("scene4_pn", "P is a bond minus a put — its holder is the option seller, so time decay works in their favor: stable, index-tracking exposure. N is a call option — its holder buys leverage on the upside. No funding rate, no liquidation price, no de-leveraging queue. Your maximum loss is simply your notional — nothing more."),
    ("scene5_settle", "At maturity, both tokens settle against a single oracle price. Above the strike, P holds the full collateral and N is spent; below it, they share. But the key property never changes: P plus N always sums to the collateral. No shortfall, no liquidation, and no real-time oracle required."),
    ("scene6_recombine", "Change your mind? Recombine P and N any time before maturity and reclaim your original collateral. And a deposit is self-collateralized — no counterparty or pool has to back your position."),
    ("scene7_versus", "So next to a traditional lending platform: no forced liquidation, no margin calls, no keepers, no funding rates, no cascading failures — and near-zero holding cost where the strategy sits, around a tenth of a basis point a year. Just clean, option-based, index-tracking exposure."),
    ("scene8_close", "Medici. Index tracking, built on options instead of debt."),
]


def main():
    only = sys.argv[1:] if len(sys.argv) > 1 else None
    for prefix, text in SCENES:
        if only and prefix not in only:
            continue
        print(f"=== {prefix} ===", file=sys.stderr)
        cmd = [
            sys.executable, "-m", "mlx_audio.tts.generate",
            "--model", MODEL,
            "--ref_audio", str(REF_AUDIO),
            "--ref_text", REF_TEXT,
            "--text", text,
            "--max_tokens", "4096",
            "--file_prefix", prefix,
            "--output_path", str(AUDIO),
        ]
        subprocess.run(cmd, check=True, cwd=ROOT)
        src = AUDIO / f"{prefix}_000.wav"
        dst = AUDIO / f"{prefix}.wav"
        if not src.exists():
            raise SystemExit(f"expected output missing: {src}")
        src.replace(dst)
        print(f"-> {dst}", file=sys.stderr)


if __name__ == "__main__":
    main()
