def count_duplicates(s: str) -> int:
    counts = {}
    for char in s:
        if char not in counts:
            counts[char] = 0
        counts[char] += 1
    count = 0
    for char in counts:
        if counts[char] > 1:
            count += 1
    return count
