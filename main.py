from sys import argv, exit
from stats import count_words, inventory_chars, organize_inventory


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()


def print_report(
        filepath: str, num_words: int, char_inventory: list[dict]) -> None:
    print('{s:{c}^{n}}'.format(s=' BOOKBOT ', n=60, c='='))
    print(f"Analyzing book found at {filepath}...")

    print('{s:{c}^{n}}'.format(s=' Word Count ', n=60, c='-'))
    print(f"Found {num_words} total words")

    print('{s:{c}^{n}}'.format(s=' Character Count ', n=60, c='-'))
    for c in char_inventory:
        if not c['character'].isalpha():
            continue
        print(f"{c['character']}: {c['count']}")

    print('{s:{c}^{n}}'.format(s=' END ', n=60, c='='))


def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    filepath: str = argv[1]
    document: str = get_book_text(filepath)
    num_words: int = count_words(document)
    char_inventory: list[dict] = organize_inventory(inventory_chars(document))
    print_report(filepath, num_words, char_inventory)


if __name__ == "__main__":
    main()
