# Problem Set 1

### Part A :

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

	Number of vowels: 5
	
For problems such as these, do not include raw_input statements or define the variable s in any way. Our automated testing will provide a value of s for you - so the code you submit in the following box should assume s is already defined. If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem set.

#####  Paste your code into this box :
```python
total = 0
for c in s:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        total += 1
print "Number of vowels: " + str(total)

ALTERNATE SOLUTION
        
num = 0
for letter in s:
  if letter in "aeiou":
    num+=1
print "Number of vowels:" + str(num)
```

---

### Part B :

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

	Number of times bob occurs is: 2
	
For problems such as these, do not include raw_input statements or define the variable s in any way. Our automated testing will provide a value of s for you - so the code you submit in the following box should assume s is already defined. If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem set.

#####  Paste your code into this box :

```python
numBobs = 0
for i in range(1, len(s)-1):
    if s[i-1:i+2] == 'bob':
        numBobs += 1
print 'Number of times bob occurs is:', numBobs
```

---

### Part C - ALPHABETICAL SUBSTRINGS  :

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

	Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

	Longest substring in alphabetical order is: abc
	
For problems such as these, do not include raw_input statements or define the variable s in any way. Our automated testing will provide a value of s for you - so the code you submit in the following box should assume s is already defined. If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem set.

Note: This problem is fairly challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

#####  Paste your code into this box :

```python
curString = s[0]
longest = s[0]
for i in range(1, len(s)):
    if s[i] >= curString[-1]:
        curString += s[i]
        if len(curString) > len(longest):
            longest = curString
    else:
        curString = s[i]
print 'Longest substring in alphabetical order is:', longest
```

