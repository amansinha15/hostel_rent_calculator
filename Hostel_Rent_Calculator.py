## input we need from the users
#Total rent 
# Total food ordered from snacking 
# Electricity units spend 
# Charge per unit 
# Person living in the room

## Output 
# Total amount you have to pay is :


rent = int(input("Enter Your hostel/Flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spent = int(input("Enter the total of electricity spend = "))
charge_per_unit =  int (input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in room/flat = "))


total_electricty_bill = electricity_spent * charge_per_unit

output = (food + rent + total_electricty_bill) // persons

print("Each persons will pay = ", output)