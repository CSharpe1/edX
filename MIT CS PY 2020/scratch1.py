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


import math

def polysum(n, s):
	'''
	n and s are int
	return: Sum of area and square of polygon.
	'''
	Area_Polygon = 	(0.25	*	n*	s**2)	/	(math.tan(math.pi/n))
	Perimeter = ((s*n)**2)
	Sum = Area_Polygon+Perimeter
	return print(round(Sum,4));
	
	
	
	




