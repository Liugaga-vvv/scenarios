def sub_chain(result, words):
    chains = []
    if not words:
        return
    current_word = words[0]
    for word in words[1:]:
        if word.startswith(current_word[-1]):
            chains.append(current_word)
            current_word = word
    chains.append(current_word)
    remaining_words = [word for word in words if word not in chains]
    if remaining_words:
        result.append(chains)
        sub_chain(result, remaining_words)
    else:
        result.append(chains)

def solitaire(words):
    result = []
    if not words:
        return result
    words.sort()
    sub_chain(result, words)

    return result

