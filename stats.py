def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()


def count_words(document: str) -> int:
    lines = document.split("\n")
    words = [word for line in lines for word in line.split()]
    return len(words)
