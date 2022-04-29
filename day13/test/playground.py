boxes = [3, 1, 6]
unitsPerBox = [2, 7, 4]
units = [2, 2, 2, 7, 4, 4, 4, 4, 4, 4]
truck = 6
units.sort()
test_unit = []
y = 0
for i in boxes:
    for x in range(i):
        test_unit.append(unitsPerBox[y])
    y += 1


print(test_unit)

print(sum(units[-truck:]))