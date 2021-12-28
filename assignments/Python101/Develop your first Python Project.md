# TASK #1: UNDERSTAND VARIABLES ASSIGNMENT


```python
# Define a variable named "x" and assign a number (integer) to it
# integer is a whole number (no decimals) that could be positive or negative
x = 10

```


```python
# Let's view "x"
print(x)
```

    10
    


```python
# Define a variable named "y" and assign a number (float) to it
# Float are real numbers with a decimal point dividing the integer and fractional parts
y = 12.34

```


```python
# Let's view "y"
print(y)
```

    12.34
    


```python
# Let's overwrite "y" (assume your portfolio value increased)
y = 58.26
```


```python
# Notice that "y" will only contain the most recent value
print(y)
```

    58.26
    


```python
# Get the type of "x" which is integer
# integer is a whole number (no decimals) that could be positive or negative
print(type(x))
```

    <class 'int'>
    


```python
# Get the type of "y" which is float
# Float are real numbers with a decimal point dividing the integer and fractional parts
print(type(y))
```

    <class 'float'>
    

MINI CHALLENGE #1:
- We defined a variable x and we assigned these 4 values listed below to it. Without executing any code cells, what will these lines of code generate?
- Verify your answer by executing the code cells



```
z = 1000
z = 2000
z = 5000
z = 6000
z
```



```python
z = 1000
z = 2000
z = 5000
z = 6000
z
```




    6000



# TASK #2: PERFORM MATH OPERATIONS IN PYTHON


```python
# Define a variable named i and initialize it with 20 
# Let's assume that we want to increment the value by 4 
i = 20
i += 4
print(i)
```

    24
    


```python
# Let's assume that you own a little grocery store 
# The price of 1 bottle of milk is $3 and we currently have 50 bottles
# We can calculate the total dollar value of our inventory as follows:
price = 3
bottles = 50
inventory_price = price * bottles
print(inventory_price)
```

    150
    


```python
# Let's assume you have $550 USD in our bank account
# We want to buy x number of IBM stocks using the total amount 
# each IBM stock is priced at $128 each
balance = 550
stock_price = 128
def buy(bal,prc):
    return bal // prc
print(buy(balance,stock_price))

```

    4
    


```python
# Divide the account balance by Amazon stock price and place the answer in units
print(buy(balance,3396))
```

    0
    

MINI CHALLENGE #2:
- Write a code that takes in APPLE (AAPL) stock prices at two days and calculate the return:
  - AAPL price on day 1 = \$135
  - AAPL price on day 2 = \$150



```python
def profit(day1, day2):
    diff = day2 - day1
    perc = diff / day1 * 100
    return perc
print(profit(135,150))
print(profit(150,146))
```

    11.11111111111111
    -2.666666666666667
    

# TASK #3: UNDERSTAND PRINT AND INPUT OPERATIONS


```python
# Print function is used to print elements on the screen
# Define a string x 
# A string in Python is a sequence of characters
# String in python are surrounded by single or double quotation marks
x = "Hello world!"
print(x)
```

    Hello world!
    


```python

```


```python
# Obtain the data type for 'x'
print(type(x))
```

    <class 'str'>
    


```python
# The format() method formats the specified value and insert it in the placeholder
# The placeholder is defined using curly braces: {}
print("I wrote: {}".format(x))
print(f"I wrote: {x}")
```

    I wrote: Hello world!
    I wrote: Hello world!
    


```python
# input is a built-in function in python
# Obtain client data such as name, country and e-mail and print them all out on the screen
input("WHAT?!?")
```

    WHAT?!?lolz
    




    'lolz'



MINI CHALLENGE #3:
- Write a code that takes in the name of the stock, price at which it is selling, the number of stocks that you want to own and prints out the total funds required to buy this stock. Find a sample expected output below:
  - Enter the price of the stock you want to buy: 3000  
  - Enter the number of stocks that you want to buy: 5
  - Enter the name of the stock that you want to buy: AMZN
  - The total funds required to buy 5 number of AMZN stocks at 3000 is: 15000



```python
name = input("Name of the stock: ")
price = input("Selling price: ")
amount = input("Number of stocks: ")
output = f"The total funds required to buy {amount} number of {name} stocks at {price} is: {int(amount) * int(price)}"
print(output)

```

    Name of the stock: AMZN
    Selling price: 3000
    Number of stocks: 5
    The total funds required to buy 5 number of AMZN stocks at 3000 is: 15000
    

# TASK #4: UNDERSTAND LISTS DATA TYPES


```python
# A list is a collection which is ordered and changeable. 
# List allows duplicate members.
lst = ["xmas", "nye", "eastern", "independence day"]
```


```python
# Obtain the datatype
print(type(lst))
```

    <class 'list'>
    


```python
# Access specific elements in the list with Indexing
# Note that the first element in the list has an index of 0 (little confusing but you'll get used to it!)
print(lst[3]) 
```

    independence day
    

MINI CHALLENGE #4:
- Print the first, second and last element in the list below

```
grocery_list = ['milk', 'rice', 'eggs', 'bread', 'oranges', 'water']

```




```python
grocery_list = ['milk', 'rice', 'eggs', 'bread', 'oranges', 'water']
print(grocery_list[0], grocery_list[1], grocery_list[len(grocery_list)-1])
```

    milk rice water
    

# TASK #5: UNDERSTAND COMPARISON OPERATORS AND CONDITIONAL STATEMENTS


```python
# Comparison Operator output could be "True" or "False"
# Let's cover equal '==' comparison operator first
# It's simply a question: "Is x equals y or not?"
# "True" output means condition is satisfied 
# "False" output means Condition is not satisfied (condition is not true) 
x = 5
y = 6
if x == y:
    print("True :)")
else:
    print("False :(")
```

    False :(
    


```python
# Greater than or equal operator '>='
x = 7
y = 6
if x >= y:
    print("True :)")
else:
    print("False :(")

```

    True :)
    


```python
# Note that '==' is a comparison operator 
# Note that '=' is used for variable assignment (put 10 in x)
x = 10
x == 10
```




    True




```python

```

- A simple if-else statement is written in Python as follows:

```
if condition:
  statement #1
else:
  statement #2
```

- If the condition is true, execute the first indented statement
- if the condition is not true, then execute the else indented statements. 
- Note that Python uses indentation (whitespace) to indicate code sections and scope.


```python
# Let's take an input from the user and grant or deny access accordingly
secret = "welcome1234"
pwd = input("Enter password: ")
if pwd == secret:
    print("access granted")
else:
    print("access denied")
```

    Enter password: welcome1234
    access granted
    

MINI CHALLENGE #5:
- Write a code that takes a number from the user and indicates if it's positive or negative


```python
nbr = input("Give a number: ")
if int(nbr) < 0:
    print(f"Number {nbr} is negative")
else:
    print(f"Number {nbr} is positive")
```

    Give a number: -3
    Number -3 is negative
    


```python
def oddeven(x):
    if x % 2 == 0:
        print(f"Number {x} is even")
    else:
        print(f"Number {x} is odd")

oddeven(7)
oddeven(180)
```

    Number 7 is odd
    Number 180 is even
    

# TASK #6: DEVELOP FUNCTIONS IN PYTHON


```python
# Define a function that takes in two argument x and y and returns their multiplication 
def multiply(x, y):
    return x * y
```


```python
# Call the function
print(multiply(5, 4))
```

    20
    

MINI CHALLENGE #6:
- Write a code that takes in three inputs from the user and calculate their sum


```python
def sum3(x, y, z):
    lst = [x, y, z]
    return sum(lst)

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
outcome = sum3(num1, num2, num3)
print(outcome)
```

    Enter 1st number: 4
    Enter 2nd number: 4
    Enter 3rd number: 10
    18
    

# TASK #7: UNDERSTAND FOR AND WHILE LOOPS


```python
# List of strings
lst = ["While", "loop", "can", "be", "used", "to", "execute", "a", "set", "of", "statements", "as", "long", "as", "a", "certain", "condition", "holds", "true"]
```


```python
print(" ".join(lst))
for i in lst:
    print(i)
```

    While loop can be used to execute a set of statements as long as a certain condition holds true
    While
    loop
    can
    be
    used
    to
    execute
    a
    set
    of
    statements
    as
    long
    as
    a
    certain
    condition
    holds
    true
    


```python
# Range() generates a list of numbers, which is used to iterate over with for loops.
# range() is 0-index based, meaning list indexes start at 0, not 1. 
# The last integer generated by range() is up to, but not including, last element. 
# Example: range(0, 7) generates integers from 0 up to, but not including, 7.
for i in range(5, len(lst)):
    print(lst[i])
```

    to
    execute
    a
    set
    of
    statements
    as
    long
    as
    a
    certain
    condition
    holds
    true
    


```python
# While loop can be used to execute a set of statements as long as a certain condition holds true.

```

MINI CHALLENGE #7:
- Write a code that displays numbers from 1 to 10 using for and while loops



```python
for i in range(1, 11):
    print(i)

i = 1
while i <= 10:
    print(i)
    i += 1
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    

# TASK #8: CAPSTONE PROJECT

Develop a guessing game that performs the following: 
- The system will automatically generate a random number between 1 and 100. 
- Users can insert any number between 1 and 100
- The program shall be able to compare the number generated by the system and the number that has been entered by the user. The program shall print out one of the following options to help the user improve their next guess:
    - You are right, great job!
    - Your guess is low, try again!
    - your guess is high, try again!

- The program exits when the user guess matches the number generated by the system




```python
from random import randrange
random_nbr = randrange(1,101)
user_nbr = -1
while True:
    user_nbr = input("Enter a number between 1 and 100: ")
    if user_nbr in ["stop", "abort", "cancel", "stop", "quit", "exit"]:
        print(f"The secret number was {random_nbr}")
        break
    else:
        try:
            user_nbr = int(user_nbr)
        except:
            print("ERROR: Please enter a valid number betwee n1 and 100")
            continue
    if user_nbr == random_nbr:
        print("You are right, great job!")
        break
    elif user_nbr < random_nbr:
        print("Your guess is too low, try again!")
    else:
        print("your guess is too high, try again!")
```

    Enter a number between 1 and 100: 4
    Your guess is too low, try again!
    Enter a number between 1 and 100: stop
    The secret number was 8
    


```python

```


```python

```


```python

```


```python

```

# EXCELLENT JOB

# MINI CHALLENGES SOLUTIONS

MINI CHALLENGE #1 SOLUTION:
- We defined a variable x and we assigned these 4 values listed below to it. Without executing any code cells, what will these lines of code generate?
- Verify your answer by executing the code cells

```
z = 1000
z = 2000
z = 5000
z = 6000
z
```


```python
# The output of this code is 5000
# Initially we put 1000 in z, then we overwrite it by placing 2000 in z, and then 5000 in z & finally 6000 in z
z = 1000
z = 2000
z = 5000
z = 6000
z
```

MINI CHALLENGE #2 SOLUTION:
- Write a code that takes in APPLE (AAPL) stock prices at two days and calculate the return:
  - AAPL price on day 1 = \$135
  - AAPL price on day 2 = \$150



```python
AAPL_price_1 = 135
AAPL_price_2 = 150

price_diff = AAPL_price_2 - AAPL_price_1
percentage_change = price_diff / AAPL_price_1 * 100

percentage_change
```

MINI CHALLENGE #3 SOLUTION:
- Write a code that takes in the name of the stock, price at which it is selling, the number of stocks that you want to own and prints out the total funds required to buy this stock. Find a sample expected output below:
  - Enter the price of the stock you want to buy: 3000  
  - Enter the number of stocks that you want to buy: 5
  - Enter the name of the stock that you want to buy: AMZN
  - The total funds required to buy 5 number of AMZN stocks at 3000 is: 15000


```python
x = input("Enter the price of the stock you want to buy: ")
x = int(x)
y = input("Enter the number of stocks that you want to buy: ")
y = int(y)
z = input("Enter the name of the stock that you want to buy: ")
print('The total funds required to buy {} number of {} stocks at {} is {}'.format(y,z,x, x*y)) 
```

MINI CHALLENGE #4 SOLUTION:
- Print the first, second and last element in the list below

```
grocery_list = ['milk', 'rice', 'eggs', 'bread', 'oranges', 'water']

```



```python
grocery_list = ['milk', 'rice', 'eggs', 'bread', 'oranges', 'water']
print(grocery_list[0])
print(grocery_list[1])
print(grocery_list[-1])
```

MINI CHALLENGE #5 SOLUTION:
- Write a code that takes a number from the user and indicates if it's positive or negative


```python
x = int(input("Please enter an integer: "))

if x < 0:
    print('Number is Negative')
elif x > 0:
    print('Number is Positive')
else:    
    print ('Number is zero')
```

MINI CHALLENGE #6 SOLUTION:
- Write a code that takes in three inputs from the user and calculate their sum


```python
def summation(x, y, z):
    return x + y + z
```


```python
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

total = summation(num1, num2, num3)

print('Total balance = {}'.format(total))
```

MINI CHALLENGE #7 SOLUTION:
- Write a code that displays numbers from 1 to 10 using for and while loops


```python
i = 1
while (i < 11):
  print (i)
  i = i+1
```


```python
for i in range(1, 11):
    print(i)
```


```python

```
