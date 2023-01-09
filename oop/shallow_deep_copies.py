warm_tones = ['orange', 'brown', 'red']

palette = list(warm_tones)

print("Warm tones ids")
for item in warm_tones:
    print(item, id(item))

print("Palette ids")
for item in palette:
    print(item, id(item))

print("Changing element in warm tones")
warm_tones[0] = 'maroon'

print("Warm tones ids")
for item in warm_tones:
    print(item, id(item))

print("Palette ids")
for item in palette:
    print(item, id(item))
