# U2 L08 — Reading Data From Files

**LO:** load a CSV file with `csv.DictReader`, handle real-world quirks (comment lines, blank rows), and convert string values to numbers for computation.

**Estimated time:** 85 minutes.

---

## PART 0 — SETUP (10 min)

First command, always:

```bash
pwd
cd ~
git pull
```

Then open your data-lab repo and pull anything new:

```bash
cd ~/compmath-u2-data-lab
git pull
```

---

## PART 1 — THE COMMENT-LINE TRAP (15 min)

Open `data/u2_student_performance_data.csv` and look at the first few lines:

```bash
head -6 data/u2_student_performance_data.csv
```

You will see:
- Line 1: a `#` comment explaining the dataset
- Line 2: a blank line
- Line 3: the real header row

If you pass this file directly to `csv.DictReader`, the comment line becomes your header, and every column name is wrong. The fix is to filter the lines **before** they reach the reader:

```python
with open("data/u2_student_performance_data.csv", newline="") as f:
    lines = [ln for ln in f if ln.strip() and not ln.startswith("#")]
    reader = csv.DictReader(lines)
    rows = list(reader)
```

**In your notes:** why does `ln.strip()` remove the blank line? What would `ln.startswith("#")` catch?

---

## PART 2 — STRINGS ARE NOT NUMBERS (20 min)

Every value from `csv.DictReader` is a **string**. You must convert before doing math:

```python
math_scores = [float(r["Math Score"]) for r in rows]
print(f"Mean: {statistics.mean(math_scores):.1f}")
print(f"Median: {statistics.median(math_scores):.1f}")
```

**Key insight:** `"85" > "90"` is `True` in string comparison (lexicographic), but `85 > 90` is `False` numerically. Always convert.

---

## PART 3 — LOAD DATA SCRIPT (20 min)

Open `load_data.py`. It is a starter — you will extend it today. Run it:

```bash
python3 load_data.py
```

It should print:
- Row count (should be 1000)
- Column names
- Mean Math Score

**Your task:** Extend `load_data.py` to also print the mean of `Overall GPA`, `Hours Studied Per Week`, and `Absence Rate`. Handle the string→float conversion for each.

---

## PART 4 — PROVENANCE CHECKLIST (15 min)

Before any analysis, answer these in your notes for **this dataset**:

1. **Source:** Where did this data come from? (Synthetic, generated for this course)
2. **Rows:** How many rows in the raw file? How many after filtering comments/blanks?
3. **Columns:** What does each column measure? What are its units?
4. **Generation:** What was the seed or method? (Seed 20261027, Faker library)
5. **Limitations:** What can this data **not** tell you? (Not real students; correlations are engineered)

**Write your answers in your notes.** This checklist is the habit — every dataset, every time.

---

## PART 5 — JOURNAL + PUSH (5 min)

Open your journal file in your repo:

```bash
code journal-$(whoami).md
```

Answer in 2–3 sentences each:
- What surprised you about the comment-line trap?
- Why does the provenance checklist matter?

Then push:

```bash
git add load_data.py journal-$(whoami).md
git commit -m "L08: load data, provenance notes"
git push
```

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

One screenshot showing, in order:

```
python3 load_data.py
git push
```

Submit the screenshot to the U2 L08 assignment on Google Classroom.

---

## WHY THIS MATTERS

Every dataset you will ever meet has quirks: comment lines, blank rows, mixed types, missing values. The `csv` module gives you the raw pieces; **you** build the filter. This lesson teaches the first filter — skip comments and blanks — and the first conversion — strings to numbers. Every subsequent lab builds on this.

**Next:** U2 L09 — Reflection: What Makes Data Real? [U2-L09-Reflection-What-Makes-Data-Real.md](LESSONS/U2-L09-Reflection-What-Makes-Data-Real.md)