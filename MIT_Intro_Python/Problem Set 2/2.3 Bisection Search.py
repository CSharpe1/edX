### PROBLEM 3: USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER (25/25 points)

#You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time each submission is allowed, so your observations from running this experiment on the grading system might be limited to an error message complaining about too much time taken.)
#Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!
#The following variables contain values as described below:
#   1. **balance** - the outstanding balance on the credit card
#   2. **annualInterestRate** - annual interest rate as a decimal
#To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year. What is a reasonable lower bound for this payment value? $0 is the obvious anwer, but you can do better than that. If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every month. One-twelfth of the original balance is a good lower bound.
#What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. What we ultimately pay must be greater than what we would've paid in monthly installments, because the interest was compounded on the balance we didn't pay off each month. So a good upper bound for the monthly payment would be one-twelfth of the balance, after having its interest compounded monthly for an entire year.
#![](./img/01.png)
#Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.
#Note that if you do not use bisection search, your code will not run - your code only has 30 seconds to run on our servers.
####################
balance = 130020
annualInterestRate = 0.12
####################

nb = balance
minpay = 10
month_intrest = (annualInterestRate / 12)   #   calculate a montly intrest rate outside of loop
lower_bound = balance/12
upper_bound = (balance * ((1 + month_intrest) ** 12) / 12.0)          #(balance*(1+montly intrest rate)^12)/12

while abs(nb) > 0.1:
    minpay = (lower_bound + upper_bound) / 2
    nb = balance
    for month in range(12):
        monthlyUnpaid = nb - minpay
        nb = monthlyUnpaid + (month_intrest * monthlyUnpaid)
        print('for',nb)
    if nb > 0.1:
        print('>',nb)
        lower_bound = minpay
    elif nb < 0.1:
        print('<',nb)
        upper_bound = minpay
print ("Lowest Payment: ", round(minpay, 2))



