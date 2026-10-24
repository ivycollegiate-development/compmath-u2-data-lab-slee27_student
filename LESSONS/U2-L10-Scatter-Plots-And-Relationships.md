# U2 L10 — Scatter Plots and Relationships

**LO:** create scatter plots to explore relationships between two numeric variables; interpret direction, form, and strength; articulate why correlation ≠ causation.

**Estimated time:** 85 minutes.

---

## PART 0 — SETUP (5 min)

```bash
cd ~/compmath-u2-data-lab
git pull
```

---

## PART 1 — SCATTER PLOT BASICS (15 min)

A scatter plot shows the relationship between **two numeric columns**. Each point = one row.

```python
import csv
import matplotlib.pyplot as plt

with open("data/u2_student_performance_data.csv", newline="") as f:
    lines = [ln for ln in f if ln.strip() and not ln.startswith("#")]
    reader = csv.DictReader(lines)
    rows = list(reader)

study = [float(r["Hours Studied Per Week"]) for r in rows]
gpa = [float(r["Overall GPA"]) for r in rows]

plt.figure()
plt.scatter(study, gpa, s=10, alpha=0.4, color="steelblue")
plt.title("Study Hours vs GPA — Positive Association")
plt.xlabel("Hours Studied Per Week")
plt.ylabel("Overall GPA")
plt.grid(True, alpha=0.3)
plt.savefig("scatter_study_gpa.png", dpi=150, bbox_inches="tight")
```

**Run it and open the image.** What do you see?

---

## PART 2 — VOCABULARY: DIRECTION, FORM, STRENGTH (15 min)

In your notes, define each using your scatter plot:

| Term | Definition | Your Plot |
|------|------------|-----------|
| **Direction** | Positive (↗), Negative (↘), or None (flat fuzz) | |
| **Form** | Linear, curved, clustered, or no pattern | |
| **Strength** | Tight cloud = strong; diffuse = weak | |

**Key rule:** Scatter plots only show **association**, not causation.

---

## PART 3 — CORRELATION ≠ CAUSATION (20 min)

Your scatter shows study hours and GPA rising together. Three explanations fit the same picture:

1. **Causation:** Studying more → higher GPA
2. **Reverse causation:** High GPA students enjoy school → study more
3. **Third variable:** Parental involvement → both more study time AND higher GPA
4. **Selection bias:** Only students who study *and* get good grades stay in the dataset

**In your notes:** For the Math Score vs Absence Rate scatter, write two alternative explanations besides "absences cause lower scores."

---

## PART 4 — ALPHA AND OVERPLOTTING (15 min)

With 1,000 points, dots overlap. `alpha=0.4` makes overlapping dots darker = shows **density**.

```python
# Compare alpha values
for a in [0.1, 0.4, 1.0]:
    plt.figure()
    plt.scatter(study, gpa, s=10, alpha=a, color="steelblue")
    plt.title(f"alpha={a}")
    plt.xlabel("Hours Studied Per Week")
    plt.ylabel("Overall GPA")
    plt.savefig(f"scatter_alpha_{a}.png", dpi=150)
```

**In your notes:** Which alpha reveals the density best? Why does `alpha=1.0` fail with 1,000 points?

---

## PART 5 — MINI-EXERCISE: THREE SCATTERS (20 min)

Create and save three scatter plots from the student performance data:

1. **Math Score vs English Score** — title states the relationship
2. **Science Score vs Hours Studied** — include `alpha=0.4`
3. **Absence Rate vs Overall GPA** — include grid, label units

Each must have: title (states finding), x-label with units, y-label with units, `plt.grid(True, alpha=0.3)`.

Save as `scatter_math_english.png`, `scatter_science_study.png`, `scatter_absence_gpa.png`.

---

## PART 6 — JOURNAL + PUSH (10 min)

```bash
code journal-$(whoami).md
```

Answer:
- Which of your three scatters shows the strongest association? How can you tell?
- Write one "correlation ≠ causation" alternative for that pair.

```bash
git add *.png journal-$(whoami).md
git commit -m "L10: three scatter plots with labels"
git push
```

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

One screenshot showing:

```
ls -lh scatter_*.png
git push
```

Submit to U2 L10 on Google Classroom.

---

## WHY THIS MATTERS

Scatter plots are the primary tool for **relationship discovery**. But the interpretation discipline — direction, form, strength, and the causation trap — is what separates analysis from pattern-matching. The Unit 2 project (L15–L18) requires you to choose the right chart type and state the relationship honestly.

**Next:** U2 L11 — Data Integrity and Clean Data [U2-L11-Data-Integrity-And-Clean-Data.md](LESSONS/U2-L11-Data-Integrity-And-Clean-Data.md)