from positional_list import PositionalList


class FavouritesList:
    """List of elements ordered from most frequently accessed to least."""

    class _Item:

        __slots__ = '_value', '_count'

        def __init__(self, e):
            self._value = e
            self._count = 0

    def __init__(self):
        """Create an empty list of favourites."""
        self._data = PositionalList()

    def _find_position(self, e):
        """Search for element e and return its Position."""
        walk = self._data.first
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """Move item at Position p earlier in the list based on access count."""
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:  # needs to move forward
                while (walk != self._data.first() and
                       cnt > self._data.before(walk).element._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def access(self, e):
        """Access element e, thereby increasing its access count."""
        p = self._find_position(e)  # try to locate existing element
        if p is None:               # doesn't exist
            p = self._data.add_last(self._Item(e))  # add it to the PositionalList
        p.element()._count += 1     # increment count of p
        self._move_up(p)            # make sure it is in the right position


    def remove(self, e):
        """Remove element e from list of favourites."""
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        """Generate sequence of top k elements in terms of access counts."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for _ in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)
