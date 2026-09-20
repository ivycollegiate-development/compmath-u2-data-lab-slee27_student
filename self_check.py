"""Self-check for the data-lab. Run: python3 self_check.py

Starts at 1 of 3 passing. Your job: make it 3 of 3, commit, push.
"""
import os, subprocess, csv, re

results = []

def check(name, fn):
    try:
        ok, msg = fn()
    except Exception as e:
        ok, msg = False, f"error: {e}"
    results.append((name, ok, msg))
    print(("PASS  " if ok else "FAIL  ") + name + (f"  ({msg})" if msg and not ok else ""))

def load_works():
    p = subprocess.run(["python3", "load_data.py"], capture_output=True, text=True)
    if p.returncode != 0:
        return False, p.stderr.strip()[-120:]
    m = re.search(r"rows loaded:\s*(\d+)", p.stdout)
    n = int(m.group(1)) if m else 0
    return (n >= 1000, f"rows loaded: {n} (expected 1000)" if n < 1000 else "")

def clean_works():
    path = "data/clean_student_performance.csv"
    if not os.path.exists(path):
        return False, "data/clean_student_performance.csv does not exist yet"
    with open(path) as f:
        rows = list(csv.reader(f))
    if len(rows) < 2:
        return False, "file has no data rows"
    if any(any(cell.strip() == "" for cell in r) for r in rows[1:]):
        return False, "still has blank cells in some rows"
    return True, ""

def project_works():
    charts = ["timeline.png", "weekday.png", "histogram.png", "analysis.md"]
    missing = [p for p in charts if not os.path.exists(p)]
    return (len(missing) == 0, "missing: " + ", ".join(missing) if missing else "")

check("load_data.py loads the full dataset", load_works)
check("clean_data.py writes a clean CSV", clean_works)
check("project.py builds 3 charts + analysis.md", project_works)

passed = sum(1 for _, ok, _ in results if ok)
print(f"\n{passed} of {len(results)} checks passing")
