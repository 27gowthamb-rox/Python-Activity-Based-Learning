print("Student Academic Risk Classification")
count = int(input("Number of students: "))
names = []
marks = []
attendance = []
labs = []

for i in range(count):
    names.append(input("Student name: "))
    marks.append(float(input("Average marks: ")))
    attendance.append(float(input("Attendance percent: ")))
    labs.append(float(input("Lab score: ")))

for i in range(count):
    risks = 0
    if marks[i] < 50:
        risks = risks + 1
    if attendance[i] < 75:
        risks = risks + 1
    if labs[i] < 50:
        risks = risks + 1

    if risks == 0:
        category = "Low"
    elif risks == 1:
        category = "Moderate"
    else:
        category = "High"

    print(names[i], "-", category, "risk; factors:", risks)