# We can use the idea of bisection search to determine if a character is in a string, 
# so long as the string is sorted in alphabetical order.

# First, test the middle character of a string against the character you're looking for (the "test character"). 
# If they are the same, we are done - we've found the character we're looking for!

# If they're not the same, check if the test character is "smaller" than the middle character.
# If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string.
# (Note that you can compare characters using Python's < function.)

# Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr.
# char will be a single character and aStr will be a string that is in alphabetical order.
# The function should return a boolean value.

# As you design the function, think very carefully about what the base cases should be.

#def isIn(char, aStr):
#    '''
    # char: a single character
    # aStr: an alphabetized string
    
    # returns: True if char is in aStr; False otherwise
#    '''
#    # Your code here

Test = 'e'
aStr = "abcdefghij"

if aStr	==	' ':
	return False
if len(aStr) == 1:
	return aStr == char
midIndex	=	len(aStr)//2
midChar		=	aStr[minIndex]
if	char	== minChar	:
	return True
elif char < midChar:
    return isIn(char, aStr[:midIndex])
else:
    return isIn(char, aStr[midIndex+1:])
  
   
#######################################

# if Test == aStr[((len(aStr)//2)-1)]:	# Test Character
	# print("IS");
# else:
	# print("Check if the test character is smalled than the middle character");
	# if Test < aStr[((len(aStr)//2)-1)]:
		# print("Test character is smaller than the middle of aStr!");
	# elif Test > aStr[((len(aStr)//2)-1)]:
		# print("It is bigger!!!");
	# else :
		# print("Else");
	
	


