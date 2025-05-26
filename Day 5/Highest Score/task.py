student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]


highest_Score=0

for num in student_scores:
    if num > highest_Score:
        highest_Score=num


print(highest_Score)
print(max(student_scores))