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

data_header, data_body = dict, tuple

def stat_head_discriminator(thing):
    if type(thing) == str:
        return data_header[thing]
    if type(thing) == int:
        return thing
    else:
        sys.exit(f"Error: {thing} is of type {type(thing)}, which is not a valid column id (header)")

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



# returns a tuple (number of filled entries, number of empty)
def stat_num_valued(header, data = data_body):
    index = stat_head_discriminator(header)
    empty = 0
    filled = 0
    ##### num_blank and num_valued
    for row in data:
        if row[index] == '':
            empty += 1
        else:
            filled += 1
    return tuple((filled,empty))

def stat_num_unique(header, data = data_body):
    index = stat_head_discriminator(header)
    return len(get_values(header, True, data))

def stat_average(header, skip = True, data = data_body):
    index = stat_head_discriminator(header)
    sum = 0
    count = 0
    for row in data:
        if not skip:
            count += 1
        if type(row[index]) in (int,float):
            if skip:
                count += 1
            sum += row[index]
    return sum / count



# this function takes a header and a dataset and returns a dict full of various statistics about it
# currently implemented: range || num_blank, num_valued, unique_values, num_unique_values, all_values
def stats(header, data = data_body):
    output_dict = {}

    ##### range, a tuple in form (min, max)
    output_dict["range"] = tuple((min(numbers),max(numbers)))

    ########## non-numerical statistics

    temp1 = stat_num_valued(header,data)
    output_dict["num_blank"] = temp1[1]
    output_dict["num_valued"] = temp1[0]

    ##### unique_values, a tuple of all unique values (not '')
    output_dict["unique_values"] = get_values(header, True, data)

    ##### num_unique_values, the len of unique_values
    output_dict["num_unique_values"] = len(output_dict["unique_values"])

    ##### all_values, a tuple of all values that are not ''
    output_dict["all_values"] = get_values(header, False, data)


    return output_dict   



# similar format as stat_numerical, but for non-numeric things
### defunct
"""
# currently implemented: num_blank, num_valued, unique_values, num_unique_values, all_values
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

    ##### num_unique_values, the len of unique_values
    output_dict["num_unique_values"] = len(output_dict["unique_values"])

    ##### all_values, a tuple of all values that are not ''
    output_dict["all_values"] = get_values(header, False, data)


    return output_dict
"""

# returns a new datastructure that satisfies the value condition in the specified column (header), value should be a tuple,
# A tuple with exactly two integers (or strings) is treated like a range (small, big). A tuple starting with "$%Exp%$", 
# then ">" or "<" and then a number(or string, if wanting to sort alphabetically)
# specifies the corresponding relationship. For more complex relationships, nest data_filter calls
def data_filter(header, value, data = data_body):
    index = stat_head_discriminator(header)
    output_struct = []
    if value[0] == "$%Exp%$":
        if value[1] == "<":
            for row in data:
                if row[index] <= value[2]:
                    output_struct.append(row)
            return tuple(output_struct)
        elif value[1] == ">":
            for row in data:
                if row[index] >= value[2]:
                    output_struct.append(row)
            return tuple(output_struct)
        else:
            try:
                for row in data:
                    if row[index] >= value[1] and row[index] <= value[2]:
                        output_struct.append(row)
                return tuple(output_struct)
            except:
                return("Invalid Value")
    else:
        for row in data:
            if row[index] in value:
                output_struct.append(row)
        return tuple(output_struct)




# returns a dictionary with the unique values of header A as keys, and the specified statistical function
# as dictionary values.  The statistical function runs across the values of header_b within data
# hol_o_num indicates whether to call stat_holistic or stat_numerical
def stat_correlation(header_a, header_b, stat, data = data_body):
    output_dict = {}
    for unique in get_values(header_a, True, data):
        filtered = data_filter(header_a, unique, data)
        output_dict[unique] = stats(header_b, filtered).get(stat, "whoops, no value here")
    return output_dict

# main interactive menu, can be called again if the user wants to run through the process again.
# returns items to be printed.

# behavior:
# 1 asks the user what to do, narrow data range, get average, mean, med, mode, etc
# 2 does so, prints whatever stat plus the length of the current data length
# 2.1 the user can repeat these, if it is a function that narrows the data, this will persist. return to 1 with modified settings
# 2.2 the user can return to baseline, return to 1 with original settings
# 3 the user can choose to print
def menu(data = data_body, context = {"Filename":"None","Filters":[]}):
    temp = ''
    if len(context["Filters"]) != 0:
        temp += "that is "
    for i in range(len(context["Filters"])):
        if
    print(f"""
Considering data from {context["Filename"]} {}
""")


############### MAIN #####################
if __name__ == "__main__":
    # 0 if the user did not provide a file on initialization, it will ask for one
    try:
        data_header, data_body = load_vehicle_data(make_csv(sys.argv[1]))
    except IndexError:
        print("No argument passed, please input a valid filename")
        stuck = True
        temp = ""
        while stuck:
            try:
                data_header, data_body = load_vehicle_data(make_csv(input(temp)))
                stuck = False
            except FileNotFoundError:
                temp = "Invalid name, try again \n"
    except FileNotFoundError:
        print("The filename passed wasn't found!")
        stuck = True
        temp = ""
        while stuck:
            try:
                data_header, data_body = load_vehicle_data(make_csv(input(temp)))
                stuck = False
            except FileNotFoundError:
                temp = "Invalid name, try again \n"
    except:
        print("unknown error")

    menu_out = menu()



year_stats = stats("year") 

print(f"The number of vehicles is: {len(get_values("id"))}")
print(f"The range of years is: {year_stats["range"][0]:.0f} to {year_stats["range"][1]:.0f}")
print(f"The number of car manufacturers is: {len(get_values("make",True))}")
temp = stat_correlation("make", "model", "num_unique_values")
#print(temp)
temp2 = max(temp.values())
temp3 = ""
for key in temp:
    if temp[key] == temp2:
        temp3 = key
        continue
print(f"The most productive manufacturer is: {temp3}")


# print(data_header)
# print(type(data_body))
# print(data_body[0])


