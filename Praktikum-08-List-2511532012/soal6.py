LAST_DIGIT = 0  # Ganti dengan digit terakhir NIM
daily_limit = 30000 + LAST_DIGIT * 1000

expenses = []

for i in range(1, 8):
    pengeluaran = int(input(f"Day {i}: "))
    expenses.append(pengeluaran)

total = sum(expenses)
average = total / 7
highest = expenses.index(max(expenses)) + 1

days_above_limit = 0

for expense in expenses:
    if expense > daily_limit:
        days_above_limit += 1

print("Daily limit:", daily_limit)
print("Total:", total)
print("Average:", format(average, ".1f"))
print("Highest: Day", highest)
print("Days above limit:", days_above_limit)