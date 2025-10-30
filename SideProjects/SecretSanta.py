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
    """
    Generate Secret Santa pairings while avoiding self-assignments and (optionally) significant others.
    Parameters
    ----------
    participants : list[str]
        Sequence of participant names. Each participant is assigned exactly one recipient (a different participant).
    significant_others : dict[str, str]
        Mapping from participant name to their significant other's name. A participant will not be assigned to the name
        returned by significant_others.get(participant). If you want the exclusion to apply in both directions you should
        include both entries (A->B and B->A) in this mapping.
    Returns
    -------
    dict[str, str]
        A dictionary mapping each participant to the participant they should give a gift to. Each recipient will appear
        at most once (i.e., assignments are unique recipients).
    Raises
    ------
    IndexError
        If, when processing a participant, there are no valid available matches (empty candidate list). This can occur
        when the greedy one-pass algorithm cannot satisfy all constraints given the current ordering of participants.
    NameError
        If the function's implementation expects random.randint to be in scope but has not been imported in the caller's
        module (ensure `from random import randint` or `import random` is available).
    Notes
    -----
    - The implementation performs a single greedy pass over `participants`. For each participant it builds a list of
      candidates that are not the participant themselves, are not the participant's significant other (if present), and
      have not already been assigned as a recipient. One candidate is chosen at random using randint.
    - Because the algorithm is greedy and uses random selection among candidates, it may fail to produce a complete
      assignment even when a valid global assignment exists. If you need guaranteed-success matchings, consider using
      a backtracking or matching algorithm (e.g., bipartite matching) instead.
    - Results are non-deterministic unless the random seed is fixed externally.
    Examples
    --------
    >>> participants = ['Alice', 'Bob', 'Carol']
    >>> significant_others = {'Alice': 'Bob', 'Bob': 'Alice'}
    >>> # Possible output (order and choices may vary due to randomness):
    >>> {'Alice': 'Carol', 'Bob': 'Alice', 'Carol': 'Bob'}
    """

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
        final_pairings = get_pairings(participants, significant_others)

        if final_pairings:
            missing_pairings = False

    except IndexError as e:
        continue


print("The order of the pairings to be displayed will be as follows")
for name in final_pairings:
    print(name)

countdown(5)

clear()
for name, pairing in final_pairings.items():
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

    for name, pairing in final_pairings.items():
        writer.writerow([name, pairing])
