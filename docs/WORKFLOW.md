# Tested Flow workflow

## 1. Prepare

Open https://flow.google.com/ in a supported browser. Sign into the intended account and inspect its actual available credits. The assistant should verify browser control and current page before promising to operate it. In our test, connected Chrome worked; native Opera automation stopped because the URL could not be verified.

For a new story, prepare the exact narration, character design, setting, emotional change and shot timeline. Use one simple causal action per beat. Our test was a distracted phone check -> deliberate phone placement -> sip of coffee -> relaxed attention to the morning.

## 2. Configure

The accepted test used **Omni 1.1 Flash, 10 seconds, landscape 16:9, 720p, one output**. Select settings in the live interface; do not assume defaults match. The editor may show a different default model for a subsequent edit; this does not change the recorded model of an already generated clip.

The Flow Agent can translate a detailed request into a generation job. In the test, it displayed a confirmation for one video at 15 credits. Check the actual job and output count before confirming. Keep confirmation enabled; do not select "always approve" merely to save clicks. Only spend within the user's authorized scope and budget.

## 3. Prompt

See `../prompts/cozy-cafe-approved.txt` for the prompt recorded by Flow. The initial assistant request additionally instructed Flow to create exactly one 10-second 16:9 720p Omni video, no extra references or variants, and to show the exact credit quote before generating.

Separate these fields:

- Static identity: head, face marks, torso, limbs, accessories, outline and proportions.
- Static setting: furniture, lighting, palette and layout for this shot.
- Prop identity: count, color, shape and visible side.
- First frame: positions, ownership and contact.
- Timed actions: physical movement, reaction and meaningful camera changes.
- Final state: where objects and hands remain for the next shot.
- Audio: exact spoken text, offscreen speaker identity, ambience, synchronized SFX and restrained music.

Do not overload ten seconds with unrelated events. Avoid abstract morphing and simultaneous complicated handoffs. Generate without in-scene titles, lettering or subtitles and add readable text afterward if requested.

## 4. Generate and preserve

Submit one job and record its state. Queues can occur with free access. Wait for the existing job instead of retrying while its result is uncertain. Do not start multiple variants by accident.

Once complete, open the generated asset and download **720p Original size**. Higher-resolution upscaling may require another plan. Browser download event capture may time out even though the file downloads successfully; inspect the resulting download before repeating the action.

Name outputs by scene and take, such as `scene-003-take-01.mp4`. Keep source clips separate from edit outputs and retain the accepted take.

## 5. Inspect

Use FFprobe for codec, dimensions, frame rate and stream duration, then FFmpeg to decode the full file. Example PowerShell commands, run from a project folder:

```powershell
ffprobe -v error -show_format -show_streams -of json .\scene-001-take-01.mp4
ffmpeg -v error -i .\scene-001-take-01.mp4 -f null NUL
ffmpeg -v error -i .\scene-001-take-01.mp4 -vf "fps=1,scale=480:-1,tile=5x2" -frames:v 1 .\contact-sheet.jpg
```

Inspect complete movement at playback speed and look closely at reaches, lifts and cuts. Check two arms/two legs, head connection, hands, feet, contact, changing expressions, stable setting, object count and final state. A technically valid file can still have obvious creative defects.

Listen to all speech and the mix. Check exact words, natural phrasing, stable speaker, intelligibility, background level and unintended character speech. If the assistant cannot listen, state that limitation and ask the user to review the actual file instead of inventing a quality assessment.

The accepted sample has a disconnected head/torso appearance in some frames and more detailed hands than requested. These do not erase its user acceptance, but should inform later scoped prompt improvements. Do not replace the accepted original automatically.

## 6. Deliver

Provide the playable MP4, project manifest and important findings. Distinguish technical checks, visual inspection, listening and explicit user acceptance. Only after the user accepts the direction should longer production continue under the agreed scope and budget.
