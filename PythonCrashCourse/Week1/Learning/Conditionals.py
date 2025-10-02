cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

requested_toppings = [
    "mushrooms",
    "onions",
    "pineapple",
    "extra cheese",
    "green peppers",
]

print("mushrooms" in requested_toppings)

age = 12

if age < 4:
    print("$0")

elif age < 18:
    print("$25")

else:
    print("$40")


if "mushrooms" in requested_toppings:
    print("adding mushrooms")

if "pepperoni" in requested_toppings:
    print("adding pepperoni")

if "extra cheese" in requested_toppings:
    print("adding extra cheese")


for requested_topping in requested_toppings:
    print(f"adding {requested_topping}")

toppings = []

if toppings:
    for topping in toppings:
        print(topping)
else:
    print("no toppings available")

is_enabled = True

# ternary conditionals
status = "active" if is_enabled == True else "inactive"

print(status)

# any and all
numbers = [1, 2, 3, 4, 5, 6, 7, 0]

if any(number > 0 for number in numbers):
    print("There is at least one number in the list greater than 0")

if all(number > 0 for number in numbers):
    print("all numbers are greater than 0 in the list")
else:
    print("not all numbers in the list are greater than 0")


# chained comparisons
value = 100

if 0 <= value <= 100:
    print(value)


# dictionary-based dispatch
def start():
    print("starting")


def stop():
    print("stopping")


def restart():
    print("restarting")


def unknown():
    print("unknown command")


dispatch = {
    "start": start,
    "stop": stop,
    "restart": restart,
}

command = "start"

dispatch.get(command, unknown)()


lambda_dispatch = {
    "hello": lambda: print("hi there"),
    "bye": lambda: print("goodbye"),
}

l_command = "bye"

lambda_dispatch.get(l_command)()

# short circuit evaluation
colors = []

shades = colors or ["blue", "red", "yellow"]
print(shades)


# Walrus operator
# non-walrus version

# line = input("Enter text: ")

# while line != "quit":
#     print(f"you said {line}")
#     line = input("Enter text: ")


# # walrus equivalent
# while (line := input("Enter text: ")) != "quit":
#     print(f"you said {line}")


# filtering inside comprehensions


words = ["one", "two", "five", "eleven", "thirteen"]

if any((n := len(word)) > 3 for word in words):
    print(f"found a word longer than 3: {n}")
