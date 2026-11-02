"""Build the reviewable script and shot ledger; performs no generation or network calls."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "stories" / "the-man-who-sold-his-happiest-memory"

# Each row is exact spoken narration and its principal visible action.
EPISODES = [
    ("The Price of Happiness", "Milo discovers the bargain is real.", [
        ("The first time Milo sold a memory, he asked if it would hurt. The shopkeeper said no. That was the first lie.", "Rainy alley: Milo hesitates at an amber-lit shop; inside, the keeper slides one empty jar toward him."),
        ("His rent was overdue. His drawing commissions had stopped. In his pocket, he had three coins and a key that might soon fit nothing.", "Apartment doorway: eviction envelope beside sketchbook; count exactly three coins, then close Milo's hand around his key."),
        ("The shop bought memories. A school prize paid almost nothing. A first kiss paid more. His happiest afternoon would cover the entire rent.", "Shop counter: keeper compares three different jars and pushes a thick payment envelope forward. No generated labels."),
        ("Milo chose a summer afternoon with his father. Two lemonades. A crooked drawing. His dad laughing so hard he could barely hold the pencil.", "Warm memory: teenage Milo, younger Lena and their father at a kitchen table; two lemonades, crooked star drawing, shared laughter."),
        ("A warm light slipped into the jar. Milo took the money. He remembered his father's face, but that afternoon had become an empty space.", "Extraction counter: one warm light enters sealed jar; Milo receives envelope and loses the reflected memory, not his identity."),
        ("That evening, his sister found the receipt. Her smile vanished. Of all the afternoons, she whispered, you sold the last one we had together.", "Apartment kitchen: Lena holds receipt, points to the star drawing; match its shape to the memory, then hold on Milo's reaction."),
    ]),
    ("No Refunds", "He learns that money cannot simply reverse the sale.", [
        ("Milo had sold his last afternoon with Dad. The next morning, their father had gone into hospital. He had never come home.", "Kitchen close-up: Lena opens an old photo beside the drawing; dissolve to an empty hospital chair, then return to Milo."),
        ("He knew those facts. He could repeat them. But he could no longer remember the last time his father had made him laugh.", "Milo studies the drawing and tries to recall; brief empty chair insert; his expression tightens without magical head effects."),
        ("He ran back with the money. The keeper did not touch it. Sold memories belonged to the auction house until a collector bought them.", "Night street into shop: Milo runs, sets intact envelope down; keeper refuses it and closes the auction ledger."),
        ("At midnight, the jars would leave town. The sales were legal. The buyers were wealthy. And Milo could not afford his own happiness anymore.", "Loading courtyard: numbered cases and auction invitation as post overlays; clock approaches midnight; distant elegant customers enter."),
        ("Then he saw his jar on a packing cart. Beside it sat an older one, cloudy with dust, carrying his father's name.", "Packing room through doorway: identify Milo's star-tagged jar beside one dusty jar bearing a distinct blue ribbon. Labels added in post."),
        ("Milo reached for the old receipt beneath it. The memory was called My Son's First Breath. His father had sold it twenty years ago.", "Receipt macro, composited readable title; Milo recognizes the date; cut to Lena entering behind him and seeing the same record."),
    ]),
    ("The Second Customer", "Their father's transaction opens a larger mystery.", [
        ("Their father had sold the moment Milo was born. Lena checked the date twice. It was not a mistake. Neither was the payment.", "Shop service corridor: Lena compares receipt date with a childhood photo; Milo holds the blue-ribbon jar without opening it."),
        ("The amount was enormous. Milo remembered a gentle man who patched his own coat. What could possibly have cost him that much money?", "Memory of father mending coat; match the patched sleeve to a payment figure added afterward; return to the siblings."),
        ("The keeper took the receipt away. Some people sell because they want more, he said. Some sell because someone else needs to live.", "Keeper retrieves receipt carefully, looks toward a tiny faded family photograph behind the counter; Milo notices the glance."),
        ("Before Milo could answer, a polished black car arrived. A buyer stepped out. The keeper straightened his coat and stopped looking at them.", "Front window: black car pulls up; Collector enters in charcoal coat; keeper's posture changes; siblings retreat from view."),
        ("Lena pulled her brother behind the shelves. Through a narrow doorway, they watched the buyer choose a memory and lower a glass viewing lens.", "Archive aisle: Lena draws Milo into cover; through doorway, Collector fits one selected jar into an antique viewing device."),
        ("A stranger's childhood flickered across the wall. The buyer laughed at a father's joke. Milo recognized the crooked drawing. Someone was watching his afternoon.", "Projection room: cropped hand-drawn memory replay, Collector's entertained silhouette, Milo's furious eyes; no second physical father in present."),
    ]),
    ("Someone Else's Happiness", "Milo moves from regret to action.", [
        ("A stranger was enjoying Milo's last afternoon with Dad. For the first time that night, being broke did not feel like the worst part.", "Projection booth: Milo clenches his hand; Lena catches his wrist before he steps into the light; lens continues turning."),
        ("The buyer called it charming. He asked whether the father had more memories available. The keeper said nothing. Milo nearly stepped out of hiding.", "Collector gestures toward the projected father; keeper lowers his eyes; siblings remain concealed behind the shelving."),
        ("Then the lens shut. The afternoon returned to its jar. Milo watched the keeper remove it and lock it inside a padded case.", "Device close-up: lens closes, light returns to the sealed star jar; keeper places that single jar into the case."),
        ("Lena had seen the key. She had also seen the delivery door. They could steal two jars, slip outside, and disappear before midnight.", "Lena traces a route on a scrap of paper: key hook, case, courtyard door; Milo listens and nods."),
        ("They waited for the keeper to follow the buyer. Then Lena lifted the key while Milo opened the case with both hands shaking.", "Counter close-up: Lena lifts the brass key; packing room cut: she unlocks case as Milo opens its lid."),
        ("His sleeve caught a tiny jar on the shelf. It fell. The seal cracked. Somewhere outside, a woman began to cry with relief.", "One small jar falls from an adjacent low shelf; wax seal splits; warm light exits toward an older woman beyond window."),
    ]),
    ("The Broken Seal", "The siblings discover a way to return the stolen moments.", [
        ("The dropped jar had given its memory back. Outside, the woman pressed a hand to her mouth, remembering something she had thought was gone.", "Courtyard window: older woman stops, touches her cheek and smiles through tears; match back to the empty cracked jar."),
        ("Milo picked up the glass. It was empty. Breaking a seal released the memory to its original owner. Keeping it sealed kept it trapped.", "Packing room floor: Milo raises the empty jar by its intact base; Lena notices the split wax and fading warm trail."),
        ("They could free their two jars right there. Instead, Lena turned toward the shelves. Hundreds of other people's happiest days waited in the dark.", "Lena's eyeline leads into rows of sealed amber jars; Milo holds his star jar and father's blue-ribbon jar, both still sealed."),
        ("A school concert. A wedding morning. A quiet goodbye. The little tags made each jar sound small. Together, they looked like an entire town.", "Archive inserts: visual symbols on tags, hands in memories behind glass; all readable descriptions composited in editing."),
        ("Then they found the disposal chute. Broken glass went to a furnace. Its warning was simple: a burned memory could never be returned.", "Rear workroom: closed furnace, chute and heat glow; a posted warning added in post; sister pulls Milo back from opening it."),
        ("Beside the furnace stood their father's auction file. Inside was a hospital invoice. The patient was not their father. The patient was Milo.", "Workroom desk: Lena opens invoice from blue-ribbon file; reveal a small childhood photo attached to it, then Milo's recognition."),
    ]),
    ("What Dad Paid", "The emotional midpoint reveals the father's sacrifice.", [
        ("Milo had been sick as a baby. He knew the family story: a long hospital stay, a successful operation, a father who never complained.", "Warm hospital memory: bundled infant Milo behind cot rails; father on waiting bench clutching a medical envelope; no graphic imagery."),
        ("What nobody had told him was how the bill got paid. His father had walked into this same shop with nothing left to sell.", "Earlier version of the same storefront: younger keeper receives father; rain and patched sleeve connect this moment to episode three."),
        ("Except one thing. The first time his baby had gripped his finger. A tiny hand. A whole new life. His happiest memory.", "Memory close-up: infant hand curls around father's finger; father bends close, stunned and tender; restrained camera move."),
        ("He traded that moment for the operation. Then he went home and learned to love his son without remembering the moment he first had.", "Father accepts payment, then returns to cot and takes child's hand again; establish a new present moment, not a restored memory."),
        ("Milo looked at his own sealed jar. Dad had lost a beginning to give him a future. Milo had sold their ending for rent.", "Present workroom: blue-ribbon jar beside star jar in Milo's hands; his shame shifts toward resolve as Lena steadies him."),
        ("He reached for the seal. Footsteps stopped behind them. The buyer was watching. He said the jars were his now, and locked the door.", "Collector appears in doorway; Milo shields both jars; Collector locks the outer workroom door, leaving an interior archive route accessible."),
    ]),
    ("Two Jars or Everyone", "A personal escape becomes a choice to help others.", [
        ("The buyer locked them inside with the memories. He had seen the cracked jar. Now he wanted his shipment gone before they broke another.", "Locked workroom: Milo tests outer door; beyond high window, Collector directs an empty handcart toward loading courtyard."),
        ("Lena found a narrow service passage behind the shelves. At its end was the delivery hatch, wide enough for one person at a time.", "Interior archive passage: Lena spots service route, opens low hatch to courtyard; no teleporting or new exit in locked door."),
        ("They had a way out. Two jars. A clear street. Milo could go home with everything he had come to save that night.", "Hatch viewpoint: safe courtyard beyond; Milo carries both jars; Lena crouches beside escape opening and waits."),
        ("But on the shelf beside him was a jar tagged with a child's drawing. A little girl holding the hand of an older man.", "Archive shelf close-up: a child-drawn family tag hangs from one pale pink-ribbon jar; Milo stops before the hatch."),
        ("He put his jars in his satchel. Then he pulled an empty delivery cart toward the shelves. Lena watched him, sighed, and started loading.", "Both hero jars go into Milo's ochre satchel; siblings load other sealed jars into a shallow padded cart, below its rim."),
        ("A hand caught the cart before it rolled. The keeper stood in the passage. He looked at the girl's drawing and whispered, My daughter.", "Keeper enters from accessible front archive route, stops cart by handle and recognizes pink-ribbon tag; leave both hands visible."),
    ]),
    ("The Keeper's Daughter", "The apparent accomplice chooses to help.", [
        ("The keeper recognized the drawing, but not the afternoon inside the jar. He had sold it years ago, when keeping the shop seemed worth anything.", "Service passage: keeper studies tag with shame; his faded photograph matches the daughter shown in the child drawing."),
        ("Over time, he had sold more. Her first song. Her ridiculous jokes. The sound of her coming home. He still knew her name.", "Three brief bounded memory inserts show younger keeper and daughter; each fades back into separate sealed jars on shelf."),
        ("But knowing a name, he said, was not the same as remembering a life. He had spent years protecting shelves he could not bear to empty.", "Keeper's cramped office: family photograph behind ledger, warm jars reflected in his glasses; he closes the ledger and rises."),
        ("He took the pink ribbon off the shelf. For a moment, Milo thought he would hide it. Instead, the keeper broke the seal.", "Archive aisle: keeper lifts only pink-ribbon jar, twists wax stopper to break seal, keeps glass body intact."),
        ("The old man's face crumpled into a smile. Then he unlocked the courtyard gate. Take the cart, he said. Take every jar you can.", "Warm light reaches keeper; he unlocks courtyard gate from inside, then helps siblings push padded cart through the service hatch."),
        ("Behind them, the loading door slammed open. The buyer saw the escaping cart, grabbed a shelf, and tipped it toward the furnace controls.", "Workroom: Collector bursts through outer door he locked, yanks shelf in pursuit; metal frame strikes furnace control, sparks at panel."),
    ]),
    ("The Jar He Left Behind", "The physical climax forces Milo's real choice.", [
        ("The falling shelf tore open the furnace chute. Hot glass spilled across the floor. A curtain caught fire. The passage filled with smoke.", "Furnace workroom: broken chute opens, glowing debris hits curtain; smoke develops along ceiling, escape route still briefly visible."),
        ("Outside, the keeper dragged the memory cart clear. Inside, Lena's coat caught beneath the fallen frame. Milo heard her call his name.", "Courtyard: keeper pulls cart to safety; cut inside: Lena's sage sleeve trapped under metal frame, Milo turns back toward her."),
        ("He pulled at the shelf. It would not move. He dropped his satchel, planted both feet, and lifted while Lena pulled herself free.", "Milo places satchel on floor near doorway, braces feet and lifts one end of shelf; Lena withdraws trapped sleeve and crawls clear."),
        ("They stumbled into the rain. Only then did Milo see his bag inside, beside the fire. His last afternoon with Dad was still in it.", "Courtyard threshold: siblings emerge together; eyeline back to ochre satchel through smoky doorway; no hero jars elsewhere."),
        ("He took one step toward the doorway. Lena reached for him. For a second, he held the hand that was here, and wanted what wasn't.", "Close-up: Lena catches Milo's hand; camera holds both living hands, then rack focus to the satchel beyond the unsafe threshold."),
        ("Milo stayed. The ceiling gave way. Behind the falling sparks, two small lights went dark. His father's beginning. Their last afternoon. Both gone.", "Milo turns fully toward Lena; seen from safe courtyard, roof section collapses over satchel and two enclosed lights extinguish; no graphic injury."),
    ]),
    ("What Was Still Here", "The final episode pays off the loss and resolves the story.", [
        ("Milo saved his sister. He could not save the jars. By morning, the shop was ash, and the cart stood untouched across the street.", "Dawn courtyard: firefighters in distant simplified silhouettes, contained ruins; padded cart safe across street with keeper and siblings."),
        ("They broke the seals one at a time. Warm lights rose above the rooftops. Across town, people stopped in doorways and remembered their own lives.", "Siblings and keeper open surviving jars individually; warm lights travel toward homes, wedding ring, school piano and hospital bedside."),
        ("The keeper's daughter arrived before noon. He remembered her terrible jokes now. She told another. He laughed before she reached the ending.", "Quiet street bench: adult daughter in rose cardigan sits with keeper; his recognition and laugh answer episode eight's absence."),
        ("The buyer demanded his property. Lena told the officers who had locked them inside. They took him aside. His money couldn't answer their questions.", "Ruined storefront exterior: Collector reaches for empty case; Lena identifies him to two briefly visible officers, who lead him aside for questioning."),
        ("That evening, Milo opened his sketchbook beside Lena. He tried to draw their father laughing. The face came easily. The afternoon did not.", "Apartment kitchen: Milo sketches father's face, pauses at empty background; Lena sits beside him with two lemonades and a clean page."),
        ("Then Lena knocked over her lemonade. The drawing was ruined. They looked at each other, and laughed. This time, Milo wasn't missing the moment.", "Lemonade spills over fresh crooked drawing; shared stunned glance becomes whole-body laughter; settle on hands and new drawing, warm light, final cut."),
    ]),
]


def stamp(seconds):
    return f"{seconds // 60:02d}:{seconds % 60:02d}"


def build():
    DEST.mkdir(parents=True, exist_ok=True)
    (DEST / "narration").mkdir(exist_ok=True)
    ledger = []
    episodes = []
    for ep_index, (title, payoff, rows) in enumerate(EPISODES, 1):
        narration = "\n\n".join(row[0] for row in rows)
        words = len(re.findall(r"\b[\w]+(?:['’-][\w]+)*\b", narration))
        assert len(rows) == 6
        assert 120 <= words <= 155, (ep_index, words)
        episode = {
            "episode": ep_index,
            "title": title,
            "target_start_seconds": (ep_index - 1) * 60,
            "target_duration_seconds": 60,
            "word_count": words,
            "payoff": payoff,
            "ending": rows[-1][0],
            "narration_file": f"narration/episode-{ep_index:02d}.txt",
            "actual_audio_duration_seconds": None,
            "status": "script-draft-awaiting-review",
        }
        episodes.append(episode)
        (DEST / episode["narration_file"]).write_text(narration + "\n", encoding="utf-8")
        for scene_index, (vo, picture) in enumerate(rows, 1):
            start = (ep_index - 1) * 60 + (scene_index - 1) * 10
            ledger.append({
                "id": f"E{ep_index:02d}-S{scene_index:02d}",
                "episode": ep_index,
                "target_start_seconds": start,
                "target_end_seconds": start + 10,
                "target_episode_start_seconds": (scene_index - 1) * 10,
                "narration": vo,
                "principal_picture": picture,
                "cliffhanger": scene_index == 6 and ep_index < 10,
                "status": "planned-not-generated",
                "accepted_take": None,
                "actual_word_timestamps": None,
                "credit_quote": None,
                "charged_credits": None,
            })
    total = sum(ep["word_count"] for ep in episodes)
    manifest = {
        "title": "The Man Who Sold His Happiest Memory",
        "genre": "Original fictional mystery / emotional fantasy",
        "language": "en",
        "style": "Cozy Storytelling: warm painterly 2D environments and expressive minimalist characters",
        "target_master_seconds": 600,
        "episode_count": 10,
        "target_episode_seconds": 60,
        "aspect_ratio": "16:9, center-safe staging for optional later portrait adaptation",
        "word_count": total,
        "timing_status": "Editorial targets only. Actual original-speed narration must be measured before final shot timing and subtitles.",
        "script_approval": None,
        "voice_audition_approval": None,
        "video_sample_approval": None,
        "spending_authorization": None,
        "planned_generation_outputs": 60,
        "estimated_one_take_video_credits": 900,
        "planning_credit_allowance": {"low": 1800, "high": 2700, "not_a_provider_quote": True},
        "episodes": episodes,
        "scenes": ledger,
    }
    (DEST / "production.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    script = [
        "# The Man Who Sold His Happiest Memory",
        "",
        "**Original fictional story. English narration. Ten connected one-minute episodes.**",
        "",
        f"Draft narration: **{total:,} words**. Each paragraph is one planned visual beat, approximately ten seconds. These are editorial targets, not measured speech timings.",
        "",
        "Use one adult male offscreen storyteller throughout: General American, warm clean medium-low voice, gentle chest resonance, no exaggerated rasp or breathiness, natural conversational phrasing, stable vocal identity and close dry recording. Dialogue is narrated in that same voice; characters do not lip-sync. Audition before locking a provider voice. Do not add direction text to the spoken transcript.",
        "",
        "Aim to land the final reveal in each part's last 8-10 seconds, then leave a short reaction before the exact one-minute cut. The next part immediately pays off the preceding question. No repeated recaps or spoken subscription requests. Episode ten ends the story.",
        "",
    ]
    for ep, (_, _, rows) in zip(episodes, EPISODES):
        start = ep["target_start_seconds"]
        script += [f"## Part {ep['episode']:02d} — {ep['title']}", "", f"**Master target: {stamp(start)}–{stamp(start+60)} · {ep['word_count']} spoken words**", ""]
        script += [p for row in rows for p in (row[0], "")]
    (DEST / "SCRIPT.md").write_text("\n".join(script), encoding="utf-8")
    board = ["# Storyboard and scene ledger", "", "Planning document only: no generation submitted. All times are target master-video times. Exact narration is in SCRIPT.md and production.json.", "", "Sixty principal pictures, one per planned ten-second generation. Each description supplies an establishing state, a purposeful physical action and an ending/reaction. Add the full frozen cast/style/voice blocks to production prompts after script approval. Deliberate returns to the shop/archive and memory locations are story-driven exceptions to the upstream new-location default; use scale and viewpoint changes without transforming the furniture.", "", "| Scene | Target | Principal picture / action |", "| --- | --- | --- |"]
    for scene in ledger:
        board.append(f"| {scene['id']} | {stamp(scene['target_start_seconds'])}–{stamp(scene['target_end_seconds'])} | {scene['principal_picture']} |")
    (DEST / "STORYBOARD.md").write_text("\n".join(board) + "\n", encoding="utf-8")
    (DEST / "narration" / "master.txt").write_text("\n\n".join("\n\n".join(r[0] for r in e[2]) for e in EPISODES) + "\n", encoding="utf-8")
    print(json.dumps({"episodes": len(episodes), "scenes": len(ledger), "total_words": total, "episode_words": [e["word_count"] for e in episodes]}))


if __name__ == "__main__":
    build()
