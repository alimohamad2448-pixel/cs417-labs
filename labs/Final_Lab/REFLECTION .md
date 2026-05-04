In Part 0, the three things I wrote down as hard to change were the file format handling, the category rules, and the totaling logic mixed in with printing. I was mostly right. The starter code had CSV parsing directly inside `main()`, so adding JSON support would have required changing the same loop instead of plugging in a new parser. The categories were also hard-coded in the script, which meant changing category rules required editing code instead of editing data. Finally, the calculation logic was mixed together with file reading and printing, so it was hard to test the real logic by itself. What surprised me was that the hardest part was not writing a lot of new code. The harder part was reshaping the code so each function had one job.

For Part 1, the main design idea was strategy/pluggable parts. I created `parse_csv(text)` and `parse_json(text)` so the program can support more than one input format while keeping the rest of the base the same.

For Part 2, the main design idea was dependency injection. The function `categorize(vendor, categories)` does not depend on a hard-coded dictionary anymore. Instead, it uses the `categories` config passed into it, which made it possible to test with other category mappings.

For Part 3, the main design idea was separation of I/O from logic. The function `build_report(rows, categories)` only computes totals and returns a dictionary. It does not open files or print. That leaves `main()` responsible for I/O and keeps the business logic testable on its own


Part 3 was the hardest. My first thought was that I only needed to move the totals loop into `build_report()`, but that was not enough because `main()` was still using the old row format.

If I had to pull transactions from a remote API next week, I would add that in `main()` since that is I/O. Then I would pass the returned text into the right parser. If the API response matched the current JSON structure, I could probably reuse `parse_json()` directly. 