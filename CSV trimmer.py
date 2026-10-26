import csv
cs104_headers=[
    "id", "year", "make", "model",
    "cylinders","VClass","city08",
    "highway08","comb08","fuelType",
    "atvType", "co2", "displ",
    "trany", "drive"]
with open("vehicles.csv", "r", newline = '') as v, open("vehicles_cs104", "w", newline='') as w:
    raw_data = csv.DictReader(v)
    writer = csv.DictWriter(w, cs104_headers)
    writer.writeheader()
    print(raw_data.fieldnames)
    for row in raw_data:
        new_row = {}
        for header in cs104_headers:
            new_row[header] = row[header]
        writer.writerow(new_row)




