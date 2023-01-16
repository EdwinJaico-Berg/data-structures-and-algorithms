from stack_implementation import ArrayStack


def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""
    S = ArrayStack()
    with open(filename) as f:
        for line in f:
            S.push(line.rstrip('\n'))

    # overwrite with contents in LIFO order
    with open(filename, 'w') as f:
        while not S.is_empty():
            f.write(S.pop() + '\n')


if __name__ == "__main__":
    file = "lorem_ipsum copy.rtf"
    reverse_file(file)
