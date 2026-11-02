# Production and delivery plan

## Requested deliverables

- One English **10:00 master MP4**, with locally composited subtitles.
- Ten English **01:00 episode MP4s**, cut at clean editorial boundaries.
- One master SRT and ten episode-local SRT files; optional subtitle-free master for reuse.
- Source clips, accepted-take ledger, original narration and production checkpoint stored locally in the ignored `projects/` directory.

The script files in this folder are public production documents. Provider account identifiers, keys, private links and runtime logs are not committed.

## Planning assumptions

Keep the already accepted 16:9 Cozy visual direction. Stage important action near the central area, but do not promise a clean 9:16 crop from every landscape composition. A portrait release would need its own framing pass before expensive generation.

The sixty ten-second rows are an **initial editorial plan**, not measured narration and not sixty production-ready prompts. Each minute has a local arc and a final reveal. Several planned returns to the shop and memory are intentional, rather than a mechanically new location for every row.

We will generate many short clips, assemble a master, then export the ten episodes. Flow is not being asked for one ten-minute generation. Submit jobs in bounded batches and inspect them before expanding production. A queued or uncertain job is not permission to retry and spend twice.

## Voice-first timing

1. Review the exact script and audition the intended Google voice, using the same service settings for every part.
2. Prefer one continuous narration if the chosen service reliably supports it, otherwise one track per episode with a fixed named voice and consistent settings. Google AI Pro web access does not itself establish API/TTS access.
3. Measure every actual track. The draft is roughly 140 spoken words per minute; pauses and provider delivery can materially change duration.
4. Fit each episode to 60 seconds through text tightening or a few seconds of motivated visual reaction, room tone and SFX. Do not stretch/speed speech or add random filler. Re-audition revised lines when needed.
5. Place the final reveal around 00:50-00:59, with the final word comfortably before the cut and a brief visual response. Do not cut through a word or use the next episode's narration early.
6. Lock each episode's exact script/audio before final picture timing and caption alignment. Current JSON times are target times only; `actual_audio_duration_seconds` and actual word timestamps remain null until measured.

## Sample gate

After the story is reviewed, make a bounded sample covering the shop transaction and warm memory. It must show the new cast, connected anatomy, jar style, natural voice and contrast between present and memory. Compare it to the accepted cafe quality, then review the actual adjacent-clip narrator continuity before commissioning the full sixty shots.

No story-specific generations, voice requests, subscription purchases or credit use have been made during script preparation. Do not mark the script, voice or sample as approved based only on this planning work.

## Budget

At the previously checked 15 credits for one ten-second Omni 720p output, the sixty-shot visual plan has a **900-credit one-take estimate**. A 2x-3x planning allowance is **1,800-2,700 credits**; this is a buffer, not an empirically verified success rate. Reference images, extra edit jobs, trims requiring replacement material or separate narration can add costs. Recheck live prices, balance and authorized budget before generation.

## Text inserts

Composite important details locally: the sale receipt, last-afternoon context, the first-breath title/date, auction deadline, seal/furnace warning and hospital patient's name. These inserts should be short, readable and visually integrated with the prop, not a competing wall of text. Do not present fictional medical or legal papers as real records.

## Assembly checks

Master timeline: episodes start at 0, 60, 120, 180, 240, 300, 360, 420, 480 and 540 seconds. Final end is 600 seconds. Each release has the same story content as its master segment. Avoid duplicate recaps or separate bumpers inside the sixty seconds.

Render episode boundaries on exact frames. Do not rely on stream-copy cuts at arbitrary non-keyframes: re-encode the final exports or deliberately place keyframes at every minute during master encoding. Probe exported durations and decode every file; container/audio rounding needs checking before claiming an exact runtime.

Split subtitles with cues clipped to their episode range, subtract the episode offset, and verify against actual audio. Do not manufacture an SRT from proportional word timing or treat planning timestamps as forced alignment. Keep the final words of each cliffhanger inside their own part.

Final creative check: every preceding question earns its answer, the father's death is never reversed, opening jars returns only the correct owners' memories, the cart excludes the two burned hero jars, Milo's satchel does not return after the fire, the collector faces questions about trapping the siblings rather than about an earlier stated legal purchase, and the closing spill creates a new memory.
