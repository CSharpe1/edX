# Lecture 2

# Options for programming languages
* **Low level language:**
uses instructions similar to internal control unit

* **high level language:**
uses more abstract terms – invert a matrix, compute a function

---

In a **compiled language**, those abstractions are  converted back into low level instructions, then executed

In an **interpreted language**, special program converts source code to internal data structure, then interpreter sequentially converts each step into low level machine instruction and executes

Python is an interpreted language

___

## Python programs
– Definitions evaluated and commands executed by Python interpreter in a shell

– Can be typed directly into a shell, or stored in a file that is read into the shell and evaluated

---

## Objects
* At heart, programs will manipulate data objects
* Each object has a type that defines the kinds of things programs can do to it
* Objects are:
 * Scalar (i.e. cannot be subdivided), or
 * Non-scalar (i.e. have internal structure that can be accessed)

---

# Scalar objects
* **int**
Used to represent integers, e.g., 5 or 10082

* **float**
Used to represent real numbers, e.g., 3.14 or 27.0

* **bool**
Used to represent Boolean values True and False

---

The built in Python function *type* returns the type of an object
```python
type(3)
int

type(3.0)
float
```

---

### Expressions

Objects and operators can be combined to form expressions, each of which denotes an object of some type

The syntax for most simple expressions is: <object> <operator> <object>

---

### Operators on ints and floats
* i + j
sum	– if both are ints, result is int, if either is float, result is float

* i - j
difference

* i * j
product

* i/j
division – if both are ints, result is int

* i%j
remainder

* i**j
i raised to the power of j

---

### Operator precedence
1. Parentheses define sub-computations

2.  In the absence of parentheses (within which expressions are first reduced), operators are executed left to right, first using **, then * and /, and then +
and -

---

### Comparison operators on ints and floats

* i > j
returns True if strictly greater than

* i >= j
returns True if greater than or equal

* i < j

* i <= j

* i == j
returns True if equal

* i != j
returns True if not equal

___

### Operators on bools

* **a and b**
is True if both are True

* **a or b**
is True if at least one is True

* **not a**
is True if a is False

---

### Type conversions (type casting)

We can often convert an object of one type to another, by using the name of the type as a function

```python
float(3)
3.0

int(3.9)
3

```

---

# Non-scalar objects

* We will see many different kinds of compound objects

* The simplest of these are strings, objects of type **str**

 * Literals of type string can be written using single or double quotes

---

### Operators on strings

```python
3*'a'
'aaa'

'a'+'a'
'aa'

'a'+str(3)
'a3'

len('abc')
3

```
---

### Extracting parts of strings
####Indexing:
– **‘abc’[0]** returns the string **‘a’**
– **‘abc’[2]** returns the string **‘c’**
– **‘abc’[3]** is an **error** (as we cannot go beyond the boundaries of the string)
– **‘abc’[-1]** returns the string **‘c’** (essentially counting backwards from the start of the string)

#### Slicing

– If **s** is a string, the expression **s[start:end]** denotes the substring that starts at start, and ends at end-1

```python
'abc'[1:3]
'bc'
```

---

# Programs (or scripts)

While we can type expressions directly to a Python interpreter (for example using an interface such as an IDLE shell), in general we will want to include statements in a program file

Executing an expression from a script will not produce any output; for that we need statements (not expressions), such as 

```python
print('ab')
ab

print('3'*3)
333

```

---

### Providing input

If we are going to write programs or scripts, we will need a way to incorporate input from a user.

We use the Python function **raw_input**

```python
name = raw_input('Enter your name: ')

Enter your name:

```
---

### Conditional Statements

```python
x = int(raw_input('Enter an integer: '))
if x%2 == 0:
 	print(‘’)
 	print('Even')
else:
 	print(‘’)
 	print('Odd')
print(’Done with conditional')
```