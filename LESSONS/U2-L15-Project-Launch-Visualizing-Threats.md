# U2 L15 — Project Launch: Visualizing Threats

**LO:** launch the Unit 2 project — load the campus threat dataset, design a cleaning pipeline, and plan three required visualizations for a specific audience.

**Estimated time:** 85 minutes.

---

## PART 0 — SETUP (5 min)

```bash
cd ~/compmath-u2-data-lab
git pull
```

---

## PART 1 — MEET THE PROJECT DATA (15 min)

The Unit 2 project uses `u2_campus_threat_daily.csv` — 60 days of synthetic campus network threat data.

```bash
head -10 data/u2_campus_threat_daily.csv
```

Columns:
- `date` — YYYY-MM-DD
- `phishing_reports` — count of reported phishing emails
- `failed_logins` — count of failed login attempts
- `login_success_rate` — fraction (0.0–1.0)
- `malware_blocks` — count of blocked malware downloads
- `vpn_connections` — count of VPN sessions
- `wifi_devices` — count of unique WiFi clients

**In your notes:** Which columns are counts? Which is a rate? Which is a date?

---

## PART 2 — BUILD YOUR CLEANING PIPELINE (30 min)

Create `clean_threats.py` modeled on your `clean_data.py` from L11.

**Your pipeline must:**
1. Load the CSV (this one has NO comment lines — but verify)
2. Parse `date` strings into `datetime.date` objects (use `datetime.strptime`)
3. Apply sanity bounds:
   - Counts (`phishing_reports`, `failed_logins`, `malware_blocks`, `vpn_connections`, `wifi_devices`) ≥ 0
   - `login_success_rate`: 0.0–1.0
   - Dates: chronological, no duplicates, no gaps > 1 day
4. Track every dropped row with reason
5. Write to `data/u2_campus_threat_clean.csv`
6. Print audit summary: original/cleaned/dropped counts by reason

**Date parsing pattern:**

```python
from datetime import datetime

def parse_date(s):
    try:
        return datetime.strptime(s.strip(), "%Y-%m-%d").date()
    except (ValueError, AttributeError):
        return None
```

**Gap detection:**

```python
dates = [parse_date(r["date"]) for r in rows if parse_date(r["date"])]
dates.sort()
for i in range(1, len(dates)):
    if (dates[i] - dates[i-1]).days > 1:
        print(f"Gap: {dates[i-1]} to {dates[i]}")
```

---

## PART 3 — RUN AND VERIFY (15 min)

```bash
python3 clean_threats.py
```

Expected: ~60 rows in, ~60 rows out (this dataset is cleaner by design). If you drop rows, document why.

Verify:

```bash
python3 -c "
import csv
from datetime import date
with open('data/u2_campus_threat_clean.csv', newline='') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
print(f'Rows: {len(rows)}')
print(f'Date range: {rows[0][\"date\"]} to {rows[-1][\"date\"]}')
for col in ['phishing_reports', 'failed_logins', 'login_success_rate']:
    vals = [float(r[col]) for r in rows]
    print(f'{col}: mean={sum(vals)/len(vals):.2f}, max={max(vals)}')
"
```

---

## PART 4 — PLAN YOUR THREE CHARTS (20 min)

**On paper**, for each of the three required visualizations, write:

### Chart 1 — Daily timeline of phishing reports and failed logins
- **Audience:** Security team (needs to spot spikes for response)
- **Chart type:** Line plot (date on x, two y-series)
- **Key decision:** Dual y-axis or normalized? How will you show both scales honestly?

### Chart 2 — Weekday vs weekend comparison
- **Audience:** Principal (needs trend overview, not daily detail)
- **Chart type:** Bar chart (weekday/weekend on x, aggregated metric on y)
- **Key decision:** Which metric? Average phishing? Total failed logins?

### Chart 3 — Histogram of login success rate
- **Audience:** Parents at open house (needs safety reassurance, no jargon)
- **Chart type:** Histogram (distribution of daily success rates)
- **Key decision:** Bin count? How to explain "success rate" simply?

**Why plan on paper first:** The project is 4 lessons (L15–L18). Students who code without a plan spend L15–L16 redoing charts. Students who plan spend L15–L16 building exactly what they envisioned and L17–L18 polishing.

---

## PART 5 — JOURNAL + PUSH (10 min)

```bash
code journal-$(whoami).md
```

Answer:
- What is your one-sentence provenance statement for the cleaned threat dataset?
- For Chart 1, what is the one thing the security team should notice?

```bash
git add clean_threats.py data/u2_campus_threat_clean.csv journal-$(whoami).md
git commit -m "L15: threat cleaning pipeline + project plan"
git push
```

---

## TURN IN — SCREENSHOT (due 23:59 tonight)

One screenshot showing:

```
python3 clean_threats.py
git push
```

Submit to U2 L15 on Google Classroom.

---

## WHY THIS MATTERS

The Unit 2 project (L15–L18) is the culmination of the unit. You are not just making charts — you are making an **argument with evidence**. The cleaning pipeline, the audience choice, the chart type, the labels, and the honesty audit all work together. Today's plan is your blueprint.

---

## NEXT

**U2 L16 — Project Lab: Build Your Visualizations** [U2-L16-Project-Lab-Build-Your-Visualizations.md](LESSONS/U2-L16-Project-Lab-Build-Your-Visualizations.md)