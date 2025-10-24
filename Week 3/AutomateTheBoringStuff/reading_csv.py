import csv
from pathlib import Path
import json
import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

csv_data_path = Path("d:/Data/csv_data")

file_name = "Popular_Baby_Names.csv"

# with open(csv_data_path / file_name, "r") as csv_file:
#     reader = csv.DictReader(csv_file)

#     csv_data = list(reader)


# print(json.dumps(csv_data, indent=4))

df = pd.read_csv(
    csv_data_path / file_name,
    names=["Year of Birth", "Gender", "Ethnicity", "First Name", "Count", "Rank"],
)


print(df.sort_values(by=["Year of Birth"]))
