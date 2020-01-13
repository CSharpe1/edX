#Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment
# required by the credit card company each month.

#The following variables contain values as described below:
#    balance - the outstanding balance on the credit card
#    annualInterestRate - annual interest rate as a decimal
#    monthlyPaymentRate - minimum monthly payment rate as a decimal
#For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months,
# print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy

#A summary of the required math is found below:
#   Monthly interest rate= (Annual interest rate) / 12.0
#   Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#   Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#   Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

#Test value;
balance = 42;
annualInterestRate = 0.2;
monthlyPaymentRate = 0.04

# My code here
for i in range(1, 13):                  #Run code 12 times (1 to 13)
    minimumpayment = balance * monthlyPaymentRate
    unpaidbalance = balance - minimumpayment
    intrest = (annualInterestRate/12)*unpaidbalance
    balance = (unpaidbalance+intrest)
 #   print(round(balance,2))
   # break
print("Remaining balance: ", round(balance,2))
