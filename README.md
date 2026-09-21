## Before you start — every session

You work on the class VS Code server, in your own clone of this repo.
Your userid shows up in your repo name, your clone URL, and your filenames
via `$(whoami)`: `whoami` prints your userid, and `$(whoami)` inserts it
automatically. If the folder is missing, re-clone it — your lesson has the
exact URL, always ending in `_student.git`.

**Pull before work, every session** — it gets any changes I pushed to your
repo since last class:

```bash
cd ~/<your-clone-folder>
git config pull.rebase false
git pull
```

- `git config pull.rebase false` tells git how to combine work; run it once,
  it is not an error if you already ran it.
- If the pull prints `Already up to date.` you have everything.
- **Asked for a username/password?** GitHub username plus Personal Access
  Token (PAT) — never your GitHub password.

---

# compmath-u2-data-lab

You received your OWN copy of this repo by accepting a GitHub invitation in
your email. This is your working repo for CSV data work in Unit 2 — including
the Visualizing Threats project.

    load_data.py    starter: load a CSV with csv.DictReader
    clean_data.py   YOU write this (L11): clean the messy values
    project.py      YOU build this (project days): three charts + analysis
    data/           the Unit 2 CSV datasets (some have a # comment first line)

Run:

    python3 load_data.py
