## Before you start — every session

You work on the class VS Code server, in your own clone of this repo.
Your userid shows up in your repo name, your clone URL, and your filenames
via `$(whoami)`: `whoami` prints your userid, and `$(whoami)` inserts it
automatically. If the folder is missing, re-clone it — your lesson has the
exact URL, always ending in `_student.git`.

**Pull before work, every session** — it gets any changes I pushed to your
repo since last class:

```bash
cd ~/<your-clone-folder>
git config pull.rebase false
git pull
```

- `git config pull.rebase false` tells git how to combine work; run it once,
  it is not an error if you already ran it.
- If the pull prints `Already up to date.` you have everything.
- **Asked for a username/password?** GitHub username plus Personal Access
  Token (PAT) — never your GitHub password.

---

# compmath-u2-data-lab

You received your OWN copy of this repo by accepting a GitHub invitation in
your email. This is your working repo for CSV data work in Unit 2 — including
the Visualizing Threats project.

    load_data.py     starter: load a CSV with csv.DictReader
    clean_data.py    YOU write this (L11): clean the messy values
    project.py       your scratch pad for the project's three charts
    project_charts.py  the graded charts (you write this in L16)
    data/            the Unit 2 CSV datasets (some have a # comment first line)
    LESSONS/         Unit 2 lesson guides for this repo (L08–L12, L15–L18)

Run:

    python3 load_data.py

---

## LESSONS IN THIS REPO

| Lesson | Title | Type |
|--------|-------|------|
| [U2-L08](LESSONS/U2-L08-Reading-Data-From-Files.md) | Reading Data From Files | Lab |
| [U2-L09](LESSONS/U2-L09-Reflection-What-Makes-Data-Real.md) | Reflection: What Makes Data Real? | Paper/Reflection |
| [U2-L10](LESSONS/U2-L10-Scatter-Plots-And-Relationships.md) | Scatter Plots and Relationships | Lab |
| [U2-L11](LESSONS/U2-L11-Data-Integrity-And-Clean-Data.md) | Data Integrity and Clean Data | Lab |
| [U2-L12](LESSONS/U2-L12-Paper-Check-Relationships-And-Clean-Data.md) | Paper Check: Relationships and Clean Data | Paper Check |
| [U2-L15](LESSONS/U2-L15-Project-Launch-Visualizing-Threats.md) | Project Launch: Visualizing Threats | Project Day 1 |
| [U2-L16](LESSONS/U2-L16-Project-Lab-Build-Your-Visualizations.md) | Project Lab: Build Your Visualizations | Project Day 2 |
| [U2-L17](LESSONS/U2-L17-Reflection-Peer-Review-Of-Visualizations.md) | Reflection: Peer Review of Visualizations | Paper/Reflection |
| [U2-L18](LESSONS/U2-L18-Project-Final-Push-Polish-And-Submit.md) | Project Final Push: Polish and Submit | Project Day 3 |

---

## DATASETS IN `data/`

| File | Description | Used In |
|------|-------------|---------|
| `u2_student_performance_data.csv` | 1,000 synthetic student records (seed 20261027) | L08–L12 |
| `u2_campus_threat_daily.csv` | 60 days of synthetic campus network threat data | L15–L18 |
| `u2_dataset1_study_habits.csv` | Study habits survey (52 students) | L13 (viz-basics) |
| `u2_dataset2_mental_health.csv` | Mental health survey data | L13 (viz-basics) |
| `u2_dataset3_activities.csv` | Activities survey data | L13 (viz-basics) |

**Note:** Some CSV files have a leading `#` comment line + blank line. Always filter before `csv.DictReader`:

```python
with open("data/filename.csv", newline="") as f:
    lines = [ln for ln in f if ln.strip() and not ln.startswith("#")]
    reader = csv.DictReader(lines)
```

---

## CORE SCRIPTS YOU WILL BUILD

| Script | Built In | Purpose |
|--------|----------|---------|
| `load_data.py` | L08 | Load CSV, filter comments/blanks, convert strings to numbers |
| `clean_data.py` | L11 | Cleaning pipeline for `u2_student_performance_data.csv` — drops logged by reason, counts must add up |
| `clean_threats.py` | L15 | **Audit** pipeline for the threat dataset: PASS/FAIL per check, `--drill` defect mode |
| `project_charts.py` | L16 | Three required project visualizations |
| `analysis.md` | L16–L18 | Written analysis for each chart (audience, finding, limitation) |