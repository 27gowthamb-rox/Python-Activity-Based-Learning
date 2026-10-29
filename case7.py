print("Product Price Fluctuation")
products = ["rice", "oil", "sugar"]
old_prices = []
new_prices = []

for product in products:
    print(product)
    old_prices.append(float(input("Previous price: ")))
    new_prices.append(float(input("Current price: ")))

threshold = float(input("Flag change above percent: "))
largest = -1
largest_product = ""

for i in range(len(products)):
    old = old_prices[i]
    new = new_prices[i]

    if old <= 0 or new < 0:
        print(products[i], "- invalid prices")
    else:
        change = (new - old) * 100 / old
        print(products[i], "change:", round(change, 2), "%")
        if abs(change) > threshold:
            print("Change exceeds threshold")
        if abs(change) > largest:
            largest = abs(change)
            largest_product = products[i]

if largest_product != "":
    print("Largest fluctuation:", largest_product, round(largest, 2), "%")