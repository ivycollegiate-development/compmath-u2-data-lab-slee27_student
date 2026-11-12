# U2 L16 — Project Lab: Prove the Audit, Finish the Charts

**LO:** prove your audit catches defects with a drill run, then finish Chart 2 and Chart 3 with analysis for your audience — a complete chart set ready for tomorrow's peer review.

**One objective for today:** by the bell, `project_charts.py` produces all three PNGs and `analysis.md` has a paragraph for each.

**Estimated time:** 50 minutes (one period). Re-timed from ~100. Today is the drill plus the two remaining charts — nothing else. Chart 1 was L15, peer review is L17.

---

Work in **your own data-lab repo**. Every command below assumes you are already in it.

## PART 0 — PULL, RE-RUN, DRILL (10 min)

```bash
cd ~/compmath-u2-data-lab
git pull
python3 clean_threats.py
```

You should see six `[PASS]` lines, `Rows out: 60`, `Rows dropped: 0`, `All checks passed`. If not, fix the script before you touch a chart — you cannot chart a file your checker does not accept.

Now prove the checker actually checks:

```bash
python3 clean_threats.py --drill
```

Expected:

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

Three rows, three different checks firing, three different reasons. That is what an audit looks like when it finds something.

**Screenshot this terminal.** It is the evidence that your checker works, and it is what I grade for rubric item D.

If your drill prints `DRILL FAILED`, one of your checks is missing. Find which of the three broken rows survived and fix that check before you build anything.

Also confirm Chart 1 still regenerates (`python3 project_charts.py` should already write `chart1_timeline.png`).

---

## PART 1 — CHART 2: WEEKDAY VS WEEKEND (16 min)

**The claim you are testing:** attacks follow the school week.

Add this block to `project_charts.py`, after Chart 1:

```python
from datetime import datetime

def is_weekend(d):
    return datetime.strptime(d, "%Y-%m-%d").weekday() >= 5   # 5 = Sat, 6 = Sun

wd, we = [], []
for row in rows:
    (we if is_weekend(row["date"]) else wd).append(int(row["phishing_reports"]))

avg_wd, avg_we = sum(wd) / len(wd), sum(we) / len(we)
print(f"weekday {avg_wd:.2f} ({len(wd)} days) | weekend {avg_we:.2f} ({len(we)} days)")

plt.figure(figsize=(6, 4))
plt.bar(["Weekday", "Weekend"], [avg_wd, avg_we])
plt.text(0, avg_wd, f"{avg_wd:.2f}", ha="center", va="bottom")
plt.text(1, avg_we, f"{avg_we:.2f}", ha="center", va="bottom")
plt.title("<your finding, for your audience>")
plt.xlabel("Day type")
plt.ylabel("Average phishing reports")
plt.ylim(bottom=0)
plt.tight_layout()
plt.savefig("chart2_weekday_weekend.png")
plt.clf()
```

**Graded:** title states the finding, not the subject; y-axis starts at 0; both averages printed on the chart; `savefig` before any `show`; `plt.clf()` after.

**Check your arithmetic against the data:** weekday **7.98** over 44 days, weekend **2.88** over 16 days. Anything else is a bug in your grouping, not a discovery.

**Then write the Chart 2 paragraph in `analysis.md`:** what the chart shows for your named audience, the one number they should notice, and one honest limitation (44 weekday days against 16 weekend days, so the weekend average is the shakier one).

---

## PART 2 — CHART 3: LOGIN SUCCESS RATE (16 min)

Same pattern, different question: what shape does a rate have?

```python
rates = [float(row["login_success_rate"]) for row in rows]

plt.figure(figsize=(7, 4))
plt.hist(rates, bins=15, edgecolor="white")
plt.title("<your finding, for your audience>")
plt.xlabel("Login success rate")
plt.ylabel("Number of days")
plt.tight_layout()
plt.savefig("chart3_success_rate.png")
plt.clf()
```

Choose `bins=15` on purpose — 60 days into 15 bins, four days per bin, not the default ten.

**The honest finding is not "most days near 100%."** In this file the median day sits at **0.56**, only 4 of 60 days are above 0.90, and 2026-10-24 collapses to **0.0**. A title like *"Most Days Sit Between 45% and 72% Login Success — One Day Collapses to 0%"* is defensible. A title claiming near-total success is false and I will mark it wrong: the chart does not say that.

**Then write the Chart 3 paragraph**, including the limitation that a single outlier day drives the left tail, and what you would need to know before concluding anything about that day.

---

## PART 3 — PARTNER GLANCE (4 min)

Your partner looks at **Chart 3 only** and answers without your explanation: what does it say, and who is it for?

One specific compliment, one specific suggestion. Fix it before you commit.

---

## PART 4 — PUSH (4 min)

```bash
git add clean_threats.py project_charts.py analysis.md chart2_weekday_weekend.png chart3_success_rate.png
git commit -m "project: drill proven, chart2 weekday vs weekend, chart3 success rate"
git push
```

Password prompt = Personal Access Token, not your GitHub password.

---

## TURN IN

1. Screenshot of the `--drill` run — 3 `DROP` lines with 3 different reasons, then `DRILL PASSED`.
2. `chart2_weekday_weekend.png` and `chart3_success_rate.png` pushed, each with its paragraph in `analysis.md`.
3. Your pull request link.

Submit all three to the U2 L16 assignment on Google Classroom.

---

## WHY THIS MATTERS

A checker that never fails is not a checker. The drill turns "I cleaned the data" into "I can prove this file is sound, and here is what my code would catch if it were not." The two charts turn the audit into an argument.

**Tomorrow (U2 L17) your partner reviews all three charts** for clarity, honesty, and impact, and you revise one from their feedback. If a chart does not exist by tonight, there is nothing to review.

**Next:** U2 L17 — Reflection: Peer Review Of Visualizations  \
[U2-L17-Reflection-Peer-Review-Of-Visualizations.md](U2-L17-Reflection-Peer-Review-Of-Visualizations.md)
