balance = 320000
annualInterestRate = 0.2
#	Lowest Payment: 29157.09


Monthly_interest_rate = (Annual_interest_rate) / 12.0
Monthly_payment_lower_bound = Balance / 12
Monthly_payment_upper_bound = (Balance * (1 + Monthly_interest_rate)**12)	/	12

epsilon = 0.01

Updated_balance_each_month = balance

while abs(Updated_balance_each_month) > epsilon:
    minimumpayment = (lower_bound + upper_bound) / 2
    Updated_balance_each_month = balance
	while month < 13:


###############



