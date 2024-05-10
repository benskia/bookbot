def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_string_words(file_contents))
        print(count_letter_occurrences(file_contents))

def count_string_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_letter_occurrences(text: str) -> dict:
    letter_occurrences = {}
    for ch in text:
        letter = ch.lower()
        if letter not in letter_occurrences:
            letter_occurrences[letter] = 1
            continue
        letter_occurrences[letter] += 1
    return letter_occurrences

if __name__ == "__main__":
    main()
