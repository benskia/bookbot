def main():
    FILEPATH = "books/frankenstein.txt"
    with open(FILEPATH) as f:
        file_contents = f.read()
        words = count_words(file_contents)
        character_counts = count_characters(file_contents)
        sorted_character_counts = sort_character_counts(character_counts)

        print(f"--- Begin report of {FILEPATH} ---")
        print(f"{words} words found in the document\n")

        for char_count in sorted_character_counts:
            character = char_count["character"]
            count = char_count["count"]
            print(f"The {character} character was found {count} times")

        print("--- End report ---")

def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_characters(text: str) -> dict:
    letter_occurrences = {}
    for ch in text:
        if not ch.isalpha():
            continue
        letter = ch.lower()
        if letter not in letter_occurrences:
            letter_occurrences[letter] = 1
            continue
        letter_occurrences[letter] += 1
    return letter_occurrences

def sort_character_counts(char_counts: dict) -> list:
    sorted_character_counts = []
    for char, count in char_counts.items():
        new_char_count = { "character": char, "count": count }
        sorted_character_counts.append(new_char_count)
    sorted_character_counts.sort(reverse=True, key=sort_on)
    return sorted_character_counts

def sort_on(dict: dict) -> int:
    return dict["count"]

if __name__ == "__main__":
    main()
