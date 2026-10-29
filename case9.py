print("Campus Festival Financial Audit")
count = int(input("Number of registrations: "))
fee_rate = float(input("Registration fee per participant: "))
registrations = []

for i in range(count):
    student_id = input("Participant ID: ")
    paid = float(input("Amount paid: "))
    sponsorship = float(input("Sponsorship for this record: "))
    registrations.append((student_id, paid, sponsorship))

expense_count = int(input("Number of expenses: "))
expenses = 0
for i in range(expense_count):
    expenses = expenses + float(input("Expense amount: "))

unique_ids = []
duplicates = []
fees = 0
sponsorship_total = 0

for student_id, paid, sponsorship in registrations:
    fees = fees + paid
    sponsorship_total = sponsorship_total + sponsorship
    if student_id in unique_ids:
        if student_id not in duplicates:
            duplicates.append(student_id)
    else:
        unique_ids.append(student_id)

expected_fees = len(unique_ids) * fee_rate
balance = fees + sponsorship_total - expenses

print("Unique participants:", len(unique_ids))
print("Fees collected:", fees)
print("Expected fees:", expected_fees)
print("Sponsorship:", sponsorship_total)
print("Expenses:", expenses)
print("Final balance:", balance)
print("Duplicate IDs:", duplicates)