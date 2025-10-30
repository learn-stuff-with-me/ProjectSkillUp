# Terminal input application which will be used by one person at a time
# For each person who is going to be participating in the secret santa they will have
# to press enter once to get their secret santa match, and then press enter again
# to clear the terminal so that the next person is not able to see the results of the
# previous pick

# For each person in the group, if they have a significant other, or are part of a couple
# They will have to specify that in the beginning so that they cannot be matched with
# That person.

from random import randint
import time
import sys
import os
import csv
from pathlib import Path
import datetime as dt


def get_pairings(
    participants: list[str], significant_others: dict[str, str]
) -> dict[str, str]:

    matched = []
    pairings = {}

    for participant in participants:
        available_matches = [
            name
            for name in participants
            if name != participant
            and name != significant_others.get(participant)
            and name not in matched
        ]

        if len(available_matches) > 1:
            match_number = randint(0, len(available_matches) - 1)
        else:
            match_number = 0

        sec_san_match = available_matches[match_number]

        pairings[participant] = sec_san_match
        matched.append(sec_san_match)

    return pairings


def clear():
    # Windows
    if os.name == "nt":
        os.system("cls")
    # macOS and Linux
    else:
        os.system("clear")


def countdown(seconds):
    for i in range(seconds, 0, -1):
        sys.stdout.write(f"\rNext Match in: {i:2d} seconds")
        sys.stdout.flush()
        time.sleep(1)
    print("\r            ")


# setup input to allow for n number of participants before other inputs
print("Who will be participating in the secret santa?")
name = input("Enter a name:\n")

participants = []
significant_others = {}

while name.lower() != "no":
    names = name.replace(" ", "").split(",")

    if len(names) > 1:
        name, so_name = names
        participants.extend(names)
        significant_others[name] = so_name
        significant_others[so_name] = name

    else:
        participants.append(name)

    add_more = input(
        "Would you like to add more participants? Hit enter to continue and no to stop\n"
    )

    if add_more.lower() != "no":
        name = input("Enter a name: ")
        # has_so = input(f"Does {name} have a significant other?\n")
        # so_participating = input(f"Is {name}'s significant other participating?\n")

    else:
        if len(participants) % 2 != 0:
            print(
                """
                You have an uneven number of participants, you will not be able to
                match all of the participants
                """
            )
            sys.exit(1)
        break


missing_pairings = True

while missing_pairings:
    try:
        pairings = get_pairings(participants, significant_others)

        if pairings:
            missing_pairings = False

    except Exception as e:
        continue


print("The order of the pairings to be displayed will be as follows")
for name in pairings.keys():
    print(name)

countdown(5)

clear()
for name, pairing in pairings.items():
    print(f"{name}, Your match is: {pairing}")
    countdown(5)
    clear()


target_path = Path.cwd() / "SideProjects/SecretSantaPairings/"
now = dt.datetime.now()
file_name = now.strftime("secret_santa_pairings_%Y.csv")
final_path = target_path / file_name

with final_path.open("w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["name", "pairing"])

    for name, pairing in pairings.items():
        writer.writerow([name, pairing])
