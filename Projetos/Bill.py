# Project of the day (day 02) - Bill Calculator

print("Welcome to the tip calculator")
count = input("What was the total bill? $")
payment = input(
    "What the percentage tip would you like to give? 10, 12 or 15? ")
pay = (float(count) * (float(payment)/100)) + float(count)
people = input("How many people to split the bill? ")
each = pay / int(people)

print(f"Each person should pay: ${round(each, 2)}")
