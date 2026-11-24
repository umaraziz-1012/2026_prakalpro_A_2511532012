temperatures = [-3, -1, -5, -2, -4, -1, -6]
highest = temperatures[0]
lowest = temperatures[0]
for i in range(1, len(temperatures) + 1):
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i
print("Highest:", highest)
print("Lowest:", lowest)
