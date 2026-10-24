# U2 L11 — Data Integrity and Clean Data

**LO:** build a cleaning pipeline that handles missing values, impossible values, and type traps; document every cleaning decision with an audit trail.

**Estimated time:** 85 minutes.

---

## PART 0 — SETUP (5 min)

```bash
cd ~/compmath-u2-data-lab
git pull
```

---

## PART 1 — WHAT "DIRTY" LOOKS LIKE (15 min)

Examine the raw data for problems:

```bash
python3 -c "
import csv
with open('data/u2_student_performance_data.csv', newline='') as f:
    lines = [ln for ln in f if ln.strip() and not ln.startswith('#')]
    reader = csv.DictReader(lines)
    rows = list(reader)

# Check for blanks
for col in reader.fieldnames:
    blanks = sum(1 for r in rows if not r[col].strip())
    if blanks:
        print(f'{col}: {blanks} blank cells')

# Check numeric ranges
for col in ['Math Score', 'English Score', 'Science Score', 'Overall GPA', 'Hours Studied Per Week', 'Absence Rate']:
    vals = [float(r[col]) for r in rows if r[col].strip()]
    print(f'{col}: min={min(vals):.1f}, max={max(vals):.1f}, mean={sum(vals)/len(vals):.1f}')
"
```

**Expected dirty patterns:**
- Blank cells in numeric columns
- Impossible values (GPA > 4.0, Absence Rate > 1.0, negative hours)
- Type traps: `"N/A"` or `""` in numeric columns

---

## PART 2 — THE CLEANING PIPELINE (30 min)

Open `clean_data.py`. It is a skeleton — you will implement it.

**Your pipeline must:**
1. Load the raw CSV (filter comments/blanks)
2. Convert each numeric column with a `to_float(val)` helper that returns `None` for unparseable values
3. Apply **sanity bounds** per column:
   - Scores: 0–100
   - GPA: 0.0–4.0
   - Hours: 0–168 (max hours in a week)
   - Absence Rate: 0.0–1.0
4. Track every dropped row with **why** (column, original value, reason)
5. Write cleaned rows to `data/u2_student_performance_clean.csv`
6. Print: original count, cleaned count, dropped count, drop reasons by category

**Starter `to_float` pattern:**

```python
def to_float(val):
    try:
        return float(val)
    except (ValueError, TypeError):
        return None
```

**Why `None` not crash?** A crash stops everything. `None` marks the bad cell and lets you decide: drop the row, fill the value, or flag it.

---

## PART 3 — RUN AND VERIFY (20 min)

```bash
python3 clean_data.py
```

**Expected output:**
```
Original rows: 1000
Cleaned rows: ~950
Dropped: ~50
  blank_cells: X
  impossible_values: Y
  unparseable: Z
Cleaned file written to data/u2_student_performance_clean.csv
```

Verify the clean file:

```bash
head -3 data/u2_student_performance_clean.csv
python3 -c "
import csv
with open('data/u2_student_performance_clean.csv', newline='') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
print(f'Clean rows: {len(rows)}')
for col in ['Overall GPA', 'Absence Rate']:
    vals = [float(r[col]) for r in rows]
    print(f'{col}: min={min(vals):.2f}, max={max(vals):.2f}')
"
```

---

## PART 4 — PROVENANCE UPDATE (10 min)

Update your provenance statement for the cleaned dataset:

> "This dataset of 1,000 synthetic student records (seed 20261027) was cleaned to 950 rows by dropping 50 rows with blank or impossible values in GPA, Scores, Hours, and Absence Rate columns. Cleaning script: `clean_data.py`."

Write this in your notes.

---

## PART 5 — JOURNAL + PUSH (10 min)

```bash
code journal-$(whoami).md
```

Answer:
- Which cleaning decision was hardest: dropping blanks, dropping impossibles, or something else? Why?
- If you filled blanks with column means instead of dropping, how would that change the correlations?

```bash
git add clean_data.py data/u2_student_performance_clean.csv journal-$(whoami).md
git commit -m "L11: cleaning pipeline with audit trail"
git push
```

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

One screenshot showing:

```
python3 clean_data.py
git push
```

Submit to U2 L11 on Google Classroom.

---

## WHY THIS MATTERS

**Every chart you build sits on a cleaning pipeline.** If the pipeline is undocumented, the chart is unverifiable. The Unit 2 project (L15–L18) requires a `clean_threats.py` with the same audit trail. Today's `clean_data.py` is your template.

**Next:** U2 L12 — Paper Check: Relationships and Clean Data [U2-L12-Paper-Check-Relationships-And-Clean-Data.md](LESSONS/U2-L12-Paper-Check-Relationships-And-Clean-Data.md)