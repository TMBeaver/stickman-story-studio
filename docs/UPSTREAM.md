# Upstream provenance and scope

Source: https://github.com/kaomei/stickman-video-director

Pinned commit: `d19705dea434626d4fc6e651e24cdf23c7eba156`

The `vendor/directing-stickman-videos` directory preserves the upstream `skills/directing-stickman-videos` snapshot, excluding installed `node_modules`. It includes the original SKILL.md, style references, runtime scripts/tests, example manifest/audio, baseline assets and licensed fonts. The root LICENSE preserves the upstream MIT copyright notice. Original font and icon licenses remain next to their assets.

## Styles

| Mode | Styles | Production route |
| --- | --- | --- |
| A / Director | Classic Black & White, Modern Pop, Prehistoric Cave, Cozy Storytelling, Historical Cartoon | Storyboards and detailed prompts for an external video generator |
| A6 / Director | Amber Noir | Reference-guided animated clips, independent narration and finishing |
| B / Autopilot | Minimal Hand-Drawn, Colorful Hand-Drawn | Authored illustrations/layers, voice, local micro-animation and MP4 rendering |

Read the selected reference rather than transplanting one mode's constraints into another. The approved production direction in this repository is **A4 Cozy Storytelling through Google Flow / Omni**, not the simpler local Autopilot demonstration.

Upstream Cozy evidence: [style-4 report](https://github.com/kaomei/stickman-video-director/blob/d19705dea434626d4fc6e651e24cdf23c7eba156/tests/reports/style-4.md). The report identifies independent approximately ten-second Omni 1.1 Flash clips at 720p and records limitations in prop handling and transitions. It does not certify every prompt's model output or a universal narrator match.

## Local runtime check

The original runtime's dependency check passed for Node, FFmpeg, FFprobe, Canvas and fonts on the test machine. Of 21 upstream runtime tests, 19 passed and two failed before their assertions because Windows denied creation of test symbolic links (EPERM). This is not a claim that all platform tests passed.

The local renderer successfully made a ten-second procedural animation with narration, captions and SFX, but its drawing and Microsoft David voice were not accepted as the final quality target. The later Flow sample is the accepted reference.

## Running the preserved renderer

```powershell
Set-Location vendor/directing-stickman-videos
npm ci
node scripts/autopilot.mjs doctor
npm test
```

For B-style rendering, read `references/autopilot.md` and `references/autopilot-runtime.md` first. Narration and timed captions are required. Preview scope and genuine sample approval govern full rendering. Do not record an approval merely because a technical check passed.

This repository is an attributed derivative production workspace, not a claim of authorship of the upstream skill or a new hosted video-generation service. Upstream showcase footage outside the vendored skill was not copied into the public project.
