from tree_implementation import Tree


# -------------------------- Table of contents --------------------------------
def preorder_indent(T: Tree, p: Tree.Position, d: int) -> None:
    print(2*d*'' + str(p.element()))
    for c in T.children(p):
        preorder_indent(T, c, d+1)


def preorder_label(T: Tree, p: Tree.Position, d: int, path: list) -> None:
    """Print labelled representation of subtree of T rooted at p at depth d."""
    label = '.'.join(str(j+1) for j in path)
    print(2*d*'' + label, p.element())
    path.append(0)
    for c in T.children(p):
        preorder_label(T, c, d+1, path)
        path[-1] += 1
    path.pop()


# -------------- Parenthetic representation of a Tree ------------------------
def parenthesize(T: Tree, p: Tree.Position) -> None:
    """Print parenthesized representation of subtree of T rooted at p."""
    print(p.element(), end='')
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = ' (' if first_time else ', '
            print(sep, end='')
            first_time = False
            parenthesize(T, c)
        print(')', end='')


# ------------------------- Computing disk space -----------------------------
def disk_space(T, p):
    """Return total disk space for subtree of T rooted at p."""
    subtotal = p.element().space()
    for c in T.children(p):
        subtotal += disk_space(T, c)
    return subtotal
