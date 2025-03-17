from sys import argv, exit
from stats import count_words, inventory_chars, organize_inventory


def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    filepath: str = argv[1]
    document: str = get_book_text(filepath)
    num_words: int = count_words(document)
    char_inventory: list[dict] = organize_inventory(inventory_chars(document))
    print_report(filepath, num_words, char_inventory)


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()


def print_report(
        filepath: str, num_words: int, char_inventory: list[dict]) -> None:
    fmt(" BOOKBOT ", "=")
    print(f"Analyzing book found at {filepath}...")

    fmt(" Word Count ", "-")
    print(f"Found {num_words} total words")

    fmt(" Character Count ", "-")
    for c in char_inventory:
        if not c['character'].isalpha():
            continue
        print(f"{c['character']}: {c['count']}")
    fmt(" END ", "=")


def fmt(header: str, fillchar: str) -> str:
    print('{s:{c}^{n}}'.format(s=header, n=79, c=fillchar))


if __name__ == "__main__":
    main()
