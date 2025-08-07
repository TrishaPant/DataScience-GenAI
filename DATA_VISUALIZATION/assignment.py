# https://api.nobelprize.org/v1/prize.json


import json
import numpy as np


with open("prize.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# print(data)
# print(type(data))

years = [prize["year"] for prize in data["prizes"]]

# print(years)

years_array = np.array(years)

unique_years, counts = np.unique(years_array, return_counts=True)

print("\n" + "-" * 32)
print(f"{'Year':<10} | {'Prizes Count':<15}")
for year, count in zip(unique_years, counts):
    print(f"{year:<10} | {count:<15}")
print("-" * 32)

# Fix the logic of prize count per year
total_years = len(unique_years)
total_prizes = len(data["prizes"])
total_laureates = sum(len(prize.get("laureates", [])) for prize in data["prizes"])
unique_categories = set(prize["category"] for prize in data["prizes"])

print(f"Total years present      : {total_years}")
print(f"Total prizes awarded     : {total_prizes}")
print(f"Total Laureates Honoured : {total_laureates}")
print(f"Total unique categories  : {len(unique_categories)}")


