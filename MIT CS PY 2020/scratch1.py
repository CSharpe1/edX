# x = 25
# epsilon = 0.01
# step = 0.1
# guess = 0.0

# while guess <= x:
    # if abs(guess**2 -x) < epsilon:
        # break
    # else:
        # guess += step

# if abs(guess**2 - x) >= epsilon:
    # print('failed')
# else:
    # print('succeeded: ' + str(guess))



	
# def square(x):
    # '''
    # x: int or float.
    # '''
#    #Your code here
    # return x**2
	
	
# def evalQuadratic(a, b, c, x):
    # '''
    # a, b, c: numerical values for the coefficients of a quadratic equation
    # x: numerical value at which to evaluate the quadratic.
    # '''
#    #Your code here     
    # return a*x**2+b*x+c

# def fourthPower(x):
    # '''
    # x: int or float.
    # '''
#    #Your code here
    # return square(square(x))
	
# x = 8
# print(bool(x%2));		# 0 if even, 1 if odd

#########################################################################
##### week 2, 4 Functions, Ex Power iter				COME BACK TOO   #
#########################################################################

   # conter = 0
    # score = base
    # if conter != exp:
        # conter += 1
        # score * base
    
    
    # return score








# import math

# n = 2
# s = 3
# Perimeter = 0


# This gives me the area of the polygon
# Area_Polygon = 	(0.25	*	n*	s**2)	/	(math.tan(math.pi/n))
# print("Area of Regular polygon", round(Area_Polygon,4));

# Perimeter = s*n


# sum = Area_Polygon + Perimeter

# print(round(sum,4));








# A regular polygon has n number of sides. Each side has length s.

# The area of a regular polygon is:  0.25*n*(s**2) / tan(π/n) 

# The perimeter of a polygon is: length of the boundary of the polygon

# Write a function called polysum that takes 2 arguments, n and s. 
# This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.


# import math

# def polysum(n, s):
	# '''
	# n and s are int
	# return: Sum of area and square of polygon.
	# '''
	# Area_Polygon = 	(0.25	*	n*	s**2)	/	(math.tan(math.pi/n))
	# Perimeter = ((s*n)**2)
	# Sum = Area_Polygon+Perimeter
	# return print(round(Sum,4));


####	
# a = 2
# b = 12
	
# t = 0
# while a != b:
	# t = b
	# b = (a%b)	
	# print( b);

# def gcdRecur(a,b)
    # if b == 0:
        # return a   
    # else:
        # return gcdRecur(b, a%b)

############




# def recurPower(base, exp):
    # '''
    # base: int or float.
    # exp: int >= 0
 
    # returns: int or float, base^exp
    # '''
    # if exp <= 0:
        # return 1
    # else :    
	    # return base * recurPower (base, exp -1)
 

#############
# n = 21

# if n == 2 or n == 4 or (n >= 20 and n&1 == False):
    # print("Not Weird");
# else    :
    # print("Weird") ;


###############
# Exercise: gcd iter
# 0.0/5.0 points (graded)
# ESTIMATED TIME TO COMPLETE: 5 minutes

# The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

# gcd(2, 12) = 2

# gcd(6, 12) = 6

# gcd(9, 12) = 3

# gcd(17, 12) = 1

# Write an iterative function, gcdIter(a, b), that implements this idea. One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either reach a case where the test divides both a and b without remainder, or you reach 1.


# Exercise: is in
# 0.0/5.0 points (graded)
# ESTIMATED TIME TO COMPLETE: 18 minutes

# We can use the idea of bisection search to determine if a character is in a string, so long as the string is sorted in alphabetical order.
# First, test the middle character of a string against the character you're looking for (the "test character").
# If they are the same, we are done - we've found the character we're looking for!
# If they're not the same, check if the test character is "smaller" than the middle character. 
# If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string. 
# (Note that you can compare characters using Python's < function.)
# Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr. 
# char will be a single character and aStr will be a string that is in alphabetical order. 
# The function should return a boolean value.
# As you design the function, think very carefully about what the base cases should be.


# year = 2020

# if year / 4 == True:
    # print("Not divide by 4", year);
# elif year / 4 == False:
    # print("divide 4 is false", year);
# elif (year // 4) == True and (year // 400) == True:
    # print("400", year);
# else	:
	# print("else", year);

#print(year % 4 == 0 and (year % 400 == 0 or year % 100 != 0));

# n = 15

# count = 0
# while count <= n:
    # print(count, end='');
    # count += 1
# print(n);



# if (1 >= 0):
   # return "Spam"
# if (n in range (6, 21) or n % 2 != 0):
    # return "Weird"
# else:
        # return "Weird"

# n = 3

# if n == 2 or n == 4 or (n >= 20 and n&1 == False):
    # print("Not Weird");
# else    :
    # print("Weird") ;
	
# x = 1
# y = 2
# z = 2
# n = 2


# for a in range (0, x + 1 ) : 
	# print("X", a);
# for b in range( 0, y + 1): 
	# print("Y", b);
# for c in range( 0, z + 1): 
	# print("Z", c);
# print(a,b,c);
# if a + b + c !=n: 
	# print([a,b,k])
	
	
	

# TT = ('I', 'am', 'a', 'test', 'tuple')
# print(TT[::2]);
	

# def oddTuples(aTup):
#    '''
 #   aTup: a tuple
    
 #   returns: tuple, every other element of aTup. 
 #   '''
    # a placeholder to gather our response
    # rTup = ()
    # index = 0

    # Idea: Iterate over the elements in aTup, counting by 2
     # (every other element) and adding that element to 
     # the result
    # while index < len(aTup):
        # rTup += (aTup[index],)
        # index += 2

    # return rTup

# def oddTuples2(aTup):
#    '''
#    Another way to solve the problem.
# 
#    aTup: a tuple
#     
#    returns: tuple, every other element of aTup. 
#    '''
    # Here is another solution to the problem that uses tuple 
     # slicing by 2 to achieve the same result
    # return aTup[::2]

x = 0
testList = [1, -4, 8, -9]
print(len(testList));
while x < len(testList):
	print(abs(testList[x]));
	x += 1
	
	
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
		
		
def inc(a):
    return a+1
applyToEach(testList, inc)




animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati', 'afaaf', 'afcacac']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(animals);


print("#####################################################");
aDict = {'B': [15], 'u': [10, 15, 5, 2, 6]}


count = 0

for x in aDict.values():
#	print(x);
#	print(len(x));
	count += len(x);
print("count", count);


print("#####################################################");
aDict = {'B': [15], 'u': [10, 15, 5, 2, 6], 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati', 'afaaf', 'afcacac']}

count = 0
for x in aDict.values():
#	print(x);
#	print(len(x));
	count += len(x);

print("count", count);

print(sorted(aDict));
