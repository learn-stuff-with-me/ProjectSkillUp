# user inputs a number, if number is even // 2 otherwise it is 3 * number + 1
# keep calling the function until 1 is reached


def collatz(number: int) -> None:
    print(number)
    if number == 1:
        return number
    elif number % 2 == 0:
        collatz(number // 2)
    elif number % 2 == 1:
        collatz((3 * number) + 1)


user_number = input("Enter an integer:\n")

try:
    user_number = int(user_number)
    collatz(user_number)

except ValueError as e:
    print("you need to provide an integer")
