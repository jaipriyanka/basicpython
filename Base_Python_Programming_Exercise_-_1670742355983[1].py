#!/usr/bin/env python
# coding: utf-8

# ## Python Basic Programming Exercises
Q1: What is the output of following expression
    5 + 4 * 9 % (3 + 1) / 6 - 15 + 4 * 9 % (3 + 1) / 6 - 1
5 + 4 * 9 % 4 / 6 - 1
5 + 36 % 4 / 6 - 1
5 + 0 / 6 - 1
5 + 0.0 - 1
5.0 - 1
4.0
# In[1]:


5 + 4 * 9 % (3 + 1) / 6 - 1


# In[2]:


5 + 4 * 9 % (3 + 1) // 6 - 1

Q2: Write a program to check if a Number is Odd or Even. Take number as a input from user at runtime.
# In[4]:


num = int( input("Enter a number: "))
print("Number: ", num)

if num % 2 == 0 :
    print(num, "is Even!")
else:
    print(num, "is Odd!")    


# In[5]:


num=int(input("Enter a number:"))
print("Number:",num)

if num % 2==0:
    print(num,"is Even!")
else:
    print(num,"is odd!")

Q3: Write a program to display the multiplication table by taking a number as input. 
    [Hint : Use print statement inside of a loop]
# In[6]:


num = int(input("Enter the number: "))

for i in range(1, 11, 1):
    print(num, " * ", i, " = " , num * i )           # 5 * 1 = 5


# In[9]:


num = int(input("enter the number:"))

for i in range(1,21,1):
    print(num,"^",i,"=",num^i)

Q4: Write a program which will find all numbers between 2000 and 3200 which are divisible by 7 
    but are not a multiple of 5.
 
Note: The numbers obtained should be printed in a comma-separated sequence on a single line.
# In[9]:


for i in range( 2000, 3201, 1):
    if ( i % 7 == 0) and (i % 5 != 0) :
        print(i, end = ',')


# In[12]:


for i in range (2000,3201,1):
    if (i %7 ==0) and(i%5!=0):
        print(i,end=',')

Q5: Count the elements of each datatype inside the list and display in output
    [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7]    
    
# In[6]:


l = [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7]    
print(l)

c_int = 0
c_float = 0
c_str = 0
c_bool = 0
c_none = 0

for i in l:
    if type(i) == int:
        c_int = c_int +1
    elif type(i) == float:
        c_float = c_float +1 
    elif type(i) == str:
        c_str = c_str +1
    elif type(i) == bool:
        c_bool = c_bool +1
    else:
        c_none = c_none +1
        
        
print("int: ", c_int)
print("float: ", c_float)
print("str: ", c_str)
print("bool: ", c_bool)
print("none: ", c_none)

Q6: Add all values from the list with numeric datatypes 
    [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7] 
# In[15]:


li = [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7] 
print(li)

sum = 0

for i in li:
    if type(i) == int or type(i) == float:
        sum =  sum + i
print("Sum of numeric elements = ", sum)        

Q7: Concat all str datatypes with hyphen as a delimiter
    [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7] 
    
hint: '-'.join()  #Py-SQL-John
# In[17]:


l1=[2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7] 
l1

l2=[]
for i in l1:
    if type(i) == str:
       l2.append(i)
    
print(l1)+

print('-'.join(l2))

Q8: Write a UDF that takes list as input and returns sum of all numbers 
    (exclude bool) and count of all str 
    [2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7] 
    
Hint:
-----
def my_func:
    # your code
        
my_func(l1)
# output --> {'Sum': xxx, 'Count_of_Strs': xxx}
# In[19]:


l5=[2, 3, 'Py', '10', 1, 'SQL', 5.5, True, 3, 'John', None, 7] 
l5

Q9: Get only odd numbers from the following list and store the numbers in new list
    li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

    i. Use loops to get the answer
   ii. Use list comprehensions
  iii. Use lambda function with filter
# In[5]:


##Use loops to get the answer
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
odd_numbers = []

for num in li:
    if num % 2 != 0:
        odd_numbers.append(num)

print(odd_numbers)


###Use list comprehensions
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
odd_numbers = [num for num in li if num % 2 != 0]

print(odd_numbers)

##Use lambda function with filter

li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
odd_numbers = list(filter(lambda num: num % 2 != 0, li))

print(odd_numbers)


Q10: Write a UDF to return the descriptives [sum, count, min, mean, max] for a list of n number of input numbers.
# In[7]:


def calculate_descriptives(numbers):
    # Calculate sum
    total_sum = sum(numbers)

    # Calculate count
    count = len(numbers)

    # Calculate minimum value
    minimum = min(numbers)

    # Calculate mean
    mean = total_sum / count

    # Calculate maximum value
    maximum = max(numbers)

    # Return the results as a dictionary
    return {
        "sum": total_sum,
        "count": count,
        "min": minimum,
        "mean": mean,
        "max": maximum
    }

# Example usage:
input_numbers = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
descriptives = calculate_descriptives(input_numbers)
print(descriptives)

Q11: Write an udf to calculate the area of different shapes

Take shape and dimensions as arguments to udf as follows : 

1. square which has side
2. rectangle which has length and width
3. circle which has radius

The shape should be a positional argument and it's dimensions are taken as kwargs

Perform proper validation for the user inputs and then calculate area.

E.g. if shape is square, ensure kwargs has "side" and if so, then you may return the area, else display appropriate error message like "Please enter 'side' for a square"
# In[19]:


import math

def calculate_area(shape, **kwargs):
    if shape == "square":
        if "side" in kwargs:
            side = kwargs["side"]
            if side > 0:
                area = side ** 2
                return area
            else:
                return "Side length should be a positive number."
        else:
            return "Please enter 'side' for a square."
    elif shape == "rectangle":
        if "length" in kwargs and "width" in kwargs:
            length = kwargs["length"]
            width = kwargs["width"]
            if length > 0 and width > 0:
                area = length * width
                return area
            else:
                return "Length and width should be positive numbers."
        else:
            return "Please enter 'length' and 'width' for a rectangle."
    elif shape == "circle":
        if "radius" in kwargs:
            radius = kwargs["radius"]
            if radius > 0:
                area = math.pi * radius ** 2
                return area
            else:
                return "Radius should be a positive number."
        else:
            return "Please enter 'radius' for a circle."
    else:
        return "Unsupported shape. Valid shapes are: square, rectangle, circle."

 ##example usage
square_area = calculate_area("square", side=5)
print("Square area:", square_area)

rectangle_area = calculate_area("rectangle", length=4, width=6)
print("Rectangle area:", rectangle_area)

circle_area = calculate_area("circle", radius=3)
print("Circle area:", circle_area)

Q12: Write a UDF to reconcile the values within two lists.
    l1 = ['January', 'February', 'March', 'May', 'June', 'September', 'December']
    l2 = ['January', 'February', 'April', 'June', 'October', 'December']

Hint:
-----
def func(l1, l2):
    your code here...
    
Output:
{'Matched': ['January', 'February', 'June', 'December'],
    'Only in l1': ['March', 'May', 'September'],
        'Only in l2': ['April', 'October']}
# In[20]:


def reconcile_lists(l1, l2):
    result = {}
    result['Matched'] = list(set(l1) & set(l2))
    result['Only in l1'] = list(set(l1) - set(l2))
    result['Only in l2'] = list(set(l2) - set(l1))
    return result

# Example usage:
l1 = ['January', 'February', 'March', 'May', 'June', 'September', 'December']
l2 = ['January', 'February', 'April', 'June', 'October', 'December']

reconciliation_result = reconcile_lists(l1, l2)
print(reconciliation_result)

Q13: write a UDF to check if a number is prime or not.
# In[21]:


def is_prime(number):
    if number <= 1:
        return False

    # Check for divisibility from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

# Example usage:
num = 17
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

Q14. Write a program which can compute the factorial of a given numbers. 
#   The results should be printed in a comma-separated sequence on a single line. 
# input() function can be used for getting user(console) input


#Suppose the input is supplied to the program:  8  
#Then, the output should be:  40320 
#Hints: In case of input data being supplied to the question, it should be assumed to be a console input. 

# In[23]:


def factorial(number):
    if number < 0:
        return "Factorial is undefined for negative numbers."
    elif number == 0:
        return 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

# Example usage:
number = int(input("Enter a number: "))
result = factorial(number)
print(result)

Q15. With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

#Suppose the following input is supplied to the program: 8
#Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Consider using dict()


# In[28]:


def generate_squared_dict(n):
    squared_dict = {}

    for i in range(1, n + 1):
        squared_dict[i] = i * i

    return squared_dict

# Example usage:
n = int(input("Enter a number: "))
result = generate_squared_dict(n)
print(result)

Q16. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program: 34,67,55,33,12,98
    #Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

#Hints: In case of input data being supplied to the question, it should be assumed to be a console input. you may use tuple() method to convert list to tuple

# In[29]:


def generate_list_and_tuple(numbers):
    number_list = numbers.split(',')
    number_tuple = tuple(number_list)
    return number_list, number_tuple

# Example usage:
numbers_input = input("Enter a sequence of comma-separated numbers: ")
list_output, tuple_output = generate_list_and_tuple(numbers_input)
print(list_output)
print(tuple_output)

Q17. Write a program that accepts a comma separated sequence of words as input and 
# prints the words in a comma-separated sequence after sorting them alphabetically.

# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world

#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# In[30]:


def sort_words_sequence(words_sequence):
    words_list = words_sequence.split(',')
    sorted_words = sorted(words_list)
    sorted_sequence = ','.join(sorted_words)
    return sorted_sequence

# Example usage:
words_input = input("Enter a comma-separated sequence of words: ")
sorted_output = sort_words_sequence(words_input)
print(sorted_output)

Q18. Write a program that accepts a sequence of whitespace separated words 
# as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again
# Then, the output should be: again and hello makes perfect practice world

#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
#We use set container to remove duplicated data automatically and then use sorted() to sort the data.

# In[27]:


def remove_duplicates_and_sort(sentence):
    words = sentence.split()
    unique_words = sorted(set(words))
    result = ' '.join(unique_words)
    return result

# Example usage:
sentence = input("Enter a sequence of words: ")
output = remove_duplicates_and_sort(sentence)
print(output)

Q19. Write a program that accepts a sentence and calculate the number of upper case 
# letters and lower case letters.
#Suppose the following input is supplied to the program: Hello world!
#Then, the output should be: UPPER CASE 1 LOWER CASE 9

#Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

# In[22]:


def count_upper_lower(sentence):
    upper_count = 0
    lower_count = 0

    for char in sentence:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Example usage:
sentence = input("Enter a sentence: ")
upper, lower = count_upper_lower(sentence)
print("UPPER CASE:", upper, "LOWER CASE:", lower)

Q20. Write a program that takes a string and returns reversed string. i.e. if input is "abcd123" output should be "321dcba"
# In[4]:


def reverse_string(input_str):
    return input_str[::-1]


input_str = "abcd123"
reversed_str = reverse_string(input_str)
print(reversed_str)

