def linear_sum(S: list, n: int) -> int:
    """Return the sum of the first n numbers of sequence S."""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]


if __name__ == "__main__":
    l = [4, 3, 6, 2, 8, 9, 3, 2, 8, 5, 1, 7, 2, 8, 3, 7]
    print(linear_sum(l, 7))
