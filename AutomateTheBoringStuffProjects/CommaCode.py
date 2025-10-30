# function to generate a comma separated list of items with the last item being prefixed
# with , and item


def oxford_comma_list(items: list[str]) -> str:

    joined_str = ""

    if items:
        for i, item in enumerate(items):
            if i == len(items) - 1:
                joined_str += f"and {item}"

            else:
                joined_str += f"{item}, "

    return joined_str


def oxford_comma_list_str_join(items: list[str]) -> str:
    if len(items) <= 2:
        return " and ".join(items)

    else:
        return f"{', '.join(items[:-1])}, and {items[-1]}"


test = oxford_comma_list(["apples", "bannanas", "tofu"])
test_2 = oxford_comma_list_str_join(["apples", "bannanas", "tofu"])

print(test)
print(test_2)
