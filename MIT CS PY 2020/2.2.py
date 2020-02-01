#######################################
###				Problem 2			###
#######################################

# Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. 
# By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

# In this problem, we will not be dealing with a minimum monthly payment rate.

# The following variables contain values as described below:

# balance - the outstanding balance on the credit card

# annualInterestRate - annual interest rate as a decimal

# The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:
# Lowest Payment: 180 
# Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). 
# The monthly payment must be a multiple of $10 and is the same for all months. 
# Notice that it is possible for the balance to become negative using this payment scheme, which is okay. 
# A summary of the required math is found below:

# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

# Test Case 1:

balance = 3329
annualInterestRate = 0.2

#Result Your Code Should Generate:
#Lowest Payment: 310

Month = 1
Lowest_payment = round(balance/12)
Previous_balance = balance

Monthly_interest_rate = (annualInterestRate / 12)

print("BALANCE", balance);
Check_balance = balance

W_Count1 = 1
while Check_balance > 10:
	Lowest_payment += 10
	# print("While 1: ", W_Count1);
	# print("LOWES_PAYMENT: ", Lowest_payment);
	while	Month <	13:
		Minimum_fixed_monthly_payment = Lowest_payment
		Monthly_unpaid_balance = (Previous_balance) - (Minimum_fixed_monthly_payment)
		Updated_balance_each_month = Monthly_unpaid_balance + (Monthly_interest_rate * Monthly_unpaid_balance)
		Running_total += Running_total + Updated_balance_each_month
		Month += 1
	W_Count1 += 1
	Month = 1
	Check_balance = Updated_balance_each_month

##########################################################################
monthlyinterestrate = (annualInterestRate/12)   #   calculate a montly intrest rate outside of loop
monthlyunpaidbalance = 0                           
minimumpayment = 10
updatedbalanceeachmonth = balance
resetbalance = balance                          #   set a value to reset on each iteration

            #start of program 
while  updatedbalanceeachmonth > 0:
    minimumpayment +=10                         #   Increments the search amount by 10 each time
    updatedbalanceeachmonth = resetbalance
    for i in range(1, 13):                  #Run code 12 times (1 to 13)
            balance = updatedbalanceeachmonth   #   Update the balance for new payment and interest
            monthlyunpaidbalance = balance - minimumpayment     #   balance after payment
            updatedbalanceeachmonth = monthlyunpaidbalance + (monthlyinterestrate * monthlyunpaidbalance)   #   new balance after payment and intrest
else:
    print("Lowest payment:",minimumpayment)





##########################################################################

# def Calculation (Lowest_payment):
	# while	Month <	13:
		# Minimum_fixed_monthly_payment = Lowest_payment
		# Monthly_interest_rate = (annualInterestRate / 12)
		# Monthly_unpaid_balance = (Previous_balance) - (Minimum_fixed_monthly_payment)
		# Updated_balance_each_month = (Monthly_unpaid_balance) + (Monthly_interest_rate * Monthly_unpaid_balance)
		# print("Lowest Payment: ", Lowest_payment);
		# Month += 1
	# return	Updated_balance_each_month 				#Lowest_payment



# Calculation(30)

