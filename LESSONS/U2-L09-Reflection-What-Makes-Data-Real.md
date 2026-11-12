# U2 L09 — Reflection: What Makes Data Real?

**LO:** reflect on data provenance — where does data come from, and can you trust it?

**Estimated time:** 70 minutes (was ~50). We move slower so the provenance habit becomes automatic.

---

Today starts on paper and ends in the terminal — you will need your workspace for Parts 3 and 4. No coding until late. Your job today: figure out where data actually comes from, and whether you should believe it.

---

## PART 1 — OPENING REVIEW: WHAT HAPPENED LAST WEEK (15 min)

Before anything new, let's reconstruct the previous lesson (U2 L08 — loading and cleaning data).

**Answer these in your notes first; then we go over them as a class. Do not look at your old code yet.**

1. What are the three things every honest chart needs? (Title, axis labels, units.)
2. Why did `plt.show()` not do anything useful in the terminal, and what did we use instead?
3. What does `savefig()` do, and where did your file end up?

**By the end of this part you should be able to say in one sentence:** **A chart is only as honest as the data underneath it.**

**Why this review:** U2 L08 was your first end-to-end data-to-viz pipeline. If you can't articulate the steps, you don't own them yet — and U2 L10 builds directly on them.

---

## PART 2 — PROVENANCE CHAIN: WHO, WHY, HOW, WHEN (20 min)

Every dataset has a backstory. In small groups, pick any dataset you can think of — the weather report, a video game leaderboard, a class survey, TikTok's "For You" recommendations — and build its **provenance chain**. Four questions, in order:

1. **Who** collected it? (A person? A sensor? A program? A government agency?)
2. **Why** did they collect it? (Were they paid? Curious? Selling something? Regulatory compliance?)
3. **How** did they collect it? (Interview? Automatic logging? A guess? Scraping? Survey?)
4. **When** did they collect it? (Last week? Ten years ago? Continuous stream? One-time snapshot?)

**Each group posts its chain on the board.** Then we sort the datasets into "I'd trust this" versus "I'd double-check this" — and the interesting answer is almost always: **it depends on what I'm using it for.**

**Example — weather report:**
- Who: National Weather Service (government sensors + models)
- Why: Public safety, aviation, agriculture — mandated by law
- How: Radar, satellites, weather balloons, surface stations — calibrated instruments
- When: Continuous, updated hourly
- Trust level: High for tomorrow's rain, lower for 10-day forecast

**Example — class survey:**
- Who: Teacher (you)
- Why: To understand the class
- How: Google Form, voluntary response
- When: One day in September
- Trust level: Low for "what all teenagers think," high for "what *this* class thinks on that day"

---

## PART 3 — IS OUR DATA REAL? (20 min)

Open your **compmath-u2-data-lab** repo — start in the terminal, always:

```bash
pwd
cd ~/compmath-u2-data-lab
ls data
```

You have been using `data/u2_student_performance_data.csv` all week: 1,000 rows of students with study hours, sleep, GPA, absence rates. Now the uncomfortable question: **is any of this real?**

**First answer in your notes, then discuss as a class:**

1. Do 1,000 real students' records with this many personal columns (gender, parent education, GPA, absence rate) seem likely to be sitting in a public CSV?
2. If I told you a program generated these rows from random ranges, what clues would you look for in the file itself?
3. Open the file in VS Code and scroll. Write down at least **two clues that support "synthetic"** and **two that support "real"** — then defend your call.

**The honest answer for our file:** It is **synthetic** — generated to be realistic enough to practice on. That is not a weakness. Synthetic data lets us practice on numbers that behave like the real thing without shipping anyone's private information. But it changes what we are allowed to *claim* from our charts.

**Why this distinction matters:**
- **Real data** → you can make claims about the population it represents (with caveats)
- **Synthetic data** → you can only make claims about *the synthetic process* ("students generated with these parameters show X pattern")
- **Confusing the two** → is how bad science and bad policy happen

---

## PART 4 — HOW CAN YOU TELL? (15 min)

A provenance checklist, one line per item. In your notes, write what each question catches:

| Checklist question | What it catches |
|---|---|
| **Is there a source named?** | A file with no origin story is a red flag — you can't verify what you can't trace. |
| **Do the rows contradict themselves?** | A 3-year-old with a GPA is data that was never checked against reality (domain logic violation). |
| **Are the numbers *too* clean?** | Real measurements are messy and uneven. Perfectly uniform distributions = likely fabricated. |
| **Is it surprisingly complete?** | Real data almost always has holes (non-response, sensor dropout, privacy redaction). 100% complete = suspicious. |
| **Does the date fit the story?** | Data collected before the thing existed is fabricated. "2023 TikTok trends" in a 2020 dataset = impossible. |

**In-class activity:** I will hand out two tiny files on the board — one real-looking, one synthetic — and you vote. We keep score on how often the class is right.

**Why this skill transfers:** You will encounter datasets in college, internships, news articles, and job interviews. The person who asks "where did this come from?" before analyzing is the one who doesn't get fooled.

---

## PART 5 — JOURNAL (10 min)

In your data-lab repo (you are already inside it — verify with `pwd`):

```bash
touch journal-$(whoami).md
```

Open `journal-$(whoami).md` in VS Code and answer in 3–4 sentences each:

1. Where did our performance data come from, and why does that matter for the charts I made last week?
2. Name one real-world dataset you use (or that is used on you). What is its provenance chain, and what would you have to believe to trust it?
3. One rule I will apply to every dataset from here on:

**Why a journal file in the repo:** It creates a permanent, versioned record of your thinking. Future you (and I) can see how your data literacy evolved across the unit.

---

## PART 6 — PUSH (10 min — same loop as U2 L08, now routine)

Your journal is already inside your repo, so push it. Type each command exactly:

```bash
cd ~/compmath-u2-data-lab
git add journal-$(whoami).md
git commit -m "Journal: data provenance"
git push
```

**Reminders:**
- **Asked for a username/password?** Use your GitHub username plus your **Personal Access Token (PAT)** — never your GitHub password. Raise your hand if yours is lost.
- **Success?** You should see a push confirmation line. The loop is now: Edit → add → commit → push.

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

One screenshot showing, in order:
1. Your `ls data` output with the dataset files visible
2. Your journal answers open in VS Code
3. The successful `git push`

Submit the screenshot to the U2 L09 assignment on Google Classroom.

**Keep the terminal open** — spot-checks happen.

---

## WHY THIS MATTERS (the bigger picture)

**Data provenance is not a unit — it's a lens.** Every chart you build from U2 L10 through the Unit 2 project (U2 L15–L18) should carry this question in the background: *Where did this come from, and what am I allowed to claim?*

The Unit 2 project (visualizing campus threat data) uses a synthetic dataset (`u2_campus_threat_daily.csv`). You will need to state its provenance explicitly in your final submission: *"This data is synthetic, generated for this course. Patterns shown are illustrative, not predictive of real threats."*

**Next:** U2 L10 — Scatter Plots and Relationships  
[U2-L10-Scatter-Plots-And-Relationships.md](U2-L10-Scatter-Plots-And-Relationships.md)