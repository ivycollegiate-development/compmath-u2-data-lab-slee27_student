"""Self-check for the Unit 2 data lab. Run: python3 self_check.py

Five checks. Run this from the repo root, after your audit script and charts exist.
"""
import os
import re
import subprocess
import csv

results = []


def check(name, fn):
    try:
        ok, msg = fn()
    except Exception as e:
        ok, msg = False, f"error: {e}"
    results.append((name, ok, msg))
    print(("PASS  " if ok else "FAIL  ") + name + (f"  ({msg})" if msg and not ok else ""))


def audit_runs():
    if not os.path.exists("clean_threats.py"):
        return False, "clean_threats.py does not exist yet"
    p = subprocess.run(["python3", "clean_threats.py"], capture_output=True, text=True)
    out = p.stdout + p.stderr
    if p.returncode != 0:
        return False, out.strip().splitlines()[-1][:120] if out.strip() else "script failed"
    if "All checks passed" not in out:
        return False, "did not print 'All checks passed'"
    if re.search(r"\[FAIL\]", out):
        return False, "at least one check printed FAIL"
    return True, ""


def clean_file_ok():
    path = "data/u2_campus_threat_daily_clean.csv"
    if not os.path.exists(path):
        return False, "data/u2_campus_threat_daily_clean.csv does not exist yet"
    with open(path, newline="") as f:
        rows = list(csv.reader(f))
    header = ["date", "phishing_reports", "failed_logins", "phishing_clicks", "login_success_rate"]
    if not rows or rows[0] != header:
        return False, f"header is {rows[0] if rows else 'missing'}"
    if len(rows) - 1 != 60:
        return False, f"{len(rows) - 1} data rows, expected 60"
    if any(any(cell.strip() == "" for cell in r) for r in rows[1:]):
        return False, "still has blank cells"
    return True, ""


def drill_runs():
    if not os.path.exists("clean_threats.py"):
        return False, "clean_threats.py does not exist yet"
    p = subprocess.run(["python3", "clean_threats.py", "--drill"], capture_output=True, text=True)
    out = p.stdout + p.stderr
    if "DRILL PASSED" not in out:
        return False, "did not print 'DRILL PASSED'"
    drops = out.count("  DROP ")
    if drops != 3:
        return False, f"{drops} DROP lines, expected 3"
    return True, ""


def charts_ok():
    charts = ["chart1_timeline.png", "chart2_weekday_weekend.png", "chart3_success_rate.png"]
    missing = [p for p in charts if not os.path.exists(p)]
    if missing:
        return False, "missing: " + ", ".join(missing)
    small = [p for p in charts if os.path.getsize(p) < 5000]
    if small:
        return False, "suspiciously small (blank?): " + ", ".join(small)
    return True, ""


def analysis_ok():
    if not os.path.exists("analysis.md"):
        return False, "analysis.md does not exist yet"
    with open("analysis.md") as f:
        text = f.read()
    paragraphs = [p for p in re.split(r"\n\s*\n", text) if len(p.strip()) > 120]
    if len(paragraphs) < 3:
        return False, f"{len(paragraphs)} substantial paragraphs, expected at least 3"
    return True, ""


check("clean_threats.py audits the real file", audit_runs)
check("data/u2_campus_threat_daily_clean.csv is 60 rows, 5 columns, no blanks", clean_file_ok)
check("clean_threats.py --drill drops 3 rows", drill_runs)
check("all three chart PNGs exist and are not blank", charts_ok)
check("analysis.md has three paragraphs", analysis_ok)

passed = sum(1 for _, ok, _ in results if ok)
print(f"\n{passed} of {len(results)} checks passing")
