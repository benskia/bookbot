def count_words(document: str) -> int:
    lines = document.split("\n")
    words = [word for line in lines for word in line.split()]
    return len(words)


def inventory_chars(document: str) -> dict[str:int]:
    inv = {}
    for ch in document.lower():
        inv[ch] = 1 if ch not in inv else inv[ch] + 1
    return inv


def organize_inventory(char_inventory: dict[str:int]) -> list[dict]:
    oinv = [{"character": k, "count": v} for k, v in char_inventory.items()]
    oinv.sort(key=lambda x: x["count"], reverse=True)
    return oinv
