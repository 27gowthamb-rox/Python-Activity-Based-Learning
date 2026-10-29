print("Smart Canteen Order and Stock Management")
items = ["sandwich", "juice", "fruit"]
prices = [50, 30, 20]
stock = [10, 12, 15]
sales = 0

orders = int(input("Number of orders: "))

for order in range(orders):
    for i in range(len(items)):
        print(i + 1, items[i], "Rs.", prices[i], "stock:", stock[i])

    choice = int(input("Item number: "))
    quantity = int(input("Quantity: "))

    if choice < 1 or choice > len(items) or quantity <= 0:
        print("Order rejected: invalid choice or quantity")
    else:
        index = choice - 1
        if quantity > stock[index]:
            print("Order rejected: insufficient stock")
        else:
            bill = prices[index] * quantity
            stock[index] = stock[index] - quantity
            sales = sales + bill
            print("Order accepted. Bill: Rs.", bill)

print("Total sales: Rs.", sales)
for i in range(len(items)):
    print(items[i], "remaining stock:", stock[i])