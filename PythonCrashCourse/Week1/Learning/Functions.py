def greet_user(username: str) -> None:
    """Display a simple greeting."""
    print(f"Hello, {username}")


greet_user("jesse")


def describe_pet(pet_name: str, animal_type: str = "dog") -> None:
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# positional arguments
describe_pet("harry", "hamster")
describe_pet(animal_type="hamster", pet_name="larry")

# keyword arguments
describe_pet(animal_type="dog", pet_name="air bud")


pets = [
    {
        "animal_type": "hamster",
        "pet_name": "harry",
    },
    {"animal_type": "dog", "pet_name": "air bud"},
    {"pet_name": "larry"},
]

for pet in pets:
    describe_pet(**pet)

dog_names = [
    "air bud",
    "balto",
    "chaser",
    "laika",
    "sinbad",
    "bobbie the wonder dog",
]

# for dog in dog_names:
#     describe_pet(dog)


print("\n\n\n")


def get_formatted_name(first_name: str, last_name: str, middle_name: str = "") -> str:
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


def build_person(first_name: str, last_name: str, age: int = None) -> dict[str, str]:
    person = {"first": first_name, "last": last_name}

    if age:
        person["age"] = age

    return person


musician = get_formatted_name("jimi", "hendrix")
print(musician)

other_musician = get_formatted_name("john", "hooker", "lee")
print(other_musician)


hendrix = build_person("jimi", "hendrix", 27)
print(hendrix)


def greet_users(names: list[str]) -> None:
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


users = [
    "hannah",
    "ty",
    "margot",
]

greet_users(users)


def print_models(unprinted_designs: list[str], completed_models: list[str]) -> None:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)


def show_completed_models(completed_models: list[str]) -> None:
    print("\nThe following models have been printed")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = [
    "phone case",
    "robot pendant",
    "dodecahedron",
]

completed_models = []

print_models(unprinted_designs[:], completed_models)
print(unprinted_designs)
show_completed_models(completed_models)


# n-arguments
def make_pizza(size: int, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, "pepperoni")
make_pizza(12, "pepperoni", "mushroom", "bacon")


def build_profile(first: str, last: str, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last

    return user_info


user_profile = build_profile(
    "albert", "einstein", location="princeton", field="physics"
)
print(user_profile)
