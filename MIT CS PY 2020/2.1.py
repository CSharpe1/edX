# Each month, a credit card statement will come with the option for you to pay a minimum amount of your charge, usually 2% of the balance due. However, the credit card company earns money by charging interest on the balance that you don't pay. 
# So even if you pay credit card payments on time, interest is still accruing on the outstanding balance.

# Say you've made a $5,000 purchase on a credit card with an 18% annual interest rate and a 2% minimum monthly payment rate.
#  If you only pay the minimum monthly amount for a year, how much is the remaining balance?

# You can think about this in the following way.

# At the beginning of month 0 (when the credit card statement arrives), assume you owe an amount we will call  b0  (b for balance; subscript 0 to indicate this is the balance at month 0).

# Any payment you make during that month is deducted from the balance. Let's call the payment you make in month 0,  p0 . Thus, your unpaid balance for month 0,  ub0 , is equal to  b0−p0 .

# ub0=b0−p0 
# At the beginning of month 1, the credit card company will charge you interest on your unpaid balance. 
# So if your annual interest rate is  r , then at the beginning of month 1, your new balance is your previous unpaid balance  ub0 , plus the interest on this unpaid balance for the month. 
# In algebra, this new balance would be

# b1=ub0+r12.0⋅ub0 
# In month 1, we will make another payment,  p1 . That payment has to cover some of the interest costs, so it does not completely go towards paying off the original charge. 
# The balance at the beginning of month 2,  b2 , can be calculated by first calculating the unpaid balance after paying  p1 , then by adding the interest accrued:

# ub1=b1−p1 
# b2=ub1+r12.0⋅ub1 
# If you choose just to pay off the minimum monthly payment each month, you will see that the compound interest will dramatically reduce your ability to lower your debt.

# Let's look at an example. 
# If you've got a $5,000 balance on a credit card with 18% annual interest rate, and the minimum monthly payment is 2% of the current balance,
# we would have the following repayment schedule if you only pay the minimum payment each month:
#	Month	Balance							Minimum Payment				Unpaid Balance					Interest
#	0		5000.00							100 (= 5000 * 0.02)			4900 (= 5000 - 100)				73.50 (= 0.18/12.0 * 4900)
#	1		4973.50 (= 4900 + 73.50)		99.47 (= 4973.50 * 0.02)	4874.03 (= 4973.50 - 99.47)		73.11 (= 0.18/12.0 * 4874.03)
#	2		4947.14 (= 4874.03 + 73.11)		98.94 (= 4947.14 * 0.02)	4848.20 (= 4947.14 - 98.94)		72.72 (= 0.18/12.0 * 4848.20)





#def MIR	(a):
	# ''' 
	# a is the annualInterestRate
	
	
	
	# '''
	
	# return monthlyInterestRate


# def	MMP	(b, pb):	
	# '''
	# b = Mim monthly payment rate
	# pb = previous balance
	# '''
	
	
	# return 


# def	MUB	(pb , mmp):
	# '''
	# pb = previous balance
	# mmp	= output from function, minimum monthly payment
	
	# '''
	
	# return


# def UBEM( MUB, MIR, MUB):
	# '''
	
	# '''

	# return









#######################################
###				Problem 1			###
#######################################


Month			=	1

# Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
   
# Result Your Code Should Generate Below:
# Remaining balance: 31.38


Previous_balance = balance



	# Monthly interest rate= (Annual interest rate) / 12.0
#Monthly_interest_rate= (annualInterestRate) / 12.0
# print("Monthly_interest_rate", round(Monthly_interest_rate,2));


	# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#Minimum_monthly_payment = (monthlyPaymentRate) * (Previous_balance)
# print("Minimum_monthly_payment", round(Minimum_monthly_payment,2));

	# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Monthly_unpaid_balance = (Previous_balance) - (Minimum_monthly_payment)
# print("Monthly_unpaid_balance", round(Monthly_unpaid_balance,2));

	# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
#Updated_balance_each_month = (Monthly_unpaid_balance) + (Monthly_interest_rate * Monthly_unpaid_balance)
# print("Updated_balance_each_month", round(Updated_balance_each_month,2));




#print("Month xx Remaining balance:", round(Updated_balance_each_month,2));


	#	Monthly interest rate= (Annual interest rate) / 12.0
Monthly_interest_rate= (annualInterestRate) / 12.0
	#	Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Minimum_monthly_payment = (monthlyPaymentRate) * (Previous_balance)
	#	Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Monthly_unpaid_balance = (Previous_balance) - (Minimum_monthly_payment)
	#	Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
Updated_balance_each_month = (Monthly_unpaid_balance) + (Monthly_interest_rate * Monthly_unpaid_balance)
print("out of loop");


while	Month <	13:

	Minimum_monthly_payment = (monthlyPaymentRate) * (Previous_balance)



	Monthly_unpaid_balance = (Previous_balance) - (Minimum_monthly_payment)


	Updated_balance_each_month = (Monthly_unpaid_balance) + (Monthly_interest_rate * Monthly_unpaid_balance)


	print("Updated", Updated_balance_each_month);


	previous_balance = Updated_balance_each_month


	print("Month xx Remaining balance:", round(Updated_balance_each_month,2));
	print("Month", Month);
	Month += 1




