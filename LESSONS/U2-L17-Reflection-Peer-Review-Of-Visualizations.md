# U2 L17 — Reflection: Peer Review of Visualizations

**LO:** give and receive feedback on visualizations — clarity, honesty, impact; revise from feedback.

**Estimated time:** 85 minutes.

---

## PART 1 — WHAT MAKES A CHART GOOD? (15 min)

Before you score anyone, agree on the standard. In your notes, answer:

**What is the difference between a chart that is *unclear* and one that is *dishonest*?**

**Expected:** Unclear = the audience cannot figure out what the chart says (missing labels, confusing encoding, jargon). Dishonest = the chart *appears* clear but leads the audience to a wrong conclusion (truncated axis, hidden data gaps, selective highlighting). One is a mistake; the other is a lie.

**Name one way a chart can be technically correct but still mislead its audience — think about the three-audience exercise from U2 L14.**

**Expected (examples):** Truncating the y-axis to exaggerate a small trend; plotting two series on different y-axes without labeling it; showing a 3-day spike as "the trend" while hiding 60 days of flat data; using area encoding for 1D data.

**We will use three scoring dimensions all day, each 1–5:**

| Dimension | 5 means... |
| --- | --- |
| **Clarity** | I understood the chart with no explanation: title, labels, legend all do their job. The audience never has to guess. |
| **Honesty** | The chart says exactly what the data says — no dropped context, no inflated axes, no hidden gaps. Y-axis starts at 0 (or states why not). Missing data is acknowledged. |
| **Impact** | The one thing the audience should notice jumps out immediately. The chart has a *point*, not just data. |

**Write these definitions in your notes** — you will reference them for every score.

---

## PART 2 — STRUCTURED SWAP (30 min)

Get your partner's repo link (their GitHub URL from yesterday's PR). Clone or read it on github.com, then review **all three** required charts.

**For each chart, fill out the feedback form in your notes:**

```
Chart: [timeline / weekday / histogram] (circle one)
Clarity: 1 2 3 4 5 — because: ________________________________________
Honesty: 1 2 3 4 5 — because: ________________________________________
Impact:  1 2 3 4 5 — because: ________________________________________
One suggestion — specific and actionable:
______________________________________________________________________________
```

**Examples of specific suggestions:**
- "Add `bbox_to_anchor=(1.05, 1), loc='upper left'` to move legend outside plot area"
- "Add `plt.tight_layout()` to prevent label clipping"
- "Y-axis on bar chart starts at 42 — must start at 0 or explain why"
- "Histogram uses 100 bins — too noisy; try 20"

**Rules of review:**
- Be specific. "Make it better" is not feedback.
- Reference the three dimensions by name.
- If you cannot read a label, that is a clarity score of 1.

Then swap roles. You will each give and receive a full review.

---

## PART 3 — REVISE ONE CHART FROM FEEDBACK (25 min)

Open your own repo and pick the **one** chart your reviewer's suggestion would help most:

```bash
cd ~/compmath-u2-data-lab
python3 project_charts.py
# edit the specific chart code
python3 project_charts.py
# verify the fix
code analysis.md
# update the corresponding paragraph if needed
```

**Commit the revision:**

```bash
git add project_charts.py chart*.png analysis.md
git commit -m "L17: peer review revision - [describe fix]"
git push
```

**Password prompt = Personal Access Token, not your GitHub password.**

---

## PART 4 — JOURNAL (15 min)

Open your journal file in your repo:

```bash
code journal-$(whoami).md
```

Answer in 3–4 sentences:

**Why a journal:** It creates a permanent, versioned record of your review literacy. The skill of *receiving* feedback and *acting on it* is the skill that separates junior analysts from senior ones.

---

## PART 5 — PUSH (5 min)

```bash
git add journal-$(whoami).md
git push
```

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

One screenshot showing, in order:

```
git push
```

Submit the screenshot to the U2 L17 assignment on Google Classroom.

**Keep the terminal open** — spot-checks happen.

---

## WHY THIS MATTERS

**Peer review is not a formality — it is the quality gate.** Every professional visualization workflow (journalism, research, product analytics, security reporting) has a review step. The person who made the chart is the *worst* person to evaluate it — they know what they meant. The reviewer represents the audience.

**The three dimensions scale:** Clarity, Honesty, Impact. These are the same criteria your project will be graded on.

**U2 L18 (tomorrow) is the final polish:** You will have one more lab period to incorporate any remaining feedback, add the audience-choice chart if you want, and submit the final PR. The project is due at the end of U2 L18.

---

## NEXT

**U2 L18 — Project Final Push: Polish and Submit** [U2-L18-Project-Final-Push-Polish-And-Submit.md](LESSONS/U2-L18-Project-Final-Push-Polish-And-Submit.md)