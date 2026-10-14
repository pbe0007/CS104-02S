import csv

with open("vehicles.csv", "r", newline='') as f:
    reader = csv.DictReader(f)
    print(reader.fieldnames)