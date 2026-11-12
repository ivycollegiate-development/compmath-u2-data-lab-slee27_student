# U2 L12 — Paper Check: Relationships and Clean Data

**LO:** demonstrate, on paper, mastery of scatter plots and data cleaning from U2 L10–L11 before the unit project.

**Estimated time:** 70 minutes (was ~55). We move slower so the check becomes a learning tool, not just a quiz.

---

No electronics today. U2 L11 was the data-cleaning lab; U2 L13 is histograms; then the project launches in U2 L15. Today's paper check makes sure scatter-plot reading and the cleaning rules from this week are solid before everything builds on them. 25 minutes of check, then swap, correct, and one forward look at the project.

**Why a paper check now:** You've built scatter plots (U2 L10) and a cleaning pipeline (U2 L11). Both involve silent-failure bugs — `plt.clf()` omission, `float("")` crash, list mutation during iteration. Paper forces you to articulate the *why* without the REPL's instant feedback. If you can't explain it on paper, you don't own it yet.

---

## PART 1 — THE CHECK (25 min, closed notes)

Answer on the check sheet. One point each unless marked. **Show your reasoning** — not just the answer.

### Section A — Reading relationships. (from U2 L10)

**Question 1.** Name the three relationship types a scatter plot can show.

> **Expected answer:** Positive (cloud tilts up-right ↗), Negative (cloud tilts down-right ↘), No relationship (flat fuzz, no tilt).

**Question 2.** In a scatter with `alpha=0.4`, what does a *darker region* of dots mean?

> **Expected answer:** More points overlap there = higher density of observations at those (x, y) values. `alpha` makes overlapping dots accumulate opacity.

**Question 3.** Your scatter shows study hours and GPA rising together. Your partner says "studying causes the GPA." Give one *other* explanation that fits the same picture.

> **Expected answer (any valid alternative):** A third variable causes both (e.g., parental involvement → more study time AND higher GPA); reverse causality (high GPA students enjoy school more → study more); selection bias (only students who study *and* get good grades stay in the dataset); coincidence in this sample.

**Question 4.** Why do we set `s=10` and `alpha=0.4` when plotting 1,000 students, but not for 6 class averages?

> **Expected answer:** With 1,000 points, default `s=20` and `alpha=1.0` creates a solid blob where density is invisible. Small dots + transparency reveal density. With 6 points, no overlap occurs — default size and opacity work fine.

### Section B — Cleaning rules. (from U2 L11)

**Question 5.** A cell is blank. Name the two choices you have and one tradeoff of each.

> **Expected answer:**
> - Drop the row: safe for plotting axes, but loses whole observation; can bias sample if missingness is systematic.
> - Fill (impute): keeps sample size, but introduces a guess; every downstream chart is partly built on fabricated data.

**Question 6.** Why is a GPA of 9 rejected by sanity bounds while a GPA of 0.5 is kept?

> **Expected answer:** Sanity bounds reject what **cannot be true** (GPA > 4.0 on a 4.0 scale = impossible), not what is merely **surprising** (0.5 GPA = struggling student, but possible).

**Question 7.** Why does `to_float` return `None` instead of letting the crash happen?

> **Expected answer:** A crash stops the whole program. `None` marks the one bad cell and lets you keep working — you decide later (drop/fill) with an explicit `if val is None:` check. Explicit handling > implicit crash.

**Question 8.** Your cleaning drops 50 of 1,000 rows. What does that quietly change about every chart you build afterward?

> **Expected answer:** The sample changes. If the 50 dropped rows are not a random subset (e.g., all low-GPA students had blank GPAs), your cleaned dataset no longer represents the original population — averages shift, relationships may weaken or strengthen artificially.

### Section C — Predict the output. (from U2 L10–L11)

**Question 9.** What does `plt.clf()` do between two plots — and what goes wrong with your second `savefig` if you skip it?

> **Expected answer:** `plt.clf()` clears the current figure. Without it, the second plot draws on top of the first, and `savefig` saves *both* overlapped — a confusing bug where your "Sleep vs GPA" PNG also contains the "Study vs Math" points.

**Question 10.** `csv.DictReader` gives you an Age value of `"14"`. What type is it, and what must happen before it can be compared to a sanity bound?

> **Expected answer:** It's a `str` (string). Must convert with `float()` or `int()` before numeric comparison. `"14" <= 22` compares string to int — works in Python 3 but is a bug waiting to happen.

### Section D — One fix-it. (2 points)

**Question 11.** This cleaner has two bugs. Name both:

```python
SANITY = {"Overall GPA": (0.0, 4.0)}
rows = list(csv.DictReader(f))       # f is the raw file
for r in rows:
    gpa = float(r["Overall GPA"])
    if not (0.0 <= gpa <= 4.0):
        rows.remove(r)
```

> **Bug 1:** `float(r["Overall GPA"])` crashes on blank cells (`ValueError: could not convert string to float: ''`). No `try/except` or blank check.
>
> **Bug 2:** `rows.remove(r)` inside a `for r in rows:` loop mutates the list you're iterating over — Python's iterator skips the next element after a removal. Use a new list (`clean_rows.append(r)`) or iterate over a copy (`for r in rows[:]:`).

---

## PART 2 — SWAP AND GRADE (15 min)

Trade papers with your partner. Using the key I project, mark each answer and write the score at the top. **Both names go on the paper you graded.**

**Grading guidance for partners:**
- Full credit = correct answer + correct reasoning
- Half credit = correct answer, missing or wrong reasoning
- Zero = incorrect answer
- For Q11: 1 point per bug identified (max 2)

---

## PART 3 — CORRECTIONS (20 min)

Take your own paper back. Correct every miss **in a different color**, and for each miss write one line:

> **What I had in my head** vs **what is true**

**Example:**
> *What I had in my head:* "removing from a list while looping over it is fine, Python handles it."
> *What is true:* The iterator advances by index; removing shifts indices left, so the next item gets skipped.

**Why this format:** Naming the misconception explicitly helps you not repeat it. "I forgot" doesn't teach you — "I thought X but actually Y" does.

---

## PART 4 — WHAT THE CHECK TELLS US (10 min, class discussion)

Hands up by section: which section was hardest? We re-teach the top one on the board, using *your actual wrong answers*, before the project starts.

**Common patterns from past years:**
- Section A Q3: Forgetting the "correlation ≠ causation" alternatives — defaulting to "x causes y"
- Section B Q8: Not connecting dropped rows to sample bias — treating cleaning as free
- Section D Q11: Missing the list-mutation bug — one of the most common Python pitfalls

---

## PART 5 — LOOK AHEAD: THE PROJECT (15 min, in pairs)

U2 L13 covers histograms; the project launches in U2 L15 — three visualizations built from a real dataset, with cleaning you do yourself. In your notes:

**Question 1.** Your project chart must survive the question "where did this data come from?" Write the one-sentence provenance statement you would make for the student-performance dataset, including how many rows it had before and after cleaning.

> **Example:** "This dataset of 1,000 synthetic student records (generated for this course) was cleaned to 950 rows by dropping 50 rows with blank or impossible values in GPA, Age, and score columns."

**Question 2.** Predict: which is more dangerous to a chart — a blank cell or an impossible value? Defend your choice; we compare answers in U2 L13.

> **Reasoning guide:** A blank cell crashes your code (loud failure). An impossible value (GPA=9) silently skews averages, trends, and correlations (quiet failure). Quiet failures are more dangerous because they don't announce themselves.

---

## TURN IN — PAPER (collected at the end of class)

One check sheet with:
- Your Part 1 answers
- Your partner's grading marks
- Your corrections in a second color

Hand it in before you leave.

**Also:** Submit a photo of the corrected check sheet to the U2 L12 assignment on Google Classroom by 23:59 tonight.

**Keep the sheet** — it is your study guide for the unit project (U2 L15–L18) and the Unit 2 assessment (U2 L19).

---

## WHY THIS MATTERS (the bigger picture)

This check covers the **vocabulary of relationships and cleaning**:
- Scatter plot patterns (positive/negative/none, strong/weak)
- Correlation vs causation distinction
- Cleaning tradeoffs (drop vs fill, explicit vs implicit)
- Sanity bounds philosophy (impossible vs surprising)
- Silent-failure bugs (`plt.clf()`, list mutation, `float("")`)

The Unit 2 project (U2 L15–L18) assumes you can:
1. Load a new dataset
2. Write a `clean_data.py` for it (with documented choices)
3. Build scatter plots, bar charts, and histograms from the clean data
4. Write one-sentence descriptions of every relationship you visualize
5. State the data provenance in your final submission

If today revealed gaps, revisit U2 L10–L11 before U2 L13.

**Next:** U2 L13 — Histograms and Distributions  
[U2-L13-Histograms-And-Distributions.md](U2-L13-Histograms-And-Distributions.md)