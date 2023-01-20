from stack_implementation import ArrayStack


def is_matched(expr: str) -> bool:
    """Return True if all delimiters are properly matched; false otherwise."""
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()


def is_matched_html(raw: str) -> bool:
    """Return Ture if all HTML tags are properly matched; False otherwise."""
    S = ArrayStack()
    j = raw.find('<')                           # find first '<' character
    while j != -1:                              # find next '>' character
        k = raw.find('>', j+1)
        if k == -1:
            return False                        # invalid tag
        tag = raw[j+1:k]                        # strip away < >
        if not tag.startswith('/'):             # determine whether opening tag
            S.push(tag)
        else:                                   # this is a closing tag
            if S.is_empty():
                return False                    # nothing to match with
            if tag[1:] != S.pop():
                return False                    # mismatched delimiter
        j = raw.find('<', k+1)                  # find next '<' character
    return S.is_empty()                         # were all opening tags matched?


if __name__ == "__main__":
    test = "({[])}"
    print(is_matched(test))
