def bad_fibonacci(n: int) -> int:
    """Return the nth fibonacci number."""
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)


def good_fibonacci(n: int) -> tuple:
    """Return pair of Fibonacci numbers, F(n) and F(n-1)."""
    if n <= 1:
        return n, 0
    else:
        a, b = good_fibonacci(n-1)
        return a+b, a
