"""Expense Report — starter code.

This script works. It reads transactions.csv, categorizes the rows,
and prints a report showing per-category totals.

It also has all of its logic crammed into one big main() function with
hard-coded filenames, a hard-coded category dict, and print() statements
woven into the calculations.

Your job is to refactor this code IN PLACE, by moving the right logic
into the four helper shapes below, in response to the change requests in
the README. Keep everything in this one file.

When you're done, the script should produce the SAME output (TOTAL = $613.87)
on the original inputs — the change requests should not change observable
behavior on the starting CSV.

DO NOT add any external libraries. Standard library only.
"""

import json
from pathlib import Path


# -----------------------------------------------------------------------------
# TODO Part 1 — fill these in. (See README "Part 1 — Add JSON support".)
# -----------------------------------------------------------------------------

def parse_csv(text: str) -> list[dict]:

    """Return a list of row dicts: {"date", "vendor", "amount", "note"}.

    Skip lines that don't have 4 comma-separated fields.

    """

    rows = []

    lines = text.splitlines()

    if len(lines) == 0:

        return rows

    for line in lines[1:]:

        parts = line.strip().split(",")

        if len(parts) != 4:

            continue

        row = {

            "date": parts[0].strip(),

            "vendor": parts[1].strip(),

            "amount": float(parts[2].strip()),

            "note": parts[3].strip(),

        }

        rows.append(row)

    return rows

def parse_json(text: str) -> list[dict]:

    """Return a list of row dicts: {"date", "vendor", "amount", "note"}.

    Input is JSON text — same fields as the CSV, just JSON-shaped.

    """

    data = json.loads(text)

    rows = []

    for item in data:

        row = {

            "date": str(item["date"]).strip(),

            "vendor": str(item["vendor"]).strip(),

            "amount": float(item["amount"]),

            "note": str(item["note"]).strip(),

        }

        rows.append(row)

    return rows

# -----------------------------------------------------------------------------
# TODO Part 2 — fill this in. (See README "Part 2 — Configurable categories".)
# -----------------------------------------------------------------------------

def categorize(vendor: str, categories: dict) -> str:
    """Return the category for `vendor` based on `categories`.

    `categories` maps {category_name: [keyword, keyword, ...]}.
    A vendor matches a category if any of the keywords appears in the
    vendor name (case-insensitive). Return "other" if no category matches.
    """
    vendor_upper = vendor.upper()

    for category_name in categories:
        keywords = categories[category_name]

        for keyword in keywords:
            if keyword.upper() in vendor_upper:
                return category_name

    return "other"


# -----------------------------------------------------------------------------
# TODO Part 3 — fill this in. (See README "Part 3 — A pure pipeline".)
# -----------------------------------------------------------------------------

def build_report(rows: list[dict], categories: dict) -> dict:
    """Return {category_name: total_amount} for a list of parsed rows.

    Pure: must NOT open files, read stdin, or print anything.
    """
    totals = {}

    for row in rows:
        vendor = row["vendor"]
        amount = float(row["amount"])
        category_name = categorize(vendor, categories)

        if category_name not in totals:
            totals[category_name] = 0.0

        totals[category_name] = totals[category_name] + amount

    return totals


# -----------------------------------------------------------------------------
# main() — I/O lives here. Once Parts 1-3 are done, this should shrink to
# just the I/O glue: read files, call parse_*, call build_report, print.
# Right now it has everything inline.
# -----------------------------------------------------------------------------

def main():
    data_path = Path(__file__).resolve().parent.parent / "data" / "transactions.csv"
    text = data_path.read_text()
    rows = parse_csv(text)  

    categories_path = Path(__file__).resolve().parent.parent / "data" / "categories.json"
    categories = json.loads(categories_path.read_text())

    totals = build_report(rows, categories)

    print("=== Expense Report ===")
    for cat, total in sorted(totals.items()):
        print(f"  {cat:<15} ${total:>8.2f}")
    print(f"  {'TOTAL':<15} ${sum(totals.values()):>8.2f}")


if __name__ == "__main__":
    main()