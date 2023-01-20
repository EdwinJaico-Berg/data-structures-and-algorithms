from favourites_list import FavouritesList
from positional_list import PositionalList


class FavouritesListMTF(FavouritesList):
    """List of elements ordered with move-to-front heuristic."""

    # override _move_up to provide move-to-front semantics
    def _move_up(self, p):
        """Move accessed item at Position p to the front of the list."""
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))

    # we override top because list is no longer sorted
    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')

        # make copy of original
        temp = PositionalList()
        for item in self._data:
            temp.add_last(item)

        # repeatedly find, report and remove element with largest count
        for _ in range(k):
            # find and report next highest from temp
            high_pos = temp.first()
            walk = temp.after(high_pos)
            while walk is not None:
                if walk.element()._count > high_pos.element()._count:
                    high_pos = walk
                walk = temp.after(walk)
            # we have found the element with the highest count:
            yield high_pos.element()._value
            temp.delete(high_pos)