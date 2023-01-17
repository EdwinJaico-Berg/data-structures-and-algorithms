from positional_list import PositionalList


def insertion_sort(L: PositionalList):
    """Sort PositionalList of comparable elements into non-decreasing order."""
    if len(L) > 1:  # otherwise no need to sort
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():  # means that they're in the correct position
                marker = pivot  # pivot becomes the new marker
            else:
                walk = marker
                # Use walk to find the correct position for pivot
                while walk != L.first() and L.before(walk).element > value:
                    walk = L.before(walk)
                # correct position found, delete pivot and reinsert value
                L.delete(pivot)
                L.add_before(walk, pivot)
