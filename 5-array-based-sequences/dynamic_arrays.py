import sys

data = []
for _ in range(10):
    a = len(data)
    b = sys.getsizeof(data)
    print(f'Length: {a}; Size in bytes: {b}')
    data.append(None)
