# Get the loan details
money_owed = float(input("How much do you owe, in dollars\n"))
apr = float(input("What is the annual percentage rate\n"))
payment = float(input("What will your monthly payment be, in dollars\n"))
months= int(input("How many months do you want to see reseult for\n"))

monthly_rate = apr/100/12

interest_paid = money_owed * monthly_rate
money_owed = money_owed + interest_paid

money_owed = money_owed - payment

print("Paid", payment, "of which", interest_paid, "was interest", end='')
print("Now i owe", money_owed)