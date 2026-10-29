print("ATM Transaction Sequence Simulation")

balance = int(input("Enter starting balance: "))

while balance < 0:
    print("Starting balance cannot be negative.")
    balance = int(input("Enter starting balance again: "))

number_of_transactions = int(input("Enter number of transactions: "))

deposit_count = 0
withdrawal_count = 0
rejected_count = 0

transaction_records = []

for transaction_number in range(1, number_of_transactions + 1):
    print("\nTransaction", transaction_number)
    transaction_type = input("Enter type (deposit/withdraw): ").lower()
    amount = int(input("Enter amount: "))

    if amount <= 0:
        print("Transaction rejected: amount must be greater than zero.")
        rejected_count = rejected_count + 1
        transaction_records.append((transaction_type, amount, "Rejected"))

    elif transaction_type == "deposit":
        balance = balance + amount
        deposit_count = deposit_count + 1
        print("Deposit accepted.")
        transaction_records.append((transaction_type, amount, "Accepted"))

    elif transaction_type == "withdraw":
        if amount > 10000:
            print("Transaction rejected: withdrawal is above the limit.")
            rejected_count = rejected_count + 1
            transaction_records.append((transaction_type, amount, "Rejected"))

        elif amount > balance:
            print("Transaction rejected: insufficient balance.")
            rejected_count = rejected_count + 1
            transaction_records.append((transaction_type, amount, "Rejected"))

        else:
            balance = balance - amount
            withdrawal_count = withdrawal_count + 1
            print("Withdrawal accepted.")
            transaction_records.append((transaction_type, amount, "Accepted"))

    else:
        print("Transaction rejected: unknown transaction type.")
        rejected_count = rejected_count + 1
        transaction_records.append((transaction_type, amount, "Rejected"))

print("\nTransaction Summary")
print("Starting balance transactions processed:", number_of_transactions)
print("Successful deposits:", deposit_count)
print("Successful withdrawals:", withdrawal_count)
print("Rejected transactions:", rejected_count)
print("Final balance: Rs.", balance)

print("\nTransaction Records")
for record in transaction_records:
    transaction_type, amount, status = record
    print(transaction_type, "- Rs.", amount, "-", status)