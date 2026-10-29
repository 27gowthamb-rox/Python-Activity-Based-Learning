print("Environmental Monitoring Data Analyzer")
locations = int(input("Number of locations: "))
days = int(input("Readings per location: "))
readings = []

for i in range(locations):
    row = []
    print("Location", i + 1)
    for j in range(days):
        row.append(float(input("Reading " + str(j + 1) + ": ")))
    readings.append(row)

lower = float(input("Lower acceptable limit: "))
upper = float(input("Upper acceptable limit: "))

for i in range(locations):
    total = 0
    minimum = readings[i][0]
    maximum = readings[i][0]

    for j in range(days):
        value = readings[i][j]
        total = total + value
        if value < minimum:
            minimum = value
        if value > maximum:
            maximum = value

    average = total / days
    print("Location", i + 1, "average:", round(average, 2),
          "minimum:", minimum, "maximum:", maximum)

    for j in range(days):
        value = readings[i][j]
        if value < lower or value > upper:
            print("Reading", j + 1, "outside limits:", value)