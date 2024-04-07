#!/bin/env python3


def read_book(book_name: str = "frankenstein"):
    """Reads a book from the books directory and returns it as a string."""

    with open(f"books/{book_name}.txt", "r") as f:
        return f.read()


def count_words(book: str) -> int:
    """Counts the number of words in a book."""

    return len(book.split())


def main():  # noqa: missing-function-docstring
    try:
        book = read_book("frankenstein")
        print(f"words in the book: {count_words(book)}")
        # print(book)
        return 0

    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return 1

    except IOError as e:
        print(f"An error occurred: {e}")
        return 1

    except Exception as e:  # noqa: broad-exception-caught
        print(f"An error occurred: {e}")
        return 1


if __name__ == "__main__":
    main()
