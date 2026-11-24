menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []

for day in range(number_of_days):
    daily_sales = []

    for menu in menus:
        porsi = int(input(f"Day {day + 1}, {menu}: "))
        daily_sales.append(porsi)

    sales.append(daily_sales)

print("\nTotal per day:")

for day in range(number_of_days):
    total = sum(sales[day])
    print(f"Day {day + 1}: {total}")

menu_totals = []

for col in range(len(menus)):
    total = 0

    for row in range(number_of_days):
        total += sales[row][col]

    menu_totals.append((menus[col], total))

print("\nTotal per menu:", menu_totals)

best_name = ""
best_total = 0

for name, total in menu_totals:
    if total > best_total:
        best_name = name
        best_total = total

print(f"Best seller: {best_name} ({best_total})")
