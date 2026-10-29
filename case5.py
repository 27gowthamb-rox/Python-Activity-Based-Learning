print("Food Waste Monitoring")
days = int(input("Number of days: "))
limit = float(input("Acceptable waste percentage: "))

for day in range(1, days + 1):
    prepared = int(input("Meals prepared: "))
    served = int(input("Meals served: "))

    if prepared <= 0 or served < 0 or served > prepared:
        print("Day", day, "- invalid meal counts")
    else:
        leftover = prepared - served
        waste = leftover * 100 / prepared
        print("Day", day, "leftovers:", leftover,
              "waste:", round(waste, 2), "%")
        if waste > limit:
            print("Above acceptable limit")