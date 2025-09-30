# exercise 2-1 simple message:
message = "this is a simple message"
print(message)

# exercise 2-2 simple message cont.:
new_message = "this will be replaced"
print(new_message)
new_message = "see, this has changed"
print(new_message)

# if anything in quotes is considered a string in python
# does that also mean that one character is also a string so long as it is in quotes?
# YES
am_i_string = "a"
print(type(am_i_string))

name = "ada lovelace"
print(name.title())

print(name.lower())
print(name.upper())


first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

print("Whitespace Stripping\n================")
favorite_language = "   python   "
print(favorite_language)
print(f"'{favorite_language.rstrip()}'")
print(f"'{favorite_language.lstrip()}'")
print(f"'{favorite_language.strip()}'")

print("Removing Prefixes\n==============")
url = "https://nostarch.com"
print(url.removeprefix("https://"))
print(url.removesuffix(".com"))

# what remove prefix and remove suffix actually are doing
print(url[len("https://") :])
print(url[: -len(".com")])

print("Exercises 2.3-2.8\n================")
someones_name = "john doe"
print(f"Hello, {someones_name.title()}, are you having a good day today?")
print(someones_name.lower())
print(someones_name.upper())
print(someones_name.title())
print(someones_name.capitalize())

famous_person = "Albert Einstein"
quote = f'{famous_person} once said, "A person who never made a mistake never tried anything new"'
print(quote)

whitespace_name = "\tjane \n\t\tdoe"
print(whitespace_name)
print(whitespace_name.strip())
print(whitespace_name.lstrip())
print(whitespace_name.rstrip())

text_file = "python_notes.txt"
print(text_file.removesuffix(".txt"))

print("Numbers\n=======")
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)
print(type(3 / 2))
print(3**2)
print(3**3)
print(10**6)
print(2 + 3 * 4)
print((2 + 3) * 4)

print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)
print(0.2 + 0.1)
print(0.3 + 0.1)
print(0.4 + 0.1)
print(0.5 + 0.1)

print(type(5 * 6))
print(type(6 / 3))

import this
