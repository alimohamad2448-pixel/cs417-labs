"""
JSON Structure Validator – Lab 7

Validates the structural nesting of a JSON string using a Stack.
Reports the location (line, column) of any errors found.
"""

from stack import Stack
from datetime import datetime

# Maps each closing character to its expected opening character.
MATCHING = {
    "}": "{",
    "]": "[",
}


def validate(json_string):
    """
    Validate the structural nesting of a JSON string.

    Checks that every { has a matching }, every [ has a matching ],
    and that quoted strings are properly closed.

    Returns:
        (is_valid, errors)
    """

    stack = Stack()
    errors = []

    line = 1
    col = 0
    in_string = False
    escape = False

    for char in json_string:
        col += 1

        if char == "\n":
            line += 1
            col = 0
            continue

        # Handle string logic
        if in_string:
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == '"':
                in_string = False
            continue

        else:
            if char == '"':
                in_string = True
                continue

        # Handle opening brackets
        if char in "{[":
            stack.push((char, line, col))

        # Handle closing brackets
        elif char in "}]":
            if stack.is_empty():
                errors.append(
                    f"Unexpected '{char}' at line {line}, column {col}"
                )
            else:
                opening, o_line, o_col = stack.pop()
                if opening != MATCHING[char]:
                    errors.append(
                        f"Mismatched '{char}' at line {line}, column {col}"
                    )

    # Unclosed string
    if in_string:
        errors.append("Unterminated string literal")

    # Unclosed brackets
    while not stack.is_empty():
        opening, o_line, o_col = stack.pop()
        errors.append(
            f"Unclosed '{opening}' at line {o_line}, column {o_col}"
        )

    return (len(errors) == 0, errors)


def validate_file(filepath):
    """
    Validate a JSON file by reading it and calling validate().
    """

    with open(filepath, "r") as f:
        content = f.read()

    return validate(content)


# ---- Main ----
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python json_validator.py <filepath>")
        sys.exit(1)

    filepath = sys.argv[1]
    is_valid, errors = validate_file(filepath)

    if is_valid:
        print(f"{filepath}: Valid JSON structure")
    else:
        for error in errors:
            print(error)