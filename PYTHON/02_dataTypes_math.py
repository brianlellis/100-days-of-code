"""
Abstract Data Type and Data Structures
  Generally, data structures can be divided into two categories in computer science: 
  primitive and non-primitive data structures. 
  The former are the simplest forms of representing data, whereas the latter are more advanced: 
  they contain the primitive data structures within more complex data structures for special purposes.

Primitive Data Structures
  Integers 
    You can use an integer represent numeric data, and more specifically, whole numbers 
    from negative infinity to infinity, like 4, 5, or -1.

    https://stackoverflow.com/questions/54009778/what-do-underscores-in-a-number-mean

  Float
    "Float" stands for 'floating point number'. You can use it for rational numbers, 
    usually ending with a decimal figure, such as 1.11 or 3.14.
  Strings
    Strings are collections of alphabets, words or other characters. In Python, you can create 
    strings by enclosing a sequence of characters within a pair of single or double quotes. 
    For example: 'cake', "cookie", etc.

    See format() and f'' string for interpolation

  Boolean
    This built-in data type that can take up the values: True and False, which often makes them 
    interchangeable with the integers 1 and 0. Booleans are useful in conditional and comparison 
    expressions.

Non-Primitive Data Structures
  Arrays
    Compact way of collecting basic data types, all the entries in an array must be of the same 
    data type. However, arrays are not all that popular in Python, unlike the other 
    programming languages such as C++ or Java. In general, when people talk of arrays in Python, 
    they are actually referring to lists. However, there is a fundamental difference between them.

  Lists
    Lists in Python are used to store collection of heterogeneous items. These are mutable, which 
    means that you can change their content without changing their identity. You can recognize lists 
    by their square brackets [ and ]

  !!! NOTE FOR Arrays V List!!!
  An array is faster than a list in python since all the elements stored in an array are homogeneous i.e., 
  they have the same data type whereas a list contains heterogeneous elements.
  
  Tuples
    The difference between tuples and list is that tuples are immutable, which means once defined 
    you cannot delete, add or edit any values inside it.

  Dictionary
    Dictionaries are made up of key-value pairs. key is used to identify the item and the value holds 
    as the name suggests, the value of the item.

  Sets
    Sets are a collection of distinct (unique) objects. 

  Files
    Files are traditionally a part of data structures. And although big data is commonplace in the data science industry, 
    a programming language without the capability to store and retrieve previously stored information would hardly be useful. 
    You still have to make use of the all the data sitting in files across databases and you will learn how to do this.

    The syntax to read and write files:
      - open()      to open files in your system, the filename is the name of the file to be opened
      - read()      to read entire files
      - readline()  to read one line at a time
      - write()     to write a string to a file, and return the number of characters written
      - close()     to close the file
"""

print("Welcome to the tip calculator.")
bill  = input("What was the total bill? $")
tip   = input("What tip percantage would you like? (10, 12, or 15) ")
split = input("How many people are splitting the bill? ")

tip_amt   = float(bill) * (float(tip) / 100)
split_amt = (float(bill)+float(tip_amt)) / float(split)
print(f'Each person should pay: ${round(split_amt, 2)}')
