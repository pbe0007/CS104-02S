import sys

# open a (the) csv in the same format as the example, and construct the dictionary
# dynamically. That is, this can accept any number of assignments per student,
# and any number of students
def data_construct(file):
    # defines the headers
    lines = file.readlines()
    score_types = lines[0].strip().lower().split(",")
    score_types.pop(0)
    #empty dict for output
    class_data = {}
    # reads each line after the headers, then creates a sub-dictionary for each
    # student from those lines in the format {"Assignment":score, etc}
    for student_init in lines[1:]:
        student_list = student_init.strip().lower().split(",")
        student_scores = {}
        for i in range(1,len(student_list)):
            student_scores[score_types[i-1]] = int(student_list[i])
        class_data[student_list[0]] = student_scores
    return class_data


def letter_grade(score):
    # a dictionary to easily hold grade boundaries. Everything equal to or above the key
    # of the format {min score:letter}
    boundaries = {
        90: "A",
        80: "B",
        70: "C",
        60: "D",
        0: "F"
    }
    # error catching
    try:
        int(score)
    except:
        return(0)

    for step in boundaries:
        if int(score) >= step:
            return boundaries[step]
    # catch if the score somehow is not within the range defined
    return("Error")

# out_of 
def weighted_average(weights, student_scores, out_of = 100):
    total = 0
    # this goes through all of the scores a student has, and references the weights dict for weights. 
    # This allows the weights dict to contain more assignment weights than strictly necessary
    # which can be used for exempt assignments, for instance.
    for assignments in student_scores:
        # catch if the weights dictionary lacks the assignment
        try:
            total += weights[assignments] * student_scores[assignments]
        except: 
            print(f"error, {assignments} not in provided weight set")
            return 0
    return total / out_of


############## main #################
with open(sys.argv[1]) as f:
    print(data_construct(f))

print(letter_grade(89))
print(letter_grade(-1))




