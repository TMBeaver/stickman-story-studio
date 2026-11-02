# The Man Who Sold His Happiest Memory

An original emotional fantasy mystery, designed as **one ten-minute master and ten connected sixty-second episodes**. All narration, titles and eventual captions are in English.

## Read the story

- [Complete narration script](SCRIPT.md)
- [Sixty-scene visual plan](STORYBOARD.md)
- [Cast, rules and continuity](STORY_BIBLE.md)
- [Production and delivery plan](PRODUCTION_PLAN.md)
- [Machine-readable scene ledger](production.json)
- [Clean narration transcript](narration/master.txt), with individual episode transcripts in the same folder

**Status: script and editorial planning draft, awaiting user review and an actual voice audition. No generation submitted for this story and no credits spent.** All scene times are planning targets; exact one-minute delivery must be checked against measured narration and the final edit.

## Premise

An illustrator sells his happiest memory to pay the rent. When his sister reveals what he sold, he returns to the shop and discovers a wealthy collector buying the most precious moments of an entire town. What begins as a desperate attempt to recover one afternoon becomes a choice between holding onto the past and saving the person still beside him.

## Ten-part escalation

| Part | Local payoff | Ending / handoff |
| --- | --- | --- |
| 01 — The Price of Happiness | The bargain really works. | He sold the last afternoon his family had with Dad. |
| 02 — No Refunds | The memory still exists, but he cannot buy it back. | His father had also sold a memory: his son's first breath. |
| 03 — The Second Customer | The shop serves collectors, not the people who made the memories. | A stranger is watching Milo's last afternoon. |
| 04 — Someone Else's Happiness | The siblings find a route to their jars. | A broken seal sends a memory back to its owner. |
| 05 — The Broken Seal | They could free the other memories too. | Their father's payment covered Milo's hospital bill. |
| 06 — What Dad Paid | Dad sacrificed a treasured moment to give Milo a future. | The collector discovers them and locks the outer door. |
| 07 — Two Jars or Everyone | The siblings find an escape but choose to save more than themselves. | The keeper recognizes a drawing made by his daughter. |
| 08 — The Keeper's Daughter | The keeper recovers a memory and helps them escape. | The collector's pursuit starts a fire in the furnace room. |
| 09 — The Jar He Left Behind | Milo saves Lena instead of returning for his satchel. | Both of their father's irreplaceable moments are destroyed. |
| 10 — What Was Still Here | The surviving memories go home; the siblings make a new moment. | The spilled lemonade transforms the opening memory into a lived present. Complete ending. |

The ninth ending is a loss, not a fake death or a reversal undone in part ten. The final part closes the main question. No unrelated cliffhanger or mandatory sequel is added after the resolution.

Rebuild the derived script and ledger from the repository root with:

```powershell
python scripts/prepare-memory-story.py
```

The source keeps exact narration alongside each principal picture. Do not edit generated transcripts independently and then overwrite them accidentally; revise the source and regenerate them together.
