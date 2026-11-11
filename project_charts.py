import csv
from datetime import datetime
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

with open("data/u2_campus_threat_daily_clean.csv") as file:
    rows = list(csv.DictReader(file))

rows.sort(key=lambda row: row["date"])
dates = [datetime.strptime(row["date"], "%Y-%m-%d") for row in rows]
reports = [int(row["phishing_reports"]) for row in rows]
rates = [float(row["login_success_rate"]) for row in rows]

# Chart 1
fig, ax1 = plt.subplots(figsize=(10, 5))
ax2 = ax1.twinx()
line1 = ax1.plot(dates, reports, color="#C45A83",
                 label="Phishing reports")
line2 = ax2.plot(dates, rates, color="#377EAE",
                 label="Login success rate")
ax1.set_xlabel("Date")
ax1.set_ylabel("Phishing reports")
ax2.set_ylabel("Login success rate")
ax1.set_ylim(bottom=0)
ax2.set_ylim(0, 1)
ax2.yaxis.set_major_formatter(PercentFormatter(1))
ax1.set_title("School IT: Phishing Reports Vary; Login Success Hits 0% Once")
lines = line1 + line2
ax1.legend(lines, [line.get_label() for line in lines],
           loc="upper left")
fig.autofmt_xdate()
plt.tight_layout()
plt.savefig("chart1_timeline.png")
plt.clf()
plt.close(fig)

# Chart 2
wd, we = [], []
for row in rows:
    weekend = datetime.strptime(row["date"], "%Y-%m-%d").weekday() >= 5
    (we if weekend else wd).append(int(row["phishing_reports"]))

avg_wd = sum(wd) / len(wd)
avg_we = sum(we) / len(we)
print(f"weekday {avg_wd:.2f} ({len(wd)} days) | "
      f"weekend {avg_we:.2f} ({len(we)} days)")

plt.figure(figsize=(7, 4))
plt.bar(["Weekday", "Weekend"], [avg_wd, avg_we],
        color=["#F4B6C8", "#A9CCE8"])
plt.text(0, avg_wd, f"{avg_wd:.2f}", ha="center", va="bottom")
plt.text(1, avg_we, f"{avg_we:.2f}", ha="center", va="bottom")
plt.title("School IT: More Phishing Reports on Weekdays")
plt.xlabel("Day type")
plt.ylabel("Average phishing reports")
plt.ylim(0, max(avg_wd, avg_we) * 1.2)
plt.tight_layout()
plt.savefig("chart2_weekday_weekend.png")
plt.clf()
plt.close()

# Chart 3
plt.figure(figsize=(8, 4))
plt.hist(rates, bins=15, edgecolor="white", color="#A9CCE8")
plt.title("School IT: Median Login Success Is 56%; One Day Hits 0%")
plt.xlabel("Login success rate")
plt.ylabel("Number of days")
plt.gca().xaxis.set_major_formatter(PercentFormatter(1))
plt.tight_layout()
plt.savefig("chart3_success_rate.png")
plt.clf()
plt.close()

print("Saved all three charts.")
