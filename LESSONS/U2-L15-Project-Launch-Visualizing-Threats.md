# U2 L15 — Project Launch: Auditing a Clean Dataset

**LO:** launch the Unit 2 project; prove the threat dataset is trustworthy with a script you wrote; write a claim and build Chart 1.

**Estimated time:** 50 minutes (one period). Re-timed from 85 so every block fits.

---

This is the **project launch day**. The break assignment (U2 L14 Part 3) was paper-only — you chose a dataset, wrote a claim, and sketched three charts. Today you turn those sketches into a working repo, a verified dataset, and one finished chart.

**Your audience is your choice** — security team, principal, or parents — but you must *say who it is* in your analysis, because that choice decides your titles, your wording, and what you highlight.

**Three required visualizations**, all built from **verified** data, each saved as a PNG, each with a 1-paragraph written analysis:

1. **Daily timeline** — a line chart of `phishing_reports` and `failed_logins` over the dates in the file. Does trouble spike on certain days? Do the two lines move together?
2. **Weekday vs weekend** — a bar chart comparing average values on weekdays against weekends. Is the attack activity a school-week pattern?
3. **Login success rate** — a histogram of `login_success_rate`. Where do most days sit, and are there suspicious outliers on the low end?

---

## PART 0 — SETUP: REPO READY (10 min)

```bash
pwd
cd ~/compmath-u2-data-lab
git pull
ls data/
```

- This is the first thing that happens today — pull before you do anything else.
- If `git pull` reports a conflict in `LESSONS/` or `self_check.py` (you edited a copy by accident), reset those files and pull again:
  ```bash
  git checkout -- LESSONS self_check.py
  git pull
  ```
- If your clone lives somewhere else, `cd ~` first and check with `ls`.
- Run every command today **from the repo root** (`~/compmath-u2-data-lab`). Every path in this lesson is relative to it.
- The dataset for this project is `data/u2_campus_threat_daily.csv` (60 rows, synthetic, seed 20261027).

**Open it and read the header row.** Know your column names before you write code — this is the single thing that makes the build days fast.

**Expected columns (verify in your file):**
```
date, phishing_reports, failed_logins, phishing_clicks, login_success_rate
```

- `phishing_clicks` — clicks on a phishing link that day. Your chart 2 metric choice may use it.
- No `total_logins` column. If you see that name anywhere in your lesson copy, your clone is stale: `git pull`.

**Why this dataset is different:** It has a `date` column (string, ISO format `YYYY-MM-DD`). You will need it in order for the timeline chart — `matplotlib` can plot strings directly as categories, so `plt.plot(dates, values)` works if `dates` is a list of strings in order.

**This file is clean on purpose.** Somebody made a tidy dataset and handed it to you. Today your job is not to clean it — it is to **prove it is clean**, with a script that would catch a defect if one were there. "Trust me" is not evidence. A checker you can read is.

---

## PART 1 — AUDIT THE THREAT DATA (15 min)

Create `clean_threats.py` in your repo, then open it:

```bash
cd ~/compmath-u2-data-lab
touch clean_threats.py
code clean_threats.py
```

This is your **audit script** — it gets submitted with your charts.

Your script runs four checks, and it must report the result of each one, not just "done":

1. **Header** — exactly the five expected columns, in order.
2. **Row count** — 60 rows, and every row accounted for.
3. **Cells** — no blanks; counts are whole numbers inside sane bounds; `login_success_rate` is between 0.0 and 1.0.
4. **Dates** — real `YYYY-MM-DD` dates, unique, one day apart, inside the term window (2026-10-05 to 2026-12-03).

On a clean file, a working audit ends with **0 dropped** — and that number is worth nothing unless your checker would actually catch a defect. That is why this script has a `--drill` mode: it injects three broken rows and proves your checks fire. You will run the drill tomorrow in U2 L16.

**Your script (`clean_threats.py`):**

```python
import csv
import re
import sys
from datetime import date

RAW   = "data/u2_campus_threat_daily.csv"
CLEAN = "data/u2_campus_threat_daily_clean.csv"

flags = [a for a in sys.argv[1:] if a.startswith("--")]
args  = [a for a in sys.argv[1:] if not a.startswith("--")]
if args or set(flags) - {"--drill"}:
    sys.exit("usage: python3 clean_threats.py [--drill]")
DRILL = "--drill" in flags

EXPECTED_HEADER = ["date", "phishing_reports", "failed_logins",
                   "phishing_clicks", "login_success_rate"]
SANITY = {
    "phishing_reports":   (0, 100),
    "failed_logins":      (0, 5000),
    "phishing_clicks":    (0, 100),
    "login_success_rate": (0.0, 1.0),
}
FIRST_DAY, LAST_DAY = date(2026, 10, 5), date(2026, 12, 3)
EXPECTED_ROWS = 60
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# --drill injects these rows in memory. Nothing is written in drill mode.
DRILL_TEXT = """# drill file -- 3 good rows, 3 broken rows
date,phishing_reports,failed_logins,phishing_clicks,login_success_rate
2026-10-05,12,33,5,0.4
2026-10-06,9,21,4,0.52
2026-10-07,8,19,3,0.58
2026-10-08,,14,2,0.61
2026-10-09,7,17,1,1.4
2026-10-1X,6,15,2,0.49
"""

def check(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f" -- {detail}" if detail else ""))
    return ok

def to_int(value):
    s = str(value).strip()
    return int(s) if s.isdigit() else None

def to_rate(value):
    try:
        return float(str(value).strip())
    except ValueError:
        return None

# 1. READ
if DRILL:
    print("DRILL MODE -- 3 broken rows injected in memory; nothing will be written")
    text = DRILL_TEXT
else:
    with open(RAW, newline="") as fh:
        text = fh.read()

all_lines = text.splitlines(True)
comments = [ln for ln in all_lines if ln.startswith("#")]
lines = [ln for ln in all_lines if not ln.startswith("#")]

reader = csv.DictReader(lines)
if reader.fieldnames != EXPECTED_HEADER:
    print("HEADER MISMATCH")
    print("  expected:", EXPECTED_HEADER)
    print("  found:   ", reader.fieldnames)
    sys.exit(1)

rows = list(reader)
rows_in = len(rows)
print(f"Rows in: {rows_in}")

# 2. CHECK every row (date first, so a bad date is never blamed on another column)
clean_rows = []
dropped = {"blank": 0, "unparseable": 0, "impossible": 0, "bad date": 0}
seen = set()

for r in rows:
    reason = None
    bucket = None

    d = None
    raw_date = (r.get("date") or "").strip()
    if not DATE_RE.match(raw_date):
        reason, bucket = f"bad date {raw_date!r} (not YYYY-MM-DD)", "bad date"
    else:
        d = date(*map(int, raw_date.split("-")))
        if not (FIRST_DAY <= d <= LAST_DAY):
            reason, bucket = f"bad date {raw_date} (outside {FIRST_DAY}..{LAST_DAY})", "bad date"
        elif d in seen:
            reason, bucket = f"bad date {raw_date} (duplicate)", "bad date"

    for col in ("phishing_reports", "failed_logins", "phishing_clicks") if not reason else []:
        if (r.get(col) or "").strip() == "":
            reason, bucket = f"blank {col}", "blank"
        else:
            value = to_int(r[col])
            if value is None:
                reason, bucket = f"unparseable {col}={r[col]!r}", "unparseable"
            else:
                lo, hi = SANITY[col]
                if not (lo <= value <= hi):
                    reason, bucket = f"impossible {col}={r[col]!r} (allowed {lo}..{hi})", "impossible"
                else:
                    r[col] = value

    if not reason:
        if (r.get("login_success_rate") or "").strip() == "":
            reason, bucket = "blank login_success_rate", "blank"
        else:
            rate = to_rate(r["login_success_rate"])
            lo, hi = SANITY["login_success_rate"]
            if rate is None:
                reason, bucket = f"unparseable login_success_rate={r['login_success_rate']!r}", "unparseable"
            elif not (lo <= rate <= hi):
                reason, bucket = f"impossible login_success_rate={r['login_success_rate']!r} (allowed {lo}..{hi})", "impossible"
            else:
                r["login_success_rate"] = rate

    if reason:
        dropped[bucket] += 1
        print(f"  DROP {raw_date or '?'}: {reason}")
        continue

    seen.add(d)
    clean_rows.append(r)

rows_out = len(clean_rows)
rows_dropped = rows_in - rows_out

# 3. PROVE -- one line per check, with the number it is based on
accepted = sorted(seen)
gaps = [f"{a} -> {b}" for a, b in zip(accepted, accepted[1:]) if (b - a).days != 1]
span = f"{accepted[0]}..{accepted[-1]}" if accepted else "no valid dates"
if DRILL:
    date_ok = not gaps
else:
    date_ok = (not gaps) and accepted[:1] == [FIRST_DAY] and accepted[-1:] == [LAST_DAY]
date_detail = f"{len(accepted)} dates {span}" + (f", gaps: {gaps[:3]}" if gaps else "")

print("Checks:")
check("source comment lines", len(comments) == (1 if DRILL else 0),
      f"{len(comments)} '#' line(s) ignored")
check("header matches the five expected columns", True)
check("row count", rows_in == (6 if DRILL else EXPECTED_ROWS), f"{rows_in} rows read")
check("no blank cells", dropped["blank"] == (1 if DRILL else 0), f"{dropped['blank']} blank")
check("counts are integers in bounds",
      dropped["unparseable"] == 0 and dropped["impossible"] == (1 if DRILL else 0),
      f"unparseable {dropped['unparseable']}, impossible {dropped['impossible']}")
check("dates unique, contiguous, inside the term window", date_ok, date_detail)
print(f"Rows out: {rows_out}")
print(f"Rows dropped: {rows_dropped}  {dropped}")
print(f"Reconciliation: {rows_out} kept + {rows_dropped} dropped = {rows_in} in")

# 4. DECIDE
if DRILL:
    if rows_dropped != 3:
        sys.exit(f"DRILL FAILED: expected 3 dropped rows, got {rows_dropped}. "
                 "Your checker is missing a defect.")
    print("DRILL PASSED: 3 dropped, 3 kept, nothing written")
else:
    if rows_dropped != 0:
        sys.exit(f"REAL RUN ABORTED: {rows_dropped} rows failed checks. Nothing written. "
                 "Fix the data or the code before continuing.")
    if rows_in != EXPECTED_ROWS:
        sys.exit(f"REAL RUN ABORTED: expected {EXPECTED_ROWS} rows, found {rows_in}. Nothing written.")
    with open(CLEAN, "w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(EXPECTED_HEADER)
        for r in clean_rows:
            writer.writerow([r[col] for col in EXPECTED_HEADER])
    print(f"Wrote {CLEAN}")
    print(f"All checks passed: {rows_in} rows verified, 0 dropped")
```

**Run it:**
```bash
python3 clean_threats.py
```

**Expected output — five lines of evidence, then the verdict:**
```
Rows in: 60
Checks:
  [PASS] source comment lines -- 0 '#' line(s) ignored
  [PASS] header matches the five expected columns
  [PASS] row count -- 60 rows read
  [PASS] no blank cells -- 0 blank
  [PASS] counts are integers in bounds -- unparseable 0, impossible 0
  [PASS] dates unique, contiguous, inside the term window -- 60 dates 2026-10-05..2026-12-03
Rows out: 60
Rows dropped: 0  {'blank': 0, 'unparseable': 0, 'impossible': 0, 'bad date': 0}
Reconciliation: 60 kept + 0 dropped = 60 in
Wrote data/u2_campus_threat_daily_clean.csv
All checks passed: 60 rows verified, 0 dropped
```

**If your output does not match:** read the `DROP` lines. A `DROP` line in a real run means your script found a broken row — and the script refuses to write the clean file. Do not "fix" it by deleting the check. Bring it to me.

**Why this matters:** A chart built on unverified data is a lie with axes. Tomorrow you will run `python3 clean_threats.py --drill` and prove your checks actually fire. A checker that never fails is not a checker.

---

## PART 2 — WRITE YOUR CLAIM AND PLAN (10 min)

On paper (your break notes or fresh), finalize:

**My audience:** ______________________ (security team / principal / parents)

**My dataset:** `u2_campus_threat_daily_clean.csv`

**My one-sentence claim:** ________________________________________________

**Three charts:**
1. **Daily timeline** — line chart: x = date, y = phishing_reports AND failed_logins (two lines, legend, alpha=0.7)
2. **Weekday vs weekend** — bar chart: x = ["Weekday", "Weekend"], y = average phishing_reports (and/or failed_logins) — decide which metric supports your claim
3. **Login success rate** — histogram: x = login_success_rate (bins=15), y = count of days

**For each chart, write the exact title you will use** (audience-aware, from U2 L14).

---

## PART 3 — BUILD CHART 1: DAILY TIMELINE (12 min)

Create `project_charts.py`, then open it. Start with Chart 1:

```bash
touch project_charts.py
code project_charts.py
```

```python
import csv
import matplotlib.pyplot as plt

with open("data/u2_campus_threat_daily_clean.csv", newline="") as f:
    rows = list(csv.DictReader(f))

# Data is already sorted by date in the file
dates = [r["date"] for r in rows]
phishing = [r["phishing_reports"] for r in rows]
failed = [r["failed_logins"] for r in rows]

plt.figure(figsize=(10, 5))
plt.plot(dates, phishing, marker="o", label="Phishing reports", alpha=0.7)
plt.plot(dates, failed, marker="s", label="Failed logins", alpha=0.7)
plt.title("Daily Phishing Reports and Failed Logins — Oct 5 to Dec 3, 2026")
plt.xlabel("Date")
plt.ylabel("Count")
plt.legend()
plt.xticks(rotation=45)   # angle the date labels so they don't overlap
plt.tight_layout()        # prevents label cutoff
plt.savefig("chart1_timeline.png", dpi=150)
plt.clf()
```

**Run it:** `python3 project_charts.py`

**Open `chart1_timeline.png` and verify:**
- Two lines, different markers, both visible (alpha=0.7)
- Legend shows both labels
- X-axis dates readable (rotated 45°)
- Title states the finding, not just the columns
- **Y-axis starts at 0** (honest axis — `plt.ylim(bottom=0)` if needed)

**Audience check:** If your audience is parents, is the title jargon-free? If security team, does it highlight the spikes?

---

## PART 4 — SAVE YOUR WORK (3 min)

```bash
cd ~/compmath-u2-data-lab
git add clean_threats.py data/u2_campus_threat_daily_clean.csv project_charts.py chart1_timeline.png
git commit -m "project: audit threats, chart1 timeline"
git push
```

**Password prompt = Personal Access Token, not your GitHub password.**

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

1. **One screenshot** of your `clean_threats.py` terminal output — all six `[PASS]` lines, `Rows out: 60`, `Rows dropped: 0`, and `All checks passed: 60 rows verified, 0 dropped`.
2. Screenshot of `chart1_timeline.png` open in VS Code.
3. Your written claim and audience choice (photo of paper or text in a file).

Submit to the U2 L15 assignment on Google Classroom.

**Keep the terminal open** — spot-checks happen, and tomorrow you run the drill in the same terminal.

---

## CHART RULES (for the rest of the project — no exceptions)

- ☐ Title, x-axis label, y-axis label — every time
- ☐ Legend when more than one line or bar series appears
- ☐ `plt.savefig("name.png")` **before** `plt.show()`, or your PNG comes out blank
- ☐ A short comment above each chart's code saying what it shows
- ☐ Verify the data **before** charting — a chart built on unverified data is a lie with axes

---

## WHY THIS MATTERS (the bigger picture)

**The project is not "make three charts" — it is "answer a question with evidence."** The claim you wrote in Part 2 is the hypothesis. The three charts are the evidence. The audit script is the proof that the evidence is trustworthy. If any piece is missing, the argument collapses.

**Build days (U2 L16–L17):** You will have two lab periods to run the drill, build Charts 2 and 3, write the three analyses, and polish. Students who leave today with a verified dataset, a clean claim, and one finished chart will build Charts 2 and 3 in one period each. Students who don't will spend both periods debugging data issues.

**Next:** U2 L16 — Project Lab: Build Your Visualizations  \
[U2-L16-Project-Lab-Build-Your-Visualizations.md](U2-L16-Project-Lab-Build-Your-Visualizations.md)

**Then:** U2 L18 — Project Final Push: Polish and Submit  \
[U2-L18-Project-Final-Push-Polish-And-Submit.md](U2-L18-Project-Final-Push-Polish-And-Submit.md)
