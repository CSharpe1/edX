#The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). 
#The computer makes guesses, and you give it input - is its guess too high or too low? 
#Using bisection search, the computer will guess the user's secret number!

#######################
###
#Please think of a number between 0 and 100!
#Is your secret number 50?
#Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.
#######################


x = 50

step = 1

H_Limit	=	100
L_Limit	= 	1

print("Please think of a number between 0 and 100!");
print("is your number", x);
print("?");
print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.");
User_Responce = input()
while User_Responce != 'c':
	print("Is your secret number ", x);
	print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.");
	User_Responce	=	input()
	if 	User_Responce == 'l':
## 		CODE TO make the guess Larger		
		x = round((x+((H_Limit - x)/2)))
	if	User_Responce == 'h':
		print("That was too High");
## 		CODE to make the Guess Smaller
		x = round((x-((H_Limit - x)/2)))
		print("x is now", x);

		
		
	if User_Responce == 'c'	:
		print("Game over. Your secret number was: ",x);

