print("Welcome to the tip calculator!")

bill = float(input("What was the total bill in Rs?\n"))

tip = int(input("How much tip would you like to give? 25 ,50 or 100?\n"))

people = int(input("How many people would you like to split the bill?\n"))

tip_as_percent = tip / 100

total_tip_amount = bill * tip_as_percent

total_bill = bill + total_tip_amount

bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

print(f"Each person should pay RS.{final_amount}")