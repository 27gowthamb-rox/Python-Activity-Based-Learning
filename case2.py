print("Repeated Transaction Detection")
count = int(input("Number of transactions: "))
transactions = []

for i in range(count):
    transaction_id = input("Transaction ID: ")
    amount = float(input("Amount: "))
    transactions.append((transaction_id, amount))

threshold = float(input("Suspicious amount threshold: "))
found = False

for i in range(len(transactions)):
    transaction_id, amount = transactions[i]
    duplicate = False

    for j in range(i):
        earlier_id, earlier_amount = transactions[j]
        if transaction_id == earlier_id:
            duplicate = True

    if duplicate or amount > threshold:
        found = True
        if duplicate:
            reason = "duplicate ID"
        else:
            reason = "amount above threshold"
        print(transaction_id, amount, "-", reason)

if not found:
    print("No suspicious transactions")