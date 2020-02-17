#############################
## isWordGuessed

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's'] #['a','p','l','e']		#['e', 'i', 'k', 'p', 'r', 's']


# print(isWordGuessed(secretWord, lettersGuessed));

#if lettersGuessed in secretWord:
#	print("All");
#else :
#	print("None");

##    '''
##    secretWord: string, the word the user is guessing
##    lettersGuessed: list, what letters have been guessed so far
##   returns: boolean, True if all the letters of secretWord are in lettersGuessed;
##      False otherwise
##    '''
    # FILL IN YOUR CODE HERE...
count = 0
wordLength = 0
while count < (len(secretWord)+1):
	print(count);
	if lettersGuessed[count] not in secretWord:
		print("	WRONG !!!!!	", lettersGuessed[count]);
		break
	else :# lettersGuessed[count] in secretWord:
		print("	Its in	", lettersGuessed[count]);
	# else :
		# print("	WRONG !!!!!	", lettersGuessed[count]);
		wordLength += 1
	count	+=	1
if wordLength == (len(secretWord)+1):
	print("All letters Guessed");
else:
	print("You guessed ", wordLength , "out of", len(secretWord));

print("#####################################################");
print("#####################################################");
##########################################
## getGuessedWord


secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
##		'_ pp_ e'		##


#print(secretWord, lettersGuessed);


#################################################
##			Makes the list to print showing which letters have been guessed already
print(len(secretWord));
myGuess = [] 
#print(myGuess);
myGuessLen = 0
while myGuessLen < len(secretWord):
	myGuess.append(0)
	myGuessLen	+=	1
print(myGuess);

###################################################

print("0", lettersGuessed[0]);
print("1", lettersGuessed[1]);
print("2", lettersGuessed[2]);
print("3", lettersGuessed[3]);
print("4", lettersGuessed[4]);
print("##########################################");
print("##########################################");


for x in secretWord:
	if lettersGuessed[x] in secretWord[x]	:
		print("Letter Guessed", lettersGuessed[x]);
	else:
		print("ELSE");


# x = 0
# index = 0
# for x in secretWord:
#	print(x);
	# print(secretWord[index]);
	# index	+=	1