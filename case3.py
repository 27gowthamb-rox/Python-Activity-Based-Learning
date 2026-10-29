print("Student Marks Matrix Analysis")
students = int(input("Number of students: "))
subjects = int(input("Number of subjects: "))
marks = []

for i in range(students):
    row = []
    for j in range(subjects):
        row.append(int(input("Student " + str(i + 1) +
                             ", subject " + str(j + 1) + ": ")))
    marks.append(row)

best_total = -1
top_student = 0

for i in range(students):
    total = 0
    for j in range(subjects):
        total = total + marks[i][j]
    print("Student", i + 1, "total:", total,
          "average:", round(total / subjects, 2))
    if total > best_total:
        best_total = total
        top_student = i + 1

for j in range(subjects):
    total = 0
    for i in range(students):
        total = total + marks[i][j]
    print("Subject", j + 1, "average:", round(total / students, 2))

print("Top student:", top_student, "with total", best_total)