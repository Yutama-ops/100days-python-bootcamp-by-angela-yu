
# Write your code here
# units = []
# y = 0
# for i in inventory:
#     for x in range(i):
#         units.append(unitsPerBox[y])
#     y += 1
# units.sort()
# total_unit = sum(units[-order:])
x = []
inventory = [2, 8, 4, 10, 6]
order = 20
result = 110
r = [10, 9, 8, 8, 7, 7, 6, 6, 6, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]
max_item = max(inventory)
z = 0
for i in range(order):
    if len(x) < order:
        if i%2 == 0:
            z += 1
        for y in range(z):
            x.append(max_item)
        max_item -= 1

print(sum(x))



print(x)
print(sum(r))

print(len(r))