def insertion_sort(A):
    """Sort list of comparable elements into nondecreasing order."""
    for k in range(1, len(A)):
        cur = A[k]
        j = k
        while j > 0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur


if __name__ == "__main__":
    example_list = [1, 3, 10, 2, 5, 6, 9]
    insertion_sort(example_list)
