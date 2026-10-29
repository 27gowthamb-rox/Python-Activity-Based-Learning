print("Employee Shift Conflict Detection")
count = int(input("Number of shifts: "))
shifts = []

for i in range(count):
    employee = input("Employee name: ")
    start = int(input("Start hour: "))
    end = int(input("End hour: "))
    shifts.append((employee, start, end))

conflict_found = False

for i in range(len(shifts)):
    employee1, start1, end1 = shifts[i]
    for j in range(i + 1, len(shifts)):
        employee2, start2, end2 = shifts[j]
        if employee1 == employee2 and start1 < end2 and start2 < end1:
            print(employee1, "has overlapping shifts:",
                  start1, "-", end1, "and", start2, "-", end2)
            conflict_found = True

if not conflict_found:
    print("No conflicts found")