# Stickman Story Studio

Create expressive, narrated stickman stories with Google Flow, from a ten-second idea to a multi-scene film. This repository preserves a tested Cozy Storytelling workflow, production prompts, an approved example, credit budgeting, and the original Stickman Video Director skill and local renderer.

## Approved visual direction

![Frames from the approved Cozy Storytelling test](examples/cozy-cafe/contact-sheet.jpg)

[Watch the ten-second example with sound](examples/cozy-cafe/video.mp4).

The first accepted test used **Google Flow / Omni 1.1 Flash / 720p / 16:9 / 10 seconds**, including generated English narration and sound. Flow quoted **15 credits**, covered by the account's free allocation. The user accepted the result as the desired direction. This is one successful sample, not a guarantee of identical quality from every generation.

The target is a full-color illustrated environment, an expressive white stickman, purposeful hand and prop interaction, motivated shot changes, and a natural offscreen storyteller. It is more than a sequence of still pictures.

## Start here

1. Read [the production workflow](docs/WORKFLOW.md).
2. Read [the approved sample prompt](prompts/cozy-cafe-approved.txt) and [sample evidence](examples/cozy-cafe/manifest.json).
3. For a longer film, follow [long-form production](docs/LONG_FORM.md) and fill in [the scene manifest template](examples/scene-manifest.template.json).
4. Estimate the budget using [credits and subscriptions](docs/CREDITS.md).
5. Use the [vendored upstream skill](vendor/directing-stickman-videos/SKILL.md) for additional visual styles and production contracts.

Example request to an assistant with browser and file access:

> Use this repository to create a 60-second Cozy Storytelling video in English, landscape 16:9. Match the approved cafe example's visual quality and natural narration. Start with a script, cast and shot plan, then a representative ten-second sample. Quote the credit budget before generation. Preserve approved assets and assemble the final MP4 with subtitles and sound.

## What is included

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Repository-specific production instructions for future sessions |
| `docs/WORKFLOW.md` | Browser preparation, generation, download and quality checks |
| `docs/LONG_FORM.md` | Continuity, narration and assembly for longer videos |
| `docs/CREDITS.md` | Dated Google credit rules and planning estimates |
| `docs/UPSTREAM.md` | Provenance, styles, preserved files and limitations |
| `prompts/cozy-cafe-approved.txt` | Actual generation prompt recorded by Flow |
| `examples/cozy-cafe/` | Accepted generated MP4, contact sheet and technical evidence |
| `vendor/directing-stickman-videos/` | Pinned upstream skill, references, scripts, runtime tests, fonts and assets |

## Requirements

- An eligible Google account signed into [Google Flow](https://flow.google.com/), with sufficient available credits. A paid plan was not required for the included test.
- A supported browser. Chrome with a connected browser-control extension worked in the test; Opera could not be controlled reliably in that session. Browser control availability depends on the host assistant.
- FFmpeg and FFprobe for local inspection and assembly.
- Node.js 20+ and `npm ci` inside `vendor/directing-stickman-videos` only when using the bundled Autopilot renderer.
- Separate provider setup if choosing an external narration service. Google AI Pro does not automatically configure a Gemini API key or API billing.

The **Director / Flow** route generates full animated clips and fits the approved Cozy style. The **Autopilot** runtime composes authored illustrations, local layer motion, voice, captions and SFX; it does not infer lifelike limb animation from a still image. These routes have different inputs and quality characteristics.

## Scope and cost

Repository code and upstream instructions are MIT-licensed. Hosted generation uses the provider's quotas, subscriptions or paid credits. A subscription improves access and credit allowance; it does not guarantee good anatomy, prop continuity or narrator consistency. See the dated [budget guide](docs/CREDITS.md) before spending.

## Credits

Based on [kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director), pinned to commit `d19705dea434626d4fc6e651e24cdf23c7eba156`. The upstream copyright and MIT license are preserved. See [upstream provenance](docs/UPSTREAM.md).

The Cozy cafe video is our generated production example, not an upstream showcase clip. Its use is also subject to Google's applicable terms. Public repository files deliberately exclude account emails, private Flow project links, browser screenshots, cookies, keys and downloaded account data.
