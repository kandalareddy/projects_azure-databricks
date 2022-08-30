# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC 
# MAGIC This notebook will just go through the basic topics in order:
# MAGIC 
# MAGIC * Data types
# MAGIC     * Numbers
# MAGIC     * Strings
# MAGIC     * Printing
# MAGIC     * Lists
# MAGIC     * Dictionaries
# MAGIC     * Booleans
# MAGIC     * Tuples 
# MAGIC     * Sets
# MAGIC * Comparison Operators
# MAGIC * if, elif, else Statements
# MAGIC * for Loops
# MAGIC * while Loops
# MAGIC * range()
# MAGIC * list comprehension
# MAGIC * functions
# MAGIC * lambda expressions
# MAGIC * map and filter
# MAGIC * methods
# MAGIC ____

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data types
# MAGIC 
# MAGIC ### Numbers

# COMMAND ----------

1 + 1

# COMMAND ----------

1 * 3

# COMMAND ----------

1 / 2

# COMMAND ----------

2 ** 4

# COMMAND ----------

4 % 2

# COMMAND ----------

5 % 2

# COMMAND ----------

(2 + 3) * (5 + 5)

# COMMAND ----------

(1+1)*(1-2)/(2**3)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Variable Assignment

# COMMAND ----------

# Can not start with number or special characters
name_of_var = 2
NameOfVariable = 1

# COMMAND ----------

x = 2
y = 3

# COMMAND ----------

z = x + y

# COMMAND ----------

z

# COMMAND ----------

# MAGIC %md
# MAGIC ### Strings

# COMMAND ----------

'single quotes'

# COMMAND ----------

"double quotes"

# COMMAND ----------

" wrap lot's of other quotes"

# COMMAND ----------

# MAGIC %md
# MAGIC ### Printing

# COMMAND ----------

x = 'hello'

# COMMAND ----------

x

# COMMAND ----------

print(x)

# COMMAND ----------

num = 12
name = 'Sam'

# COMMAND ----------

print('My number is: {one}, and my name is: {two}'.format(one=num,two=name))

# COMMAND ----------

print('My number is: {}, and my name is: {}'.format(num,name))

# COMMAND ----------

print(f'My name is:{name}, and my number is: {num}')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Lists

# COMMAND ----------

[1,2,3]

# COMMAND ----------

['hi',1,[1,2]]

# COMMAND ----------

my_list = ['a','b','c']

# COMMAND ----------

my_list.append('d')

# COMMAND ----------

my_list

# COMMAND ----------

my_list[0]

# COMMAND ----------

my_list[1]

# COMMAND ----------

my_list[1:]

# COMMAND ----------

my_list[:1]

# COMMAND ----------

my_list[0] = 'NEW'

# COMMAND ----------

my_list

# COMMAND ----------

nest = [1,2,3,[4,5,['target']]]

# COMMAND ----------

nest[3]

# COMMAND ----------

nest[3][2]

# COMMAND ----------

nest[3][2][0]

# COMMAND ----------

# MAGIC %md
# MAGIC ### Dictionaries

# COMMAND ----------

d = {'key1':'item1','key2':'item2'}

# COMMAND ----------

d

# COMMAND ----------

d['key1']

# COMMAND ----------

# MAGIC %md
# MAGIC ### Booleans

# COMMAND ----------

True

# COMMAND ----------

False

# COMMAND ----------

# MAGIC %md
# MAGIC ### Tuples 

# COMMAND ----------

t = (1,2,3)

# COMMAND ----------

t[0]

# COMMAND ----------

t[0] = 'NEW'

# COMMAND ----------

# MAGIC %md
# MAGIC ### Sets

# COMMAND ----------

{1,2,3}

# COMMAND ----------

{1,2,3,1,2,1,2,3,3,3,3,2,2,2,1,1,2}

# COMMAND ----------

# MAGIC %md
# MAGIC ## Comparison Operators

# COMMAND ----------

1 > 2

# COMMAND ----------

1 < 2

# COMMAND ----------

1 >= 1

# COMMAND ----------

1 <= 4

# COMMAND ----------

1 == 1

# COMMAND ----------

'hi' == 'bye'

# COMMAND ----------

# MAGIC %md
# MAGIC ## Logic Operators

# COMMAND ----------

(1 > 2) and (2 < 3)

# COMMAND ----------

(1 > 2) or (2 < 3)

# COMMAND ----------

(1 == 2) or (2 == 3) or (4 == 4)

# COMMAND ----------

# MAGIC %md
# MAGIC ## if,elif, else Statements

# COMMAND ----------

if 1 < 2:
    print('Yep!')

# COMMAND ----------

if 1 < 2:
    print('yep!')

# COMMAND ----------

if 1 < 2:
    print('first')
else:
    print('last')

# COMMAND ----------

if 1 > 2:
    print('first')
else:
    print('last')

# COMMAND ----------

if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('Last')

# COMMAND ----------

# MAGIC %md
# MAGIC ## for Loops

# COMMAND ----------

seq = [1,2,3,4,5]

# COMMAND ----------

for item in seq:
    print(item)

# COMMAND ----------

for item in seq:
    print('Yep')

# COMMAND ----------

for jelly in seq:
    print(jelly+jelly)

# COMMAND ----------

# MAGIC %md
# MAGIC ## while Loops

# COMMAND ----------

i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i+1

# COMMAND ----------

# MAGIC %md
# MAGIC ## range()

# COMMAND ----------

range(5)

# COMMAND ----------

for i in range(5):
    print(i)

# COMMAND ----------

list(range(5))

# COMMAND ----------

# MAGIC %md
# MAGIC ## list comprehension

# COMMAND ----------

x = [1,2,3,4]

# COMMAND ----------

out = []
for item in x:
    out.append(item**2)
print(out)

# COMMAND ----------

[item**2 for item in x]

# COMMAND ----------

# MAGIC %md
# MAGIC ## functions

# COMMAND ----------

def my_func(param1='default'):
    """
    Docstring goes here.
    """
    print(param1)

# COMMAND ----------

my_func

# COMMAND ----------

my_func()

# COMMAND ----------

my_func('new param')

# COMMAND ----------

my_func(param1='new param')

# COMMAND ----------

def square(x):
    return x**2

# COMMAND ----------

out = square(2)

# COMMAND ----------

print(out)

# COMMAND ----------

# MAGIC %md
# MAGIC ## lambda expressions

# COMMAND ----------

def times2(var):
    return var*2

# COMMAND ----------

times2(2)

# COMMAND ----------

lambda var: var*2

# COMMAND ----------

# MAGIC %md
# MAGIC ## map and filter

# COMMAND ----------

seq = [1,2,3,4,5]

# COMMAND ----------

map(times2,seq)

# COMMAND ----------

list(map(times2,seq))

# COMMAND ----------

list(map(lambda var: var*2,seq))

# COMMAND ----------

filter(lambda item: item%2 == 0,seq)

# COMMAND ----------

list(filter(lambda item: item%2 == 0,seq))

# COMMAND ----------

# MAGIC %md
# MAGIC ## methods

# COMMAND ----------

st = 'hello my name is Sam'

# COMMAND ----------

st.lower()

# COMMAND ----------

st.upper()

# COMMAND ----------

st.split()

# COMMAND ----------

tweet = 'Go Sports! #Sports'

# COMMAND ----------

tweet.split('#')

# COMMAND ----------

tweet.split('#')[1]

# COMMAND ----------

d

# COMMAND ----------

d.keys()

# COMMAND ----------

d.items()

# COMMAND ----------

lst = [1,2,3]

# COMMAND ----------

lst.pop()

# COMMAND ----------

lst

# COMMAND ----------

'x' in [1,2,3]

# COMMAND ----------

'x' in ['x','y','z']

# COMMAND ----------

# MAGIC %md
# MAGIC # Great Job!
