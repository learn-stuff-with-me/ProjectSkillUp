bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
print(bicycles[0])

for bike in bicycles:
    print(bike.title())


print("Exercises\n==========")
# 3-1
friend_names = ["james", "john", "jane"]
print(friend_names[0])
print(friend_names[1])
print(friend_names[2])

for friend in friend_names:
    print(f"hello, {friend}!")

print(bicycles)
bicycles[0] = "schwinn"
print(bicycles)

bicycles.append("trek")
print(bicycles)

bicycles.insert(0, "giant")
print(bicycles)

bicycles.insert(3, "nishiki")
print(bicycles)

del bicycles[0]
del bicycles[3]

print(bicycles)

print(bicycles.pop())
print(bicycles)

print(bicycles.pop(0))
print(bicycles)

bicycles.remove("nishiki")
print(bicycles)

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

print(sorted(cars))
print(sorted(cars, reverse=True))
print(cars)

cars.reverse()  # in place reversal
print(cars)
print(cars[::-1])  # returns a new list

colors = ["red", "blue", "red", "teal", "green", "yellow"]
print(colors.count("red"))
print(colors.index("blue"))

colors_2 = colors[:]
print(colors, colors_2)
colors_2.append("aquamarine")
print(colors, colors_2)

proper_cased_colors = [color.title() for color in colors]
print(proper_cased_colors)

# unpacking
coordinates_list = [2, 3]
coordinates_tuple = (2, 3)
coordinates_set = {2, 3}

a, b = coordinates_list
c, d = coordinates_tuple
e, f = coordinates_set

print(a, b)
print(c, d)
print(e, f)

print(colors + colors_2)

numbers = [1, 2, 3]

numbers.extend(
    [
        4,
        5,
        6,
    ]
)
print(numbers)

try:
    numbers.index(7)

except ValueError:
    print("item in the list could not be found")

numbers_2 = numbers.copy()

numbers.append(7)
print(numbers, numbers_2)

nested_list = [[1, 2], [3, 4]]
nested_2 = nested_list.copy()

nested_list.append([5, 6])
nested_2[0][1] = 10
print(nested_list, nested_2)

print(numbers)

first, second, *middle, almost_last, last = numbers
print(first, second, middle, almost_last, last)

# zipping
names = ["alice", "bob", "charlie"]
scores = [85, 90, 95]

pairs = list(zip(names, scores))
print(pairs)

print(numbers[::2])

flat = [x for sublist in nested_list for x in sublist]
print(flat)

names, scores = zip(*pairs)
print(names, scores)

zip_dictionary = dict(zip(names, scores))
print(zip_dictionary)

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

digits.reverse()
digits.reverse()
print(digits)

for item in reversed(digits):
    print(item)

print(list(range(0, 5, 2)))

for i in range(0, 11, 2):
    print(i)

print(sum(digits))
print(min(digits))
print(max(digits))

del digits[:3]
print(digits)
