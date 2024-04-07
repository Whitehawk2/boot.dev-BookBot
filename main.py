#!/bin/env python3
"""
Building a Book bot, according to guided project from
boot.dev, found here:
https://www.boot.dev/learn/build-bookbot

To use: Clone, create a "books" subfolder, and place
a book / text file there, in "txt" format; then execute `main.py`

Do whatever you please with this license, 2024 Alon R.

Written proudly Copilot free :)
"""


def read_book(book_name: str = "frankenstein") -> str:
    """Reads a book from the books directory and returns it as a string."""

    with open(f"books/{book_name}.txt", "r", encoding="utf-8") as f:
        return f.read()


def count_words(book: str) -> int:
    """Counts the number of words in a book."""

    return len(book.split())


def count_letters(book: str) -> dict:
    """Counts the number of letters in a book."""
    letters = {}
    for letter in book:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters


def print_report(bookname: str, wordcount: int, letter_segmentation: list[dict]) -> int:
    """Pretty prints a report based on instructions format"""
    print(f"--- Begin report of {bookname} ---")
    print(f"{wordcount} words have been found in {bookname}.")
    for letter in letter_segmentation:
        print(f'the "{letter["char"]}" was found {letter["count"]} times')
    print("--- End report --- ")

    return 0


def main():  # noqa: missing-function-docstring
    try:
        book = read_book("frankenstein")
        word_count = count_words(book)
        char_count = count_letters(book)

        # this is not easy to read but I like list comprehensions too much :(
        sorted_dict = sorted(
            [{"char": x[0], "count": x[1]} for x in char_count.items()],
            key=lambda x: x["count"],
            reverse=True,
        )
        # print(sorted_dict)
        print_report(book, word_count, sorted_dict)

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
