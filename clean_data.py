"""clean_data.py — YOU build this (Unit 2 L11).

Read data/u2_student_performance_data.csv with csv.DictReader, then:

  1. Convert the numeric columns with the to_float pattern
     ("Math Score" is the string "53", not the number 53).
  2. Drop rows with blanks in the columns you chose to drop on.
  3. Drop rows with impossible values (SANITY bounds: Age 10-22,
     Math/Science/English Score 0-100, GPA 0-4.0, hours 0-24).
  4. Write the survivors to data/u2_student_performance_clean.csv
     with csv.writer, keeping the original header row.
  5. Print rows in, rows out, rows dropped — plus a count per reason.
     They must add up. If they do not, your cleaning has a bug.

Naming matters: the output file is data/u2_student_performance_clean.csv
(with the u2_ prefix), not clean_student_performance.csv.

Separately: the project's audit script is clean_threats.py — different
file, different dataset (data/u2_campus_threat_daily.csv). Threat code
does not belong in this file.
"""
# TODO: your cleaning code here
