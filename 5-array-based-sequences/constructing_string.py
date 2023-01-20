def constructing_string_iteration(document: str) -> str:
    temp = []
    for c in document:
        if c.isalpha():
            temp.append(c)
    letters = ''.join(temp)
    return letters


def constructing_string_comprehension(document: str) -> str:
    letters = ''.join(c for c in document if c.isalpha())
    return letters
