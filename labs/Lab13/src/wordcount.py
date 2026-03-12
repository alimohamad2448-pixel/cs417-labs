"""Word counter using argparse."""
import argparse
from collections import Counter


def build_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "filename",
        help="text file to analyze"
    )

    parser.add_argument(
        "--ignore-case", "-i",
        action="store_true",
        default=False
    )

    parser.add_argument(
        "--top", "-t",
        type=int,
        default=None
    )

    parser.add_argument(
        "--min-length", "-m",
        type=int,
        default=1
    )

    parser.add_argument(
        "--sort-by", "-s",
        choices=["freq", "alpha"],
        default="freq"
    )

    parser.add_argument(
        "--reverse", "-r",
        action="store_true",
        default=False
    )

    return parser    
    
    """Create and return the argument parser.

    Arguments to define:
        filename    - positional, the text file to analyze
        --ignore-case / -i  - store_true, lowercase all words
        --top / -t          - int, show top N most frequent words (default: None)
        --min-length / -m   - int, only count words with at least this many chars (default: 1)
        --sort-by / -s      - choices ["freq", "alpha"], how to sort top words (default: "freq")
        --reverse / -r      - store_true, reverse the sort order

    Returns:
        argparse.ArgumentParser
    """
    # TODO: Create an ArgumentParser with a description
    # TODO: Add the positional 'filename' argument
    # TODO: Add --ignore-case / -i (action="store_true")
    # TODO: Add --top / -t (type=int, default=None)
    # TODO: Add --min-length / -m (type=int, default=1)
    # TODO: Add --sort-by / -s (choices=["freq", "alpha"], default="freq")
    # TODO: Add --reverse / -r (action="store_true")
    pass


def analyze(filepath, ignore_case=False, top=None, min_length=1, sort_by="freq", reverse=False):
    with open(filepath, "r") as infile:
        text = infile.read()

    words = text.split()

    if ignore_case:
        words = [word.lower() for word in words]

    words = [word for word in words if len(word) >= min_length]

    count = len(words)

    if top is None:
        return f"{filepath}: {count} words"

    counts = Counter(words)

    if sort_by == "freq":
        items = counts.items()
        sorted_items = sorted(items, key=lambda item: (-item[1], item[0]))
        if reverse:
            sorted_items = list(reversed(sorted_items))
    else:
        sorted_items = sorted(counts.items(), key=lambda item: item[0])
        if reverse:
            sorted_items = list(reversed(sorted_items))

    top_words = sorted_items[:top]

    lines = [f"{filepath}: {count} words", "", f"Top {top} words:"]
    for word, word_count in top_words:
        lines.append(f"  {word}: {word_count}")

    return "\n".join(lines)

    """Analyze a text file and return a formatted result string.

    Args:
        filepath: path to the text file
        ignore_case: if True, lowercase all words before counting
        top: if set, show the N most frequent words with counts
        min_length: only count words with at least this many characters
        sort_by: "freq" (by count) or "alpha" (alphabetical) when showing top words
        reverse: if True, reverse the sort order

    Returns:
        str: formatted result

    Raises:
        FileNotFoundError: if the file doesn't exist
    """
    # TODO: Read the file and split into words on whitespace
    # TODO: If ignore_case, lowercase all words
    # TODO: Filter out words shorter than min_length
    # TODO: Count total words
    # TODO: If top is None, return "<filename>: <count> words"
    # TODO: If top is set, find the most frequent words:
    #   - Use Counter(words).most_common() for frequency data
    #   - If sort_by == "alpha", sort alphabetically instead
    #   - If reverse, flip the order
    #   - Take the first 'top' entries
    #   - Return multi-line string:
    #       "<filename>: <count> words\n\nTop <N> words:\n  <word>: <count>\n  ..."
    pass


def main():
    parser = build_parser()
    args = parser.parse_args()

    result = analyze(
        args.filename,
        ignore_case=args.ignore_case,
        top=args.top,
        min_length=args.min_length,
        sort_by=args.sort_by,
        reverse=args.reverse
    )

    print(result)


if __name__ == "__main__":
    main()
    """Build parser, parse args, analyze, print result."""
    # TODO: Build the parser
    # TODO: Parse args
    # TODO: Call analyze with the parsed arguments
    # TODO: Print the result
    pass
