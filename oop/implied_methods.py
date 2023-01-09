class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, i):
        """Return the ith item of the vector."""
        return self._coords[i]

    def __setitem__(self, key, value):
        """Set the key coordinate of vector to given value."""
        self._coords[key] = value

    def __add__(self, other):
        """Return the sum of two vectors."""
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other  # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return f'<{str(self._coords)}>' # adapt list representation


if __name__ == "__main__":
    v = Vector(5)  # <0, 0, 0, 0, 0>
    v[1] = 23  # <0, 23, 0, 0, 0>
    v[-1] = 45  # <0, 23, 0, 0, 45>
    print(v[4])
    u = v + v  # via the __add__ method
    print(u)
    total = 0
    for entry in v:
        total += entry
    print(total)
    