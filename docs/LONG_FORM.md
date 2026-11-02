# Building longer films

Long videos are edited sequences of short generated clips. The approved route supports ten-second Omni clips; there is no assumption that one request can reliably produce an entire five-minute film.

## Story and timing

Write one complete narrative with a clear opening tension, causal development and earned payoff. Plan narration and visual meaning together. A minute can start with roughly six ten-second segments, but cuts may trim clips and natural speech timing may require additional material. Do not create six unrelated mini-stories or repeat the same action to fill time.

Maintain a scene ledger containing narration, setting, cast, prop state, key action, camera direction, incoming/outgoing state, estimated credits, take selection and trim points. Use the included manifest template. A manifest is a production record, not an executable prompt or proof of actual provider output.

## Continuity

Freeze the complete protagonist anchor and repeat it in every generation. When available, use an approved character reference or a shot-specific opening frame, keeping an identity reference distinct from the opening composition. Use the accepted last usable frame as a reference when a continuous action benefits from it; choose a clean point, not blindly the final frame.

Preserve body proportions, limb count, outline, props, visible sides, ownership and screen direction. Change locations deliberately to support the story. The upstream Cozy default introduces another recognizable main location per new ten-second segment unless a single-location story or a return is intentionally chosen. Record those decisions rather than accidentally resetting the world.

## Voice

Our ten-second sample generated voice inside the video. Independent clip narration can drift between speakers, timbre and pace, even with repeated text instructions. For a longer film:

1. First test adjacent clips with one frozen voice profile, exact narration and stable music direction.
2. Listen across the cut before committing the whole budget.
3. If consistency is inadequate, use one continuous external narration track or fixed-provider chapter tracks, with the user's selected voice and approved service access.
4. Time the edit to actual original-speed speech. Avoid long dead air, repeated narration and forced speech stretching.

An external voice service is optional, not bundled into this repository. Google AI Pro and Gemini API access have separate setup and quota rules. Check current service terms rather than assuming a consumer plan supplies API credit.

## Bounded production

Approve a representative ten-to-twenty-second sample before preparing every expensive shot. Then generate in small batches, review each batch, and retry only failed scenes. Preserve the accepted opening and all usable outputs. Save a checkpoint after every submitted/completed job to prevent duplicate generation after interruptions.

Reserve a planning allowance of **2x to 3x the one-take credit estimate**, depending on how strict anatomy, continuity and performance must be. This is a suggested buffer, not a measured success rate or a guarantee that it is sufficient.

## Assembly

Trim at story actions, reactions or intentional location changes. Avoid indiscriminate crossfades that blur line-art characters. Match audio level, remove duplicate music/voice where replacing them, and keep room tone or music continuous across cuts where appropriate. Add synchronized captions in post-production with safe margins and natural phrase boundaries.

FFmpeg can assemble compatible streams without re-encoding. For clips with differing formats, normalize them before concatenation or use a video editor. Do not assume every output shares frame rate, dimensions, pixel format and audio settings: inspect first.

The final pass must cover the whole film, not only its opening: no anatomy/prop failures, no unexplained cast changes, no repeated filler, stable narrator and music, readable captions and complete ending. Deliver the MP4, subtitles when present, ledger, costs and any remaining limitations.
