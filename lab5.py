import sys

### hardcoded information and formatting stuff

# grade weights for the class
weights = {
    "Quiz" : 10,
    "Labs" : 30,
    "Test1" : 15,
    "Test2" : 15,
    "Project" : 20,
    "Final" : 10
}

# dict associating the internal grade names with the longer names for output:
assignment_names = {
    "Quiz" : "quiz",
    "Labs" : "lab",
    "Test1" : "test1",
    "Test2" : "test2",
    "Project" : "Capstone Project",
    "Final" : "final exam"
}

# a dictionary to easily hold grade boundaries. Everything equal to or above the key
# of the format {min score:letter}
boundaries = {
    90: "A",
    80: "B",
    70: "C",
    60: "D",
    0: "F"
}
# formatting info for the output table
name_col_width = 25 # 'Student Name' is 12 characters as a minimum
score_col_width = 15 # 'Final Score' is 11 characters as a minimum
grade_col_width = 5 # 'grade' is 5 characters long as a minimum
linebreak_width = name_col_width + score_col_width + grade_col_width + 2
# going ahead and generating the linebreak string
linebreak = ""
for i in range(0,linebreak_width):
    linebreak += "-"


# out_of means the number that the weights are out of, or the sum of all the values of the weights
def weighted_average(weights, student_scores, out_of = 100):
    total = 0
    # this goes through all of the scores a student has, and references the weights dict for weights.
    # This allows the weights dict to contain more assignment weights than strictly necessary
    # which can be used for exempt assignments, for instance.
    for assignment in student_scores:
        # catch if the weights dictionary lacks the assignment
        try:
            total += weights[assignment] * student_scores[assignment]
        except:
            print(f"error, {assignment} not in provided weight set")
            return 0
    return total / out_of

# open a (the) csv in the same format as the example, and construct the dictionary
# dynamically. That is, this can accept any number of assignments per student,
# and any number of students
def data_construct(file):
    # defines the headers
    lines = file.readlines()
    score_types = lines[0].strip().split(",")
    score_types.pop(0)
    #empty dict for output
    class_data = {}
    # reads each line after the headers, then creates a sub-dictionary for each
    # student from those lines in the format {"Assignment":score, etc}
    for student_init in lines[1:]:
        student_list = student_init.strip().split(",")
        student_scores = {}
        for i in range(1,len(student_list)):
            student_scores[score_types[i-1]] = int(student_list[i])
        student_scores["final_score"] = weighted_average(weights,student_scores)
        student_scores["grade"] = letter_grade(student_scores["final_score"])
        class_data[student_list[0]] = student_scores
    return class_data

# convert the provided score (out of 100) into a letter grade
def letter_grade(score):
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

# returns the average value for some assignment across all students
def col_average(column, data):
    total2 = 0
    count2 = 0
    for row in data:
        total2 += data[row][column]
        count2 += 1
    return total2 / count2

############## main #################
# catch that a filename has been passed and exists
try:
    file = sys.argv[1]
    open(file,"r")
except:
    sys.exit("Please put a valid .csv file as the first CMD line argument")

# output string
out = ""

with open(file,"r") as f:
    grade_data = data_construct(f)
    # table header
    out += linebreak + "\n"
    out += f"{"Student Name" : <{name_col_width}}{"Final Score" : <{score_col_width}}{"Grade" : <{grade_col_width}}\n"
    out += linebreak + "\n"
    #body of table
    for student in grade_data:
        out += f"{student: <{name_col_width}}{grade_data[student]["final_score"]: <{score_col_width}}{grade_data[student]["grade"] : <{grade_col_width}}\n"
    out += linebreak + "\n"
    # other lines of the output
    out += f"Number of students in class: {len(grade_data)}\n"
    # shorter and dynamic way to list all class averages
    for assignment in assignment_names:
        temp = col_average(assignment, grade_data)
        out += f"Class average of {assignment_names[assignment]}: {temp: .2f} {letter_grade(temp)}\n"
    # the last row is singled out because it is in a slightly different format and the concerned columns are added
    # dynamically which would confuse the data entry (at the top of the program) if anything were to change
    # also, the example shows a final
    out += f"Class average grade: {col_average("final_score", grade_data): .2f} {letter_grade(col_average("final_score", grade_data))}"
    print(out)

# bonus. im using grade_report_2 so as to not overwrite the other one.
with open("grade_report_2.txt","w") as o:
    o.write(out)

sys.exit("Done")

