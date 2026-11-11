# U2 L17 — Reflection: Peer Review Of Visualizations

**LO:** give and receive feedback on visualizations — clarity, honesty, impact; revise from feedback.

**Estimated time:** 85 minutes (was ~65). We move slower so the review is substantive and the revision is deliberate.

---

Today is a review day. You read a partner's repo through their GitHub link, score it on three dimensions, and then revise one of your own charts from the feedback you receive.

---

## PART 1 — WHAT MAKES A CHART GOOD? (15 min)

Before you score anyone, agree on the standard. In your notes, answer:

1. **What is the difference between a chart that is *unclear* and one that is *dishonest*?**

   > **Expected:** Unclear = the audience cannot figure out what the chart says (missing labels, confusing encoding, jargon). Dishonest = the chart *appears* clear but leads the audience to a wrong conclusion (truncated axis, hidden data gaps, selective highlighting). One is a mistake; the other is a lie.

2. **Name one way a chart can be technically correct but still mislead its audience — think about the three-audience exercise from U2 L14.**

   > **Expected (examples):** Truncating the y-axis to exaggerate a small trend; plotting two series on different y-axes without labeling it; showing a 3-day spike as "the trend" while hiding 60 days of flat data; using area encoding for 1D data (bubble size for a single value).

**We will use three scoring dimensions all day, each 1–5:**

| Dimension | 5 means... |
|---|---|
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

Clarity:  1  2  3  4  5   — because: ________________________________________
Honesty:  1  2  3  4  5   — because: ________________________________________
Impact:   1  2  3  4  5   — because: ________________________________________

One suggestion — specific and actionable:
______________________________________________________________________________
```

**Examples of specific suggestions:**
- "Move the legend outside the plot (add `bbox_to_anchor=(1.05, 1), loc='upper left'` and `plt.tight_layout()`) so it doesn't cover data."
- "Your y-axis starts at 30, which shrinks the visible drop — start at 0 or add a note explaining why."
- "The title says 'Phishing Reports' but the chart also has failed logins — rename to 'Phishing Reports and Failed Logins Over Time'."
- "Histogram bins=50 is too noisy for 60 data points — drop to 15 so the shape is readable."
- "Analysis paragraph mentions 'the spike on day 14' but the chart x-axis is dates — add the date (Oct 14) to the analysis."

**Rules of review:**
- ☐ Score **before** you talk — form first, conversation second
- ☐ **Every score gets a "because"** — a score without a reason is a guess
- ☐ **Every review ends with one suggestion**, not zero and not ten
- ☐ "Looks good" is not a review

Then swap roles. You will each give and receive a full review.

---

## PART 3 — REVISE ONE CHART FROM FEEDBACK (25 min)

Open your own repo and pick the **one** chart your reviewer's suggestion would help most:

```bash
pwd
cd ~/compmath-u2-data-lab
git pull
```

- ☐ Make the **exact change** your partner suggested (or, if you disagree, write one sentence in your journal defending why).
- ☐ Re-run `python3 project_charts.py` and regenerate the PNG.
- ☐ Update that chart's paragraph in `analysis.md` if the change altered the story.

**Commit the revision:**

```bash
cd ~/compmath-u2-data-lab
git add project_charts.py analysis.md
git commit -m "revise chart from peer feedback"
git push
```

**Password prompt = Personal Access Token, not your GitHub password.**

---

## PART 4 — JOURNAL (15 min)

Open your journal file in your repo and answer in 3–4 sentences:

1. What did your partner catch that you could not see yourself? Why do you think you missed it?
2. Which of the three dimensions — clarity, honesty, impact — is hardest to get right, and why?
3. What is the one habit you will carry into every chart you ever make?

**Why a journal:** It creates a permanent, versioned record of your review literacy. The skill of *receiving* feedback and *acting on it* is the skill that separates junior analysts from senior ones.

---

## PART 5 — PUSH (5 min — same loop, now routine)

```bash
cd ~/compmath-u2-data-lab
git add analysis.md
git commit -m "L17 peer review journal"
git push
```

**Reminders:**
- **Asked for a username/password?** Use your GitHub username plus your **Personal Access Token (PAT)** — never your GitHub password. Raise your hand if yours is lost.
- **Success?** You should see a push confirmation line. The loop is now: Edit → add → commit → push.

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

One screenshot showing, in order:
1. Your completed feedback forms (all three charts, scores + suggestion)
2. Your revised chart's new PNG (the change your partner suggested)
3. The successful `git push`

Submit the screenshot to the U2 L17 assignment on Google Classroom.

**Keep the terminal open** — spot-checks happen.

---

## WHY THIS MATTERS (the bigger picture)

**Peer review is not a formality — it is the quality gate.** Every professional visualization workflow (journalism, research, product analytics, security reporting) has a review step. The person who made the chart is the *worst* person to evaluate it — they know what they meant. The reviewer represents the audience.

**The three dimensions scale:**
- **Clarity** → "Can my boss read this in 5 seconds on a phone?"
- **Honesty** → "Will my boss make a wrong decision because of how I drew this?"
- **Impact** → "Did I answer the question, or just show data?"

**Next class (U2 L18) is the Project Final Push:** polish what the review exposed, then submit. The Unit 2 assessment follows. Bring your journal and be ready to mark your Reds.

**Then U2 L18 (after that)** is the final project push.

**Next:** U2 L18 — Project Final Push: Polish And Submit  
[U2-L18-Project-Final-Push-Polish-And-Submit.md](U2-L18-Project-Final-Push-Polish-And-Submit.md)