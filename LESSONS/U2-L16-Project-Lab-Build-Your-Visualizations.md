# U2 L16 — Project Lab: Build Your Visualizations

**LO:** work day — prove your audit actually catches defects, then build Chart 2 and start Chart 3 with audience-aware analysis.

**Estimated time:** 50 minutes (one period). This is a work day, and the checklist below is more than one period of work: **today's minimum target is the drill run plus Chart 2.** Chart 3 and the analysis polish continue in U2 L17.

---

Today is a work day. Everything stays in **your own data-lab repo**.

---

## PART 0 — OPEN YOUR REPO, AUDIT IT, THEN DRILL IT (15 min)

```bash
pwd
cd ~/compmath-u2-data-lab
git pull
```

### Step 1 — Re-run your audit (3 min)

```bash
python3 clean_threats.py
```

Confirm six `[PASS]` lines, `Rows out: 60`, `Rows dropped: 0`, and `All checks passed`.

**Write the output in your notes:**
- Rows in: ______
- Rows out: ______
- Rows dropped: ______

### Step 2 — Run the defect drill (10 min) — this is today's graded evidence

Your audit reported 0 dropped. That number means nothing unless your checker would actually catch a broken row. Prove it:

```bash
python3 clean_threats.py --drill
```

The drill builds three deliberately broken rows in memory — it never touches your data file — and runs them through the same checks. **Expected output:**

```
DRILL MODE -- 3 broken rows injected in memory; nothing will be written
Rows in: 6
  DROP 2026-10-08: blank phishing_reports
  DROP 2026-10-09: impossible login_success_rate='1.4' (allowed 0.0..1.0)
  DROP 2026-10-1X: bad date '2026-10-1X' (not YYYY-MM-DD)
Checks:
  [PASS] source comment lines -- 1 '#' line(s) ignored
  [PASS] header matches the five expected columns
  [PASS] row count -- 6 rows read
  [PASS] no blank cells -- 1 blank
  [PASS] counts are integers in bounds -- unparseable 0, impossible 1
  [PASS] dates unique, contiguous, inside the term window -- 3 dates 2026-10-05..2026-10-07
Rows out: 3
Rows dropped: 3  {'blank': 1, 'unparseable': 0, 'impossible': 1, 'bad date': 1}
Reconciliation: 3 kept + 3 dropped = 6 in
DRILL PASSED: 3 dropped, 3 kept, nothing written
```

**Before you move on, read the three `DROP` lines out loud to yourself.** Blank in one column, impossible value in another, bad date in the third — three different checks firing, three different reasons. That is what a real audit looks like when it finds something.

**Screenshot this terminal now.** It is the evidence that your checker works, and it is what I grade for rubric item D.

**If the drill fails** (`DRILL FAILED: expected 3 dropped rows`): your checker is missing a defect. Fix the script before you build any chart — a chart built on an unverified file is exactly the problem this project is about.

### Step 3 — Confirm Chart 1 (2 min)

```bash
python3 project_charts.py
```

`chart1_timeline.png` should appear and match yesterday's. If it does not exist, building it is your first job today.

---

## PART 1 — THE CHECKLIST (25 min of work today)

Work through this top to bottom. **Today's minimum: Chart 2 finished and pushed.** Do not write analysis for a chart that does not exist yet.

### The audit (done yesterday, verified today)

- ☐ `clean_threats.py` reads `data/u2_campus_threat_daily.csv` with `csv.DictReader`
- ☐ Comment lines (starting with `#`) are stripped before parsing
- ☐ Every row is checked and **each check prints PASS or FAIL with its count**
- ☐ The real run writes `data/u2_campus_threat_daily_clean.csv` and refuses to write if any row fails
- ☐ The `--drill` run drops exactly 3 rows, for 3 different reasons, and writes nothing
- ☐ Dates are verified unique, one day apart, and inside 2026-10-05 to 2026-12-03

### Chart 1 — Daily timeline (line chart) — done in U2 L15

- ☐ `phishing_reports` and `failed_logins` plotted over the dates (two lines)
- ☐ Different markers (`marker="o"`, `marker="s"`) and `alpha=0.7` so both are visible
- ☐ Legend shows which line is which (`label=` + `plt.legend()`)
- ☐ Title states the finding, audience-aware (e.g., "Phishing Reports Peak at 17 in Mid-October — Security Team Alert" vs "Campus Attacks Follow the School Week — Parents' View")
- ☐ X-axis label: "Date", Y-axis label: "Count"
- ☐ `plt.xticks(rotation=45)` + `plt.tight_layout()` so dates don't overlap
- ☐ Y-axis starts at 0 (honest axis) — add `plt.ylim(bottom=0)` if needed
- ☐ Saved as `chart1_timeline.png` with `plt.savefig()` **before** any `plt.show()`
- ☐ `plt.clf()` after saving

### Chart 2 — Weekday vs weekend (bar chart) — today's minimum

- ☐ Compute averages separately for weekdays and weekends:
  ```python
  # Parse date string to determine weekday/weekend
  from datetime import datetime
  def is_weekend(date_str):
      return datetime.strptime(date_str, "%Y-%m-%d").weekday() >= 5  # 5=Sat, 6=Sun
  ```
- ☐ Accumulate sums and counts for each group, then average (float division `/`, not `//`)
- ☐ Two bars (or grouped bars if showing both phishing and failed logins), clearly labeled
- ☐ **Put the two averages on the chart** (e.g. `plt.text()` or value labels) — a bar chart of two bars should show its two numbers
- ☐ Title states the finding, audience-aware
- ☐ X-axis label: "Day type", Y-axis label: "Average count" (or "Average failed logins")
- ☐ Saved as `chart2_weekday_weekend.png`
- ☐ `plt.clf()` after saving

**Check your numbers against the real data:** weekday phishing reports average **7.98** (44 days), weekends **2.88** (16 days). Weekday failed logins **23.64**, weekends **7.19**. If your chart shows different averages, you have a bug in your grouping, not a discovery.

### Chart 3 — Login success rate (histogram) — starts today, finishes in L17

- ☐ Extract `login_success_rate` values from clean rows
- ☐ Choose bin count **on purpose** (not default): `bins=15` is a good starting point for 0–1 rates
- ☐ Title states the finding, audience-aware. This dataset's honest finding is **not** "most days near 100%": the median day sits at **0.56**, only 4 of 60 days are above 0.90, and one Saturday (2026-10-24) collapses to **0.0**. Something like "Most Days Sit Between 45% and 72% Login Success — One Day Collapses to 0%" is defensible; "Most Days Near 100%" is false and I will mark it wrong.
- ☐ X-axis label: "Login success rate", Y-axis label: "Number of days"
- ☐ `edgecolor="white"` so bins are separable
- ☐ Saved as `chart3_success_rate.png`
- ☐ `plt.clf()` after saving

### Writing — one paragraph per chart in `analysis.md`

Create `analysis.md` in your repo. For **each chart**, write one paragraph that includes:

1. **What the chart shows, in plain words, for your named audience** — no jargon if audience is parents; technical terms OK for security team.
2. **The one number or pattern you most want that audience to notice** — be specific: "phishing reports average 7.98 on weekdays against 2.88 on weekends, a 2.8× gap" not "there are spikes."
3. **One honest limitation** — a gap in the data, a small sample (60 days), an outlier that might be noise, the synthetic nature of the data.

**Example paragraph for Chart 1 (security team audience), written from the real numbers:**

> This timeline shows daily phishing reports (blue circles) and failed logins (orange squares) across 60 days, from 2026-10-05 to 2026-12-03. Both metrics track the school week: phishing reports average 7.98 on weekdays against 2.88 on weekends, and failed logins average 23.64 against 7.19. The peak is 17 phishing reports on 2026-10-12, a Monday; Mondays average 9.6 reports versus 7.7 on Wednesdays, so the day-of-week pattern is real but milder than the weekday/weekend gap. Limitation: this is 60 days of synthetic data with one extreme low outlier (2026-10-24), so the weekday/weekend gap should be read as a pattern in this file, not a measured trend in real traffic.

---

## PART 2 — COMMON PITFALLS (5 min, then back to work)

The three ways this project goes wrong, in order of how often I see them:

1. **Charting a file nobody verified.** One blank or malformed row and your timeline has a hole or your histogram a phantom bin. **Audit first, always.** Your `clean_threats.py` output and your drill screenshot are the proof you did it.
2. **Missing labels.** An untitled chart is a picture, not an analysis. If I have to guess what an axis means, the chart fails. **Title, x-label, y-label — every time.**
3. **Uncommented chart code.** Each chart's block needs a one-line comment saying what it shows — future-you (and your reviewer tomorrow) needs the map.

**If your PNGs are blank:** You called `plt.show()` before `plt.savefig()`, or you closed the figure before saving. Fix the order — **save then show**.

---

## PART 3 — PARTNER SANITY-CHECK (5 min)

Swap screens with your partner and look at **one** chart each:

- Can you tell, from the chart alone, what it shows? **No explanation allowed first.**
- Show your partner your drill screenshot. Can they tell what your checker catches?
- Give **one specific compliment** and **one specific suggestion**. "Looks good" is not a review.

**Fix anything your partner caught BEFORE you commit.**

---

## PART 4 — SAVE YOUR WORK (5 min)

```bash
cd ~/compmath-u2-data-lab
git add clean_threats.py project_charts.py analysis.md chart1_timeline.png chart2_weekday_weekend.png
git commit -m "project: audit drill proven, chart2 weekday vs weekend"
git push
```

**Password prompt = Personal Access Token, not your GitHub password.**

**Milestone for today:** drill screenshot taken, Chart 2 pushed with its analysis paragraph.

---

## TURN IN — PULL REQUEST LINK (due 23:59 tonight)

1. Screenshot of your `--drill` run: 3 `DROP` lines with 3 different reasons, then `DRILL PASSED`.
2. Push your `project_charts.py`, `analysis.md`, `chart1_timeline.png`, `chart2_weekday_weekend.png`.
3. On github.com, open or update a Pull Request from your repo back to the original repo (Contribute → Open pull request).

Submit the PR link and the drill screenshot to the U2 L16 assignment on Google Classroom.

**Early finishers:** start Chart 3 now (checklist above), or add the fourth "audience choice" chart from U2 L14.

---

## WHY THIS MATTERS (the bigger picture)

**The project is an argument, not an art show.** Every chart is a premise; the analysis paragraphs are the reasoning; the audit script and the drill are the evidence that the premises are sound. A checker that never fails is not a checker — the drill is what turns "I cleaned the data" into "I can prove this data is sound, and here is what my code would catch if it were not."

**U2 L17 (tomorrow) is peer review:** You will read a partner's full project and they will read yours. The review form asks: *Does the evidence support the claim? Is the audit auditable? Are the charts honest for the stated audience?* If your work today cannot answer "yes" to those, tomorrow's review will expose it.

**Next:** U2 L17 — Reflection: Peer Review Of Visualizations  \
[U2-L17-Reflection-Peer-Review-Of-Visualizations.md](U2-L17-Reflection-Peer-Review-Of-Visualizations.md)
