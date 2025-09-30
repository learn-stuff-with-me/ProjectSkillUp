test_string = "This is a testing stringß"
second_test = "This is another string"
third_test = "ThIS is another string"

print("casefold vs. lower\n===================")
print(test_string.lower())

print(test_string.casefold())

print("Capitalize\n============")
print(test_string.capitalize())

print("endswith\n============")
print(second_test.endswith("ng"))
print(second_test.endswith("ing"))
print(second_test.endswith("is"))
print(second_test.endswith(("g", "ing")))
print(second_test.endswith(("es", "is")))
# this will return False because this function uses the slicing notation where the
# first index is inclusive and the second index is exclusive, so this will result in
# a check that asks if Thi ends in is which is False
print(second_test.endswith("is", 0, 3))
print(second_test.endswith("is", 0, 4))
print(second_test[0:3])
print(second_test.endswith("hi", 0, 3))
# endswith is case sensitive, this will return False
print(third_test.endswith("is", 0, 4))
