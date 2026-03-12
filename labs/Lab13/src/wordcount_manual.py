"""Word counter using manual sys.argv parsing."""
import sys


def parse_args_manual(argv):
    if len(argv) < 2:
        print("Usage: wordcount_manual.py <filename>", file=sys.stderr)
        sys.exit(1)

    return argv[1]

    """Extract filename from argv list.

    If no filename provided, print usage to stderr and exit with code 1.

    Args:
        argv: sys.argv (list of strings)

    Returns:
        str: the filename
    """
    # TODO: Check if argv has at least 2 elements (program name + filename)
    # If not, print "Usage: wordcount_manual.py <filename>" to stderr and exit(1)
    # Otherwise return argv[1]
    pass


def count_words(filepath):
    with open(filepath, "r") as infile:
        text = infile.read()

    words = text.split()
    return len(words)
    """Read a file and return the number of words.

    Words are defined by splitting on whitespace.

    Args:
        filepath: path to the text file

    Returns:
        int: total word count

    Raises:
        FileNotFoundError: prints error to stderr and exits with code 1
    """
    # TODO: Try to open and read the file
    # If FileNotFoundError, print "Error: file '<filepath>' not found" to stderr and exit(1)
    # Otherwise split on whitespace and return the count
    pass


def main():
    filename = parse_args_manual(sys.argv)

    try:
        count = count_words(filename)
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found", file=sys.stderr)
        sys.exit(1)

    print(f"{filename}: {count} words")

    """Wire it together: parse args, count words, print result."""
    # TODO: Call parse_args_manual with sys.argv
    # Call count_words with the filename
    # Print "<filename>: <count> words"
    pass


if __name__ == "__main__":
    main()