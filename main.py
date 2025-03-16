from stats import count_words


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()


def main():
    filepath: str = "./books/frankenstein.txt"
    document: str = get_book_text(filepath)
    num_words: int = count_words(document)
    print(f"{num_words} words found in the document")


if __name__ == "__main__":
    main()
