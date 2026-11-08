# U2 L18 — Project Final Push: Polish and Submit

**LO:** finish the Unit 2 project to a submittable standard — three correct charts, honest analysis, clean code — and submit it.

**Estimated time:** 50 minutes (one period). Re-timed so the final submission is genuinely complete, not just "done enough."

---

Today is the last working day on the project. You are not building anything new. You are taking what you have and making it **correct, complete, and honest** — then submitting it.

---

## PART 0 — OPEN YOUR REPO AND AUDIT YOURSELF (15 min)

```bash
pwd
cd ~/compmath-u2-data-lab
git pull
ls
python3 project_charts.py
```

Now grade yourself honestly against the rubric. **Tick a box only if it is true, not if it is nearly true.**

### Data integrity

- ☐ `project_charts.py` runs start to finish with **no error output**
- ☐ It prints `Rows in` and `Rows out`, and one PASS/FAIL line per check with its count
- ☐ I can show the `--drill` run: 3 dropped rows, 3 different reasons (blank, impossible, bad date) — proof my checker catches defects, not just that my data looks fine
- ☐ The dates parse into chronological order (the timeline is not scrambled)

### The three required charts

- ☐ `chart1_timeline.png` exists, has a title, and both axis labels
- ☐ `chart2_weekday_weekend.png` exists, has a title, and both axis labels
- ☐ `chart3_success_rate.png` exists, has a title, and both axis labels
- ☐ I chose the histogram's bin count **on purpose** and can say why
- ☐ Every chart's code has a one-line comment saying what it shows

### Analysis (`analysis.md`)

- ☐ One paragraph per chart — three paragraphs total
- ☐ Each paragraph names the audience and the one thing they should notice
- ☐ Each paragraph contains **one honest limitation**
- ☐ I did not claim anything the chart does not actually show

### The honesty audit — do this last, and do it seriously.

Look at each of your three charts and ask:

1. **Does my y-axis start at zero?** If not, do I **say why** somewhere in `analysis.md`?
2. **Did my audit exclude any row that would have made my story less dramatic?** If it did, was excluding it correct — and did I say so?
3. **Is there anything in my data I chose not to plot?** A careful reader would notice. Say so yourself, before they ask.

**An honest limitation is not a weakness in your write-up. It is the sentence that tells your reader you understood your own data.**

**Write your answers to the three honesty questions in your notes.** If any answer is "no," that is your fix list for Part 1.

---

## PART 1 — FIX WHAT IS ACTUALLY WRONG (25 min)

Work in this order. **Do not skip to polish while something is still broken.**

1. **Does it run?** No error, no blank PNG, no missing chart. Fix this before anything else — a chart that does not exist cannot be polished.
2. **Are the numbers true?** Re-read your audit code (`clean_threats.py`). A row your checker rejected must be genuinely broken — not merely a value your parser refused to understand. If the real run dropped a row on a good value, the bug is in your code, not the data.
3. **Do the labels tell the truth?** A y-axis label that says "attacks" when the column is `failed_logins` is a lie in a chart title. Rename the label.
4. **Now** polish: colors, `plt.tight_layout()`, readable font sizes, legend placement.

**If a chart is missing**, say so in `analysis.md` and explain what you tried. A **documented gap is honest work. A silent gap is a lie.**

---

## PART 2 — FINAL SUBMISSION (10 min)

Push your finished work:

```bash
cd ~/compmath-u2-data-lab
git add project_charts.py analysis.md
git add chart1_timeline.png chart2_weekday_weekend.png chart3_success_rate.png
git commit -m "final: three visualizations with analysis"
git push
```

Then open or update your Pull Request on github.com (Contribute → Open pull request). If you already opened one on U2 L16, **update it** — do not open a second one.

**Before you submit, verify on github.com that all of this is actually visible:**

- ☐ `project_charts.py` opens and is the version you just pushed
- ☐ All three PNGs are visible in the repo, and each one renders
- ☐ `analysis.md` shows all three paragraphs
- ☐ The Pull Request page shows your latest commit

---

## TURN IN — PULL REQUEST LINK (due 23:59 tonight)

One submission showing, in order:
1. Your completed self-audit checklist, with the honesty audit answered in writing
2. Your final `git push` confirmation
3. Your updated Pull Request page on github.com, with the latest commit visible

Submit the PR link to the U2 L18 assignment on Google Classroom.

**Keep the terminal open** — spot-checks happen.

**(Password prompt = Personal Access Token, not your GitHub password.)**

---

## WHY THIS MATTERS (the bigger picture)

**The project is an argument, and the submission is the evidence.** The self-audit is you checking your own work *before* I do. If you catch it, it's a fix. If I catch it, it's a deduction.

**The honesty audit is the most important part of this course.** In the real world, no one checks your charts line by line — they trust you. The only reason they can trust you is that you've internalized the habit of asking: *What did I leave out? What did I drop? What would change the reader's conclusion?* That habit is what this unit was for.

**U2 L19 (after Fall Break, second day back)** is the Unit 2 Assessment + Reflection: paper test first (35 min), then synthesis reflection. The assessment covers everything we built and debugged in Unit 2. Your paper checks (L06, L12), today's self-audit, and your drill run are your study guides.

**Next:** U2 L19 — Reflection: Unit 2 Wrap — What Makes A Secure Visualization  
[U2-L19-Reflection-Unit-2-Wrap-What-Makes-A-Secure-Visualization.md](U2-L19-Reflection-Unit-2-Wrap-What-Makes-A-Secure-Visualization.md)