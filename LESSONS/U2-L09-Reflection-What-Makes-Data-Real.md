# U2 L09 — Reflection: What Makes Data Real?

**LO:** distinguish synthetic from real data; articulate a provenance statement for any dataset; practice the provenance checklist on the student performance dataset.

**Estimated time:** 70 minutes.

---

## PART 1 — OPENING QUESTION (10 min)

Before any code, answer in your notes:

**What is the difference between a dataset that describes real people and one that was generated to *look like* it describes real people?**

Write your answer. We will discuss. The distinction is not about file format — it is about **provenance**.

---

## PART 2 — THE STUDENT PERFORMANCE DATASET (20 min)

Open your data-lab repo and load the data:

```bash
cd ~/compmath-u2-data-lab
python3 -c "
import csv
with open('data/u2_student_performance_data.csv', newline='') as f:
    lines = [ln for ln in f if ln.strip() and not ln.startswith('#')]
    reader = csv.DictReader(lines)
    rows = list(reader)
print(f'Rows: {len(rows)}')
print(f'Columns: {reader.fieldnames}')
print(f'Sample row: {rows[0]}')
"
```

This dataset has **1,000 rows** of synthetic student records. It was generated with:
- **Seed:** 20261027
- **Library:** Python Faker
- **Columns:** Student_ID, Math Score, English Score, Science Score, Overall GPA, Hours Studied Per Week, Absence Rate, Extracurricular Activities, Parent Education Level

**In your notes:** What does "synthetic" mean here? Can you treat these correlations as real findings about students?

---

## PART 3 — PROVENANCE STATEMENT (20 min)

Every dataset you use must have a **provenance statement** — a one-sentence summary of where it came from and what was done to it. For this dataset, write:

> "This dataset of 1,000 synthetic student records (generated for Comp Math Unit 2, seed 20261027) was loaded from `u2_student_performance_data.csv` after filtering a leading comment line and blank row. All values are strings from CSV; numeric columns were converted with `float()` for analysis."

**Your turn:** Write the provenance statement for the campus threat dataset (`u2_campus_threat_daily.csv`). Check the file first:

```bash
head -5 data/u2_campus_threat_daily.csv
```

---

## PART 4 — THE CHECKLIST IN PRACTICE (15 min)

For the student performance dataset, complete the provenance checklist in your notes:

| Item | Your Answer |
|------|-------------|
| Source | |
| Raw rows | |
| Clean rows | |
| Generation method | |
| What it CANNOT tell you | |

**Key realization:** The correlations in this data (study hours → GPA) were *designed in*. They are not discovered truths. A real dataset might have the same pattern — but you would not know *why* without provenance.

---

## PART 5 — JOURNAL + PUSH (5 min)

Open your journal:

```bash
code journal-$(whoami).md
```

Answer in 3–4 sentences:
- If you were handed this dataset without being told it was synthetic, what would you assume?
- What is the one question you would ask the data provider before trusting any chart made from it?

Push:

```bash
git add journal-$(whoami).md
git commit -m "L09: reflection on synthetic data provenance"
git push
```

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

One screenshot showing, in order:

```
git push
```

Submit the screenshot to the U2 L09 assignment on Google Classroom.

---

## WHY THIS MATTERS

**Data without provenance is a rumor.** The provenance checklist is not bureaucracy — it is the discipline that prevents you from presenting synthetic correlations as discovered insights. In Unit 2 project (L15–L18), you will be graded on whether your provenance statement is honest and complete.

**Next:** U2 L10 — Scatter Plots and Relationships [U2-L10-Scatter-Plots-And-Relationships.md](LESSONS/U2-L10-Scatter-Plots-And-Relationships.md)