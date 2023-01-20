def reverse(S, start, stop):
    """Reverse elements in implicit slice S[start:stop]"""
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start+1, stop-1)


if __name__ == "__main__":
    s = [4, 3, 6, 2, 8, 9, 5]
    reverse(s, 0, 6)
