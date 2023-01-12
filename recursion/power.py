def power(x: int, n: int) -> int:
    """Compute the value of x**n for integere n."""
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


def fast_power(x: int, n: int) -> int:
    """Compute the value for x**n for integer n."""
    if n == 0:
        return 1
    else:
        partial = power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:  # if n odd, include extra factor of x
            result *= x
        return result
