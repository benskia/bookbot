from stats import count_words, inventory_chars


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()


def main():
    filepath: str = "./books/frankenstein.txt"
    document: str = get_book_text(filepath)

    num_words: int = count_words(document)
    print(f"{num_words} words found in the document")

    char_inventory: dict[str:int] = inventory_chars(document)
    for ch, num in char_inventory.items():
        print(f"'{ch}': {num}")


if __name__ == "__main__":
    main()
