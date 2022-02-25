
item = [1, 2, 3]
new_list = [n+1 for n in item]
print(new_list)
name = "Yutama"
new_name = [n + 1 for n in name]
new_name = [n + "ame" for n in name]
print(new_name)
new_range = [n * 2 for n in range(1, 5)]
print(new_range)
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_name = [letter for letter in names if len(letter) < 5]
print(short_name)
cappitol = [letter.upper() for letter in names if len(letter) > 5]