import csv
import sys

def make_csv(filename):
    new_filename = "trimmed_vehicles.csv"
    cs104_headers=[
        "id", "year", "make", "model",
        "cylinders","VClass","city08",
        "highway08","comb08","fuelType",
        "atvType", "co2", "displ",
        "trany", "drive"]
    with open(filename, "r", newline = '') as v, open(new_filename, "w", newline='') as w:
        raw_data = csv.DictReader(v)
        writer = csv.DictWriter(w, cs104_headers)
        writer.writeheader()
        # print(raw_data.fieldnames)
        for row in raw_data:
            new_row = {}
            for header in cs104_headers:
             new_row[header] = row[header]
            writer.writerow(new_row)
    return new_filename

def load_vehicle_data(filename):
    new_set = []
    indeces = {}
    with open (filename, "r", newline = '') as f:
        reader = csv.reader(f)
        for row in reader:
            new_set.append(tuple(row))
    for item in new_set[0]:
        indeces[item] = new_set[0].index(item)
    # returns a nested tuple, with index 0 holding a dictionary for easy header lookup, and
    # index 1 holding the data. A tuple holding all the rows of data as tuples.
    # them being tuples is not strictly necessary, but it is technically more efficient for searching
    # through the data to make statistics, and they don't need to be mutable
    return (indeces,tuple(new_set[1:]))

data_header, data_body = load_vehicle_data(make_csv("vehicles.csv"))

def stat_head_discriminator(thing):
    if type(thing) == str:
        return data_header[thing]
    if type(thing) == int:
        return thing
    else:
        sys.exit(f"Error: {thing} is of type {type(thing)}, which is not valid.")

def get_values(header, unique = False, data = data_body):
    index = stat_head_discriminator(header)
    if unique == True:
        temp_set = set(())
        for row in data:
            temp_set.add(row[index])
        return tuple(temp_set) 
    else:
        temp_list = []
        for row in data:
            if row[index] != '':
                temp_list.append(row[index])
        return tuple(temp_list)

# this function takes a header and returns a dictionary with various statistical
# figures based on that column

# currently implemented: range, entry_num
def stat_numerical(header, data = data_body):
    index = stat_head_discriminator(header)
    output_dict = {}
    numbers = []
    # get all the numbers
    for row in data:
        if row[index] != '':
            try:
                numbers.append(float(row[index]))
            except ValueError:
                continue
    # catch if there are no numbers
    if numbers == []:
        print(f"""The column:'{header}' does not have any numbers for stats!""")
        numbers = [0]
    numbers.sort()

    ##### range, a tuple in form (min, max)
    output_dict["range"] = tuple((min(numbers),max(numbers)))

    ##### entry_num, the number of non-blank entries for this header
    output_dict["entry_num"] = len(numbers)


    return output_dict
   

# similar format as stat_numerical, but for non-numeric things

# currently implemented: num_blank, num_valued, unique_values, all_values
def stat_holistic(header, data = data_body):
    index = stat_head_discriminator(header)
    output_dict = {}
    temp1 = 0
    temp2 = 0
    ##### num_blank and num_valued
    for row in data:
        if row[index] == '':
            temp1 += 1
        else:
            temp2 += 1
    output_dict["num_blank"] = temp1
    output_dict["num_valued"] = temp2

    ##### unique_values, a tuple of all unique values (not '')
    output_dict["unique_values"] = get_values(header, True, data)

    ##### all_values, a tuple of all values that are not ''
    output_dict["all_values"] = get_values(header, False, data)


    return output_dict

# returns a new datastructure with the filter applied
def data_filter(header, value, data = data_body):
    index = stat_head_discriminator(header)
    output_struct = ()
    for row in data:
        if row[index] == value:
            output_struct.add(row)
    return output_struct

# returns a dictionary with the unique values of header A as keys, and the specified statistical function
# as dictionary values.  The statistical function runs across the values of header_b within data
# hol_o_num indicates whether to call stat_holistic or stat_numerical
def stat_correlation(header_a, header_b, stat, hol_o_num, data = data_body):
    output_dict = {}
    for unique in get_values(header_a, True, data):
        with data_filter(header_a, unique, data) as filtered:
            if hol_o_num == "num":
                output_dict[unique] = stat_numerical(header_b, filtered).get(stat,default = "whoops, no value here")
            else:
                output_dict[unique] = stat_holistic(header_b, filtered).get(stat,default = "whoops, no value here")
    return output_dict

############### MAIN #####################
year_stats = stat_numerical("year") 

print(f"The number of vehicles is: {stat_count("id")}")
print(f"The range of years is: {year_stats["range"][0]:.0f} to {year_stats["range"][1]:.0f}")
print(f"The number of car manufacturers is: {stat_count("make",True)}")


# print(data_header)
# print(type(data_body))
# print(data_body[0])


