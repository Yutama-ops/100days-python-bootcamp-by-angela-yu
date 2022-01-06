print("Welcome to the tip calculator")
total_bill = input("What was the total bill? $")
tips = input("What percentage of tip you like to give? 10, 12 or 15?")
people = input("How many people to split the bill? ")
total_bill = float(total_bill)
tips = float(tips)
people = float(people)
tip_percent_bill = total_bill * (tips / 100 )
total_bill += tip_percent_bill
each = total_bill / people
each = float(round(each, 2))
print(f"Each person should pay: ${each}")

