import re

def split_sentence(sentence: str):
    result = re.findall(r'\b[a-zA-Z]+\b', sentence.lower())
    result = list(set(result))
    return result

