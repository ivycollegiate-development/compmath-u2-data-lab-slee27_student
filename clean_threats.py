import csv
import io
import sys
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

FIELDS = [
    "date", "phishing_reports", "failed_logins",
    "phishing_clicks", "login_success_rate"
]
START = date(2026, 10, 5)
END = date(2026, 12, 3)
DRILL = "--drill" in sys.argv

if DRILL:
    print("DRILL MODE -- 3 broken rows injected in memory; nothing will be written")
    source = """# Drill test data
date,phishing_reports,failed_logins,phishing_clicks,login_success_rate
2026-10-05,12,33,5,0.4
2026-10-06,11,26,4,0.53
2026-10-07,4,25,3,0.55
2026-10-08,,24,0,0.56
2026-10-09,0,25,0,1.4
2026-10-1X,0,9,0,0.49
"""
else:
    source = Path("data/u2_campus_threat_daily.csv").read_text(
        encoding="utf-8-sig"
    )

lines = source.splitlines()
comments = sum(line.lstrip().startswith("#") for line in lines)
reader = csv.DictReader(io.StringIO("\n".join(
    line for line in lines
    if line.strip() and not line.lstrip().startswith("#")
)))

if reader.fieldnames != FIELDS:
    print("[FAIL] header must be:", ",".join(FIELDS))
    sys.exit(1)

rows = list(reader)
print(f"Rows in: {len(rows)}")
kept = []
dates = []
seen = set()
drops = Counter({
    "blank": 0, "unparseable": 0,
    "impossible": 0, "bad date": 0
})

for row in rows:
    day = row.get("date", "")
    reason = None
    detail = ""

    if None in row:
        reason, detail = "unparseable", "extra CSV cells"
    elif any(row.get(key) in ("", None) for key in FIELDS):
        reason = "blank"
        key = next(key for key in FIELDS if row.get(key) in ("", None))
        detail = f"blank {key}"
    else:
        try:
            parsed = date.fromisoformat(day)
            if parsed.isoformat() != day or not START <= parsed <= END:
                raise ValueError
        except ValueError:
            reason = "bad date"
            detail = f"bad date {day!r} (not YYYY-MM-DD or outside term)"

        if reason is None:
            try:
                counts = [int(row[key]) for key in FIELDS[1:4]]
                rate = float(row["login_success_rate"])
            except ValueError:
                reason, detail = "unparseable", "non-numeric value"
            else:
                if any(value < 0 for value in counts):
                    reason, detail = "impossible", "negative count"
                elif not 0.0 <= rate <= 1.0:
                    reason = "impossible"
                    detail = (
                        f"impossible login_success_rate="
                        f"{row['login_success_rate']!r} (allowed 0.0..1.0)"
                    )
                elif parsed in seen:
                    reason, detail = "bad date", f"duplicate date {day}"

    if reason:
        drops[reason] += 1
        print(f"  DROP {day}: {detail}")
    else:
        kept.append(row)
        dates.append(parsed)
        seen.add(parsed)

ordered = sorted(dates)
expected_start = START
expected_end = START + timedelta(days=2) if DRILL else END
expected_dates = [
    expected_start + timedelta(days=n)
    for n in range((expected_end - expected_start).days + 1)
]
dates_ok = ordered == expected_dates
expected_rows = 6 if DRILL else 60

checks = [
    (True, f"source comment lines -- {comments} '#' line(s) ignored"),
    (True, "header matches the five expected columns"),
    (len(rows) == expected_rows, f"row count -- {len(rows)} rows read"),
    (
        drops["blank"] == (1 if DRILL else 0),
        f"no blank cells -- {drops['blank']} blank"
    ),
    (
        drops["unparseable"] == 0
        and drops["impossible"] == (1 if DRILL else 0),
        "counts and rates in bounds -- "
        f"unparseable {drops['unparseable']}, impossible {drops['impossible']}"
    ),
    (dates_ok, "dates unique, contiguous, inside the term window"),
]

print("Checks:")
for passed, label in checks:
    print(f"  [{'PASS' if passed else 'FAIL'}] {label}")

dropped = sum(drops.values())
print(f"Rows out: {len(kept)}")
print(f"Rows dropped: {dropped}  {dict(drops)}")
print(f"Reconciliation: {len(kept)} kept + {dropped} dropped = {len(rows)} in")

passed = all(ok for ok, label in checks)
if DRILL:
    passed = passed and len(kept) == 3 and dict(drops) == {
        "blank": 1, "unparseable": 0, "impossible": 1, "bad date": 1
    }
    print(
        "DRILL PASSED: 3 dropped, 3 kept, nothing written"
        if passed else "DRILL FAILED"
    )
elif passed:
    output = Path("data/u2_campus_threat_daily_clean.csv")
    with output.open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(sorted(kept, key=lambda row: row["date"]))
    print("All checks passed")
    print(f"Saved: {output}")
else:
    print("Audit failed; nothing written")

sys.exit(0 if passed else 1)
