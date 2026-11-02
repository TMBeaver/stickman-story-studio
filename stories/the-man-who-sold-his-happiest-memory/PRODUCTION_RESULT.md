# First-take production findings

The user requested the complete ten-part story without paid retries. Production used Google Flow in the browser for pictures, Google AI Studio for chapter narration, and local FFmpeg editing for timing, sound and captions. No subscription API entitlement was assumed.

## Generation

- Flow: Omni 1.1 Flash, 720p, landscape 16:9, ten seconds, one output per scene.
- Sixty individual scene jobs submitted once each, in ten batches of six.
- Each batch quoted 90 credits: 15 per scene, 900 total before refunds.
- Fifty-seven successful video assets; three failed jobs refunded.
- Observed account balance decreased by 855 credits. No regeneration or alternate takes.
- Narration: Google AI Studio, Gemini 3.8 Flash TTS, Bodi voice; ten separate chapter tracks, kept at native speech speed.

## Editorial replacements

E05-S06 and E06-S01 were refused by the provider's minor-related content filter. E09-S03 failed generation. These were not resubmitted.

- E05-S06 uses a locally designed animated fictional hospital invoice, making the patient's name readable.
- E06-S01 reuses the hospital corridor and bedside passage from E06-S04 as a recollection.
- E09-S03 uses a local smoke, escape and hand-contact montage from E09-S01, S04 and S05. The shelf-lifting rescue is described by the narrator; the replacement does not visibly perform the planned lift.

## Editing and checks

The six narrative paragraphs in each chapter were aligned to measured word timestamps. Small reaction beats between paragraphs bring each chapter to exactly 1,440 frames at 24 fps without stretching speech. English captions follow those actual edit timings. Music is a quiet original synthesized motif; source ambience remains low under narration.

Local QA records include full decoding, frame counts, subtitle timings, source transcription comparisons and chronological review images. All ten source narrations automatically matched the script at 98.5% or better; this is an ASR check, not proof of natural delivery. A human listening pass is still required before publishing.

## Limitations to review

The accepted ten-second example did not guarantee long-form continuity. Despite repeated cast prompts, first takes vary in clothing, hair, anatomy, bag ownership and background cast. The father is sometimes drawn as a detailed human. Some intended prop transfers and actions are only implied by narration. A few accidental technical headings were removed by cropping their top strip in the edit.

These findings mean the result should be reviewed as a first-take narrative film, not advertised as flawless character-consistent animation. Further improvements should target specifically identified scenes and require a separate retry budget. Generated films, account details and private production URLs are excluded from this public repository.

## TikTok delivery correction

The destination was clarified after landscape production: TikTok, vertical 9:16. A separate 1080x1920 adaptation reuses the clean picture edits and verified narration, retains the complete wide scenes over an animated blurred extension, and re-renders larger English captions with portrait margins. It uses no additional generation credits. The original landscape delivery remains available.

This layout preserves important group actions; it does not turn the source into natively composed portrait shots. Future videos in this series should specify 9:16 before script blocking and generation, use vertical depth and shot-specific placement, and validate the phone layout before spending the full batch budget.
