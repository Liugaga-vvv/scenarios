def count_long_words(text, length):
    words = text.split()
    count = 0
    for word in words:
        word = word.strip(".,;:!?")
        if len(word) > length:
            count += 1
    return count
