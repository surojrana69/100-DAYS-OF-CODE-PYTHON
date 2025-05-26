# from symtable import Function
#
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over"
# }
# # print(programming_dictionary["Function"])
# # print(programming_dictionary["Bug"])
# # print(programming_dictionary["Loop"])
#
# # Empty_Name = {}
# #
# # Empty_Name["Name"] = "Suroj"
# #
# # print(Empty_Name["Name"])
# #
# # #Deleting the existing dictionary
# # Empty_Name = {}
#
# #Modifying the item in the dictionary
#
# programming_dictionary["Bug"]="A unexcepted errors in the computer"
#
# # print(programming_dictionary["Bug"])
#
# for keys in programming_dictionary:
#     print(keys)
#     print(programming_dictionary[keys])

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]

    if score > 90:
        grade = "Outstanding"
    elif score > 80:
        grade = "Exceeds Expectations"
    elif score > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"

    student_grades[student] = grade
