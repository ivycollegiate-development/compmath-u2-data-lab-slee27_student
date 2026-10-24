# U2 L12 — Paper Check: Relationships and Clean Data

**LO:** demonstrate, on paper, mastery of scatter plots and data cleaning from U2 L10–L11 before the unit project.

**Estimated time:** 70 minutes.

---

## WHY A PAPER CHECK?

You've built scatter plots (L10) and a cleaning pipeline (L11). Both involve silent-failure bugs — `plt.clf()` omission, `float("")` crash, list mutation during iteration. Paper forces you to articulate the *why* without the REPL's instant feedback. If you can't explain it on paper, you don't own it yet.

The corrections are the point. A corrected miss is worth more than a lucky guess.

---

## PART 1 — THE CHECK (25 min, closed notes)

Answer on the check sheet. One point each unless marked. **Show your reasoning** — not just the answer.

### Section A — Reading relationships (from L10)

**Q1.** Name the three relationship types a scatter plot can show.

**Expected:** Positive (cloud tilts up-right ↗), Negative (cloud tilts down-right ↘), No relationship (flat fuzz, no tilt).

**Q2.** In a scatter with `alpha=0.4`, what does a *darker region* of dots mean?

**Expected:** More points overlap there = higher density of observations at those (x, y) values.

**Q3.** Your scatter shows study hours and GPA rising together. Your partner says "studying causes the GPA." Give one *other* explanation that fits the same picture.

**Expected (any valid):** Third variable causes both; reverse causality; selection bias; coincidence.

**Q4.** Why do we set `s=10` and `alpha=0.4` when plotting 1,000 students, but not for 6 class averages?

**Expected:** With 1,000 points, default `s=20` and `alpha=1.0` creates a solid blob. Small dots + transparency reveal density. With 6 points, no overlap occurs.

### Section B — Cleaning rules (from L11)

**Q5.** A cell is blank. Name the two choices you have and one tradeoff of each.

**Expected:** Drop the row (loses data, but clean) or fill/impute (keeps row count, but introduces assumptions).

**Q6.** Why is a GPA of 9 rejected by sanity bounds while a GPA of 0.5 is kept?

**Expected:** Sanity bounds reject what **cannot be true** (GPA > 4.0 on a 4.0 scale), not what is merely **surprising** (0.5 GPA = struggling student, but possible).

**Q7.** Why does `to_float` return `None` instead of letting the crash happen?

**Expected:** A crash stops the whole program. `None` marks the one bad cell and lets you keep working — you decide later (drop/fill) with an explicit `if val is None:` check.

**Q8.** Your cleaning drops 50 of 1,000 rows. What does that quietly change about every chart you build afterward?

**Expected:** The sample changes. If the 50 dropped rows are not a random subset (e.g., all low-GPA students had blank GPAs), your cleaned dataset no longer represents the original population.

### Section C — Predict the output (from L10–L11)

**Q9.** What does `plt.clf()` do between two plots — and what goes wrong with your second `savefig` if you skip it?

**Expected:** `plt.clf()` clears the current figure. Without it, the second plot draws on top of the first, and `savefig` saves *both* overlapped.

**Q10.** `csv.DictReader` gives you an Age value of `"14"`. What type is it, and what must happen before it can be compared to a sanity bound?

**Expected:** It's a `str`. Must convert with `float()` or `int()` before numeric comparison.

### Section D — One fix-it (2 points)

**Q11.** This cleaner has two bugs. Name both:

```python
for r in rows:
    gpa = float(r["Overall GPA"])
    if gpa > 4.0:
        rows.remove(r)
```

**Bug 1:** `float(r["Overall GPA"])` crashes on blank cells. No `try/except` or blank check.

**Bug 2:** `rows.remove(r)` inside a `for r in rows:` loop mutates the list you're iterating over — Python's iterator skips the next element after a removal. Use a new list (`clean_rows.append(r)`) or iterate over a copy (`for r in rows[:]:`).

---

## PART 2 — SWAP AND GRADE (15 min)

Trade papers with your partner. Using the key, mark each answer and write the score at the top. **Both names go on the paper you graded.**

---

## PART 3 — CORRECTIONS (20 min)

Take your own paper back. Correct every miss **in a different color**, and for each miss write one line:

**What I had in my head** vs **what is true**

*Example:*
- What I had in my head: "removing from a list while looping over it is fine, Python handles it."
- What is true: The iterator advances by index; removing shifts indices left, so the next item gets skipped.

**Why this format:** Naming the misconception explicitly helps you not repeat it.

---

## PART 4 — WHAT THE CHECK TELLS US (10 min)

Class discussion: which section was hardest? We re-teach the top one on the board, using *your actual wrong answers*.

---

## PART 5 — LOOK AHEAD: THE PROJECT (15 min, in pairs)

U2 L13 covers histograms; the project launches in U2 L15 — three visualizations built from a real dataset, with cleaning you do yourself. In your notes:

**Q1.** Your project chart must survive the question "where did this data come from?" Write the one-sentence provenance statement you would make for the student-performance dataset, including how many rows it had before and after cleaning.

**Example:** "This dataset of 1,000 synthetic student records (generated for this course) was cleaned to 950 rows by dropping 50 rows with blank or impossible values in GPA, Age, and score columns."

**Q2.** Predict: which is more dangerous to a chart — a blank cell or an impossible value? Defend your choice.

**Reasoning guide:** A blank cell crashes your code (loud failure). An impossible value (GPA=9) silently skews averages, trends, and correlations (quiet failure). Quiet failures are more dangerous because they don't announce themselves.

---

## TURN IN — PAPER (collected at end of class)

One check sheet with both names. Also submit a photo of the corrected check sheet to the U2 L12 assignment on Google Classroom by 23:59 tonight.

**Keep the sheet** — it is your study guide for the unit project (U2 L15–L18) and the Unit 2 assessment (U2 L19).

---

## WHY THIS MATTERS

This check covers the vocabulary of relationships and cleaning:

- `plt.clf()`, `float("")`, `try/except`, list mutation, sanity bounds, provenance

The Unit 2 project (U2 L15–L18) assumes you can:
- Read scatter plots for direction/form/strength
- Build a cleaning pipeline with audit trail (`clean_data.py`)

If today revealed gaps, revisit U2 L10–L11 before U2 L13.

---

## NEXT

**U2 L13 — Histograms and Distributions** [U2-L13-Histograms-And-Distributions.md](LESSONS/U2-L13-Histograms-And-Distributions.md)

*(Note: U2 L13 uses the viz-basics repo, but the cleaned data from this repo feeds into it.)*