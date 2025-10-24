from pathlib import Path
import os

sample_path = Path("spam", "bacon", "eggs")
# print(sample_path)

# print(Path("spam") / "bacon" / "eggs")
# print(Path("spam") / Path("bacon/eggs"))
# print(Path("spam") / Path("bacon", "eggs"))

# print(Path.cwd())

sample_path_2 = Path("Week 2/PokemonAPI/APIProcessing/PokemonDataIngestion.py")
# print(sample_path_2.is_absolute())

absolute_path = Path.cwd() / sample_path_2

# print(f"Anchor: {sample_path_2.anchor}")
# print(f"Parent: {sample_path_2.parent}")
# print(f"Stem: {sample_path_2.stem}")
# print(f"Suffix: {sample_path_2.suffix}")
# print(f"Drive: {sample_path_2.drive}")

# print(f"Anchor: {absolute_path.anchor}")
# print(f"Parent: {absolute_path.parent}")
# print(f"Stem: {absolute_path.stem}")
# print(f"Suffix: {absolute_path.suffix}")
# print(f"Drive: {absolute_path.drive}")

# for parent in absolute_path.parents:
#     print(parent)

# print(os.listdir("d:\\ProjectSkillUp\\"))

skill_up_path = Path.cwd() / "Week 2" / "PokemonAPI" / "APIProcessing"
# print(skill_up_path)
# print(skill_up_path.is_file())
# print(skill_up_path.is_dir())

files = list(skill_up_path.glob("*.py"))


def read_file_print_lines(file_path: Path) -> None:
    with open(file_path, "r") as data_file:
        lines = data_file.readlines()

        for line in lines:
            print(line)


def append_line_to_file(file_path: Path, line: str) -> None:
    with open(file_path, "a") as data_file_append:
        data_file_append.write(line)


def write_file(file_path: Path, content: str) -> None:
    with open(file_path, "w") as data_file_writer:
        data_file_writer.write(content)


# for file in files:
#     print(file)

data_file_path = (
    Path.cwd() / "Week 3/AutomateTheBoringStuff/SampleFiles/" / "sample1.txt"
)

read_file_print_lines(data_file_path)

content = "this is some new text for the write file function"

write_file(data_file_path, content)

read_file_print_lines(data_file_path)
