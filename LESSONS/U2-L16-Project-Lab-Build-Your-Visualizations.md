# U2 L16 — Project Lab: Build Your Visualizations

**LO:** build the three required project visualizations from cleaned threat data; apply chart-type matching, label rules, and honest axis practices.

**Estimated time:** 85 minutes.

---

## PART 0 — SETUP (5 min)

```bash
cd ~/compmath-u2-data-lab
git pull
```

Verify your clean data exists:

```bash
wc -l data/u2_campus_threat_clean.csv
```

---

## PART 1 — CREATE PROJECT CHARTS SCRIPT (60 min)

Create `project_charts.py` that builds all three required charts.

**Required charts:**

### 1. `chart1_timeline.png` — Daily timeline
- **Data:** `date` (x), `phishing_reports` and `failed_logins` (two y-series)
- **Type:** Line plot with two lines
- **Must have:** Title (states finding), x-label (Date), y-label (Count), legend, `plt.grid(True, alpha=0.3)`
- **Honesty:** If y-axis doesn't start at 0, note why in `analysis.md`

### 2. `chart2_weekday_weekend.png` — Weekday vs weekend
- **Data:** Aggregate by `date.weekday() < 5` (weekday) vs `>= 5` (weekend)
- **Metric:** Your choice (phishing reports, failed logins, or malware blocks)
- **Type:** Bar chart (two bars: Weekday, Weekend)
- **Must have:** Title, x-label (Day Type), y-label (your metric + "Count"), y-axis starts at 0
- **Honesty:** Bar chart y-axis **must** start at 0 — no exceptions

### 3. `chart3_success_rate.png` — Histogram of login success rate
- **Data:** `login_success_rate` column
- **Type:** Histogram
- **Must have:** Title, x-label (Login Success Rate), y-label (Number of Days), deliberate bin count (note your choice)
- **Honesty:** Note in `analysis.md` why you chose that bin count

**Code skeleton:**

```python
import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Load cleaned data
with open("data/u2_campus_threat_clean.csv", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

dates = [datetime.strptime(r["date"], "%Y-%m-%d").date() for r in rows]
phishing = [int(r["phishing_reports"]) for r in rows]
failed = [int(r["failed_logins"]) for r in rows]
success_rate = [float(r["login_success_rate"]) for r in rows]

# Chart 1: Timeline
plt.figure(figsize=(10, 5))
plt.plot(dates, phishing, marker="o", label="Phishing Reports", color="steelblue")
plt.plot(dates, failed, marker="s", label="Failed Logins", color="indianred")
plt.title("Daily Phishing Reports and Failed Logins — 60-Day Trend")
plt.xlabel("Date")
plt.ylabel("Count")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("chart1_timeline.png", dpi=150, bbox_inches="tight")
plt.clf()

# Chart 2: Weekday vs Weekend
# ... your code here

# Chart 3: Success Rate Histogram
# ... your code here
```

**Run and verify each chart:**

```bash
python3 project_charts.py
ls -lh chart*.png
```

Open each PNG in VS Code — confirm titles, labels, legends, honest axes.

---

## PART 2 — START ANALYSIS.MD (15 min)

Create `analysis.md` with three paragraphs (one per chart):

```markdown
# Unit 2 Project Analysis

## Chart 1: Daily Timeline
**Audience:** Security Team
**One thing they should notice:** [your answer]
**Honest limitation:** [your answer]

## Chart 2: Weekday vs Weekend
**Audience:** Principal
**One thing they should notice:** [your answer]
**Honest limitation:** [your answer]

## Chart 3: Success Rate Histogram
**Audience:** Parents
**One thing they should notice:** [your answer]
**Honest limitation:** [your answer]
```

Fill in draft answers now — you'll refine in L17–L18.

---

## PART 3 — JOURNAL + PUSH (5 min)

```bash
code journal-$(whoami).md
```

Answer: Which chart was hardest to get right? What did you have to fix?

```bash
git add project_charts.py chart*.png analysis.md journal-$(whoami).md
git commit -m "L16: three project charts + draft analysis"
git push
```

---

## TURN IN — REPO LINK (due 23:59 tonight)

1. Push your final `project_charts.py`, all three chart PNGs, and `analysis.md`
2. Confirm on github.com that all files are visible and PNGs render
3. Submit your repo link to U2 L16 on Google Classroom

---

## WHY THIS MATTERS

You are building the **evidence** for your project argument. Each chart must be technically correct (runs, saves, labels) AND honest (audience-appropriate, no truncated bar axes, documented limitations). L17 is peer review; L18 is final polish.

---

## NEXT

**U2 L17 — Reflection: Peer Review of Visualizations** [U2-L17-Reflection-Peer-Review-Of-Visualizations.md](LESSONS/U2-L17-Reflection-Peer-Review-Of-Visualizations.md)