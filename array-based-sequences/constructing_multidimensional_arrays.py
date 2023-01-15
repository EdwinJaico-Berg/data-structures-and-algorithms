def incorrect_multidimensional_array_construction():
    r = 3
    c = 3
    data = [[0] * c] * r

    print(data)
    data[2][0] = 100
    print(id(data[2][0]), id(data[1][0]), data)


def correct_multidimensional_array_construction():
    r = 3
    c = 3
    data = [[0] * c for j in range(r)]

    print(data)
    data[2][0] = 100
    print(id(data[2][0]), id(data[1][0]), data)