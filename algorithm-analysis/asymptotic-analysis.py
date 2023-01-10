def find_max(data: list) -> int:
    """Return the maximum element from a nonempty python list"""
    biggest = data[0]
    for val in data:
        if val > biggest:
            biggest = val
    return biggest

# This function runs in linear time O(n), as it will always travers the
# entire length of the input list.
