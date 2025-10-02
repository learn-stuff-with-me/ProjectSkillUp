alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])

print(alien_0)

alien_0["x_pos"] = 0
alien_0["y_pos"] = 25

print(alien_0)

alien_0 = {"x_pos": 0, "y_pos": 25, "speed": "medium"}

print(f"original position: {alien_0['x_pos']}")


if alien_0["speed"] == "slow":
    x_increment = 1

elif alien_0["speed"] == "medium":
    x_increment = 2

else:
    x_increment = 3

alien_0["x_pos"] = alien_0["x_pos"] + x_increment

print(f"new position: {alien_0['x_pos']}")

del alien_0["x_pos"]
alien_0.get("x_pos", 0)
print(f"position: {alien_0.get('x_pos', 0)}")

print(alien_0)

# for key, value in alien_0.items():
#     print(key, value)


# for key in alien_0.keys():
#     print(key)

# for value in alien_0.values():
#     print(value)

# for key in sorted(alien_0.keys()):
#     print(key)

print("\n\n\n")
alien_1 = {"color": "green", "points": 5}
alien_2 = {"color": "yellow", "points": 10}
alien_3 = {"color": "red", "points": 15}

aliens = []

for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# for alien in aliens[:5]:
#     print(alien)

# print(f"there are {len(aliens)} aliens")

for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["points"] = 10
        alien["speed"] = "medium"

# for alien in aliens[:5]:
#     print(alien)


pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}

# for topping in pizza["toppings"]:
#     print(topping)


users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['location']}"

    print(full_name)
    print(location)


squares = {x: x**2 for x in range(5)}
print(squares)

defaults = {
    "color": "blue",
    "size": "M",
}

overrides = {"size": "L"}

settings = {**defaults, **overrides}
print(settings)

names = ["alice", "bob"]
scores = [85, 90]

d = dict(zip(names, scores))
print(d)

persons = [
    {"name": "bob", "age": 30},
    {"name": "james", "age": 25},
]


def greet(name, age):
    print(f"Hello {name}, age: {age}")


for person in persons:
    greet(**person)
