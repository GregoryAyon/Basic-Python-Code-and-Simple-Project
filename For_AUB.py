# print() introduce about print function.

# print(1==2)
# print(1>2)

# Introduce varibale and their data types.
# Introduce string formating.
# Introduce string basic functions.

#  String....
# str = 'Asian University'
# print(str.capitalize())
# print(str.isalnum())
# print(str.split(' '))


# Example - Find out a born year
# name = input('Hello there! What is your name? ');
# age = int(input('How older you? '));
# result = 2022-age;
# print(f'Hello {name}, you are born in {result}');

# Example - Celcus to Fahrenheit coverter
# celcus = int(input('Enter your celcus point: '))
# fahrenheit = celcus*((9/5)+32)
# print(f'Your Fahrenheit Point: {fahrenheit:.2f}')


# if else example ......
# robot_command = input('Enter your command: ');

# if robot_command == 'forward':
#     print('Going forward...')
# elif robot_command == 'backward':
#     print('Going backward')
# else:
#     print('Still stand.');

# While looping......
# i=0
# while i<=5:
#     print(i)
#     i+=1

# Example Break....
# while True:
#     name = input('your name write here please: ')
#     if name == 'break it!':
#         break

# print('Now Its Breaked!')


# For Looping.....
# odd_sum=0
# for i in range(1,6):
#     if i%2 == 1:
#         odd_sum+=i
# print(odd_sum)


# for i in range(5,-1,-1):
#     for j in range(i):
#         print('*',end=' ')
#     print()


# Example Continue....
# sum=0
# for i in range(1,6):
#     if i == 2:
#         continue
#     sum+=i
# print(sum)



# exception handling.......
# def func(x):
#     try:
#         return 100/x
#     except:
#         print('There is zero division error')

# func(0)

# EX- Simple Project............
# from random import sample

# lower = "abcdefghijklmnopqrstuvwxyz"
# upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# numbers = "0123456789"
# symbols = "[]()*;/\,-_"

# pass_all = lower + upper + numbers + symbols
# length = 16

# for i in range(6):
#     password = "".join(sample(pass_all, length))
#     print(password)


# List......
# myList = ['Bhutan', 'Napal', 'France', 'Jamaica', 'Germany', 'Bangladesh']
# print(myList[1])
# print(myList[1:5:2])
# print(myList[::2])
# newList = myList[:3]
# print(newList)

# List Methods.....
# myList.append("Finland")
# myList.extend(["Canada", "Pakistan", "India"])
# myList.insert(3, "Bulgaria")
# myList.remove("France")
# myList.pop()
# country = myList.pop(3)
# myList.clear()
# myList.count('Bangladesh')
# print(myList)



#  Tuple Sequence .... 
# tp = ('Ayon', 24, 'Dhaka',(1,2,3))
# tp = ([1,2,3,4,5],[2,3,6,5])
# tp[0][0] = 'Ayon'
# tp = 'Ayon',
# print(tp)

# Sets ....
# mySet = {'Ayon', 1 , True, False}
# print(mySet)

# strName_1 = 'Ayon'
# print(set(strName_1))

# Dictonary ....
# myDict = {'key1': 'Ayon', 'key2': 1204}
# myDict['key3'] = 'Student'
# del  myDict['key2']
# print(myDict)


# Type of dictonary diclaration....
# a = dict(key1 = 'Simanta', key2 = 'Bohubrihi', key3 = 25)
# b = {'key1': 'Simanta', 'key2': 'Bohubrihi', 'key3': 25}
# c = dict(zip(['key1', 'key2', 'key3'], ['Simanta', 'Bohubrihi', 25]))
# d = dict([('key1', 'Simanta'), ('key2', 'Bohubrihi'), ('key3', 25)])
# e = dict({'key1': 'Simanta', 'key2': 'Bohubrihi', 'key3': 25})
# f = dict({'key1': 'Simanta', 'key2': 'Bohubrihi'}, key3 = 25)


#  Range Basics......
# a = list(range(1,20, 3))
# print(a)
# myRange = range(0, 51)
# check = 100 in myRange
# print(check)

# Sequence Unpacking.....
# myList_1 = ["Bangladesh", "India", "Pakistan", "USA", "Canada", [1,2,3]]
# c1, *c2, c3, c4, [c5, c6, c7] = myList_1
# print(c1)
# print(c2)
# print(c3)
# print(c4)
# print(c5)
# print(c6)
# print(c7)

# Looping on list and dictionary..........
# myList = [("a", 1, "BDT"), ("b", 2, "USD"), ("c", 3, "CAD")]
#for x, y, z in myList:
#    print(f"{x}, {y}, {z}")

# myDict = {"name" : "Ayon", "age" : 23, "country" : "Bangladesh"}
#for key, value in myDict.items():
    #print(f"{key} => {value}")

# myStr = "Bohubrihi"
# for ch in myStr:
#    print(ch)


# myListRen = ['Bangla', 'Spanish', 'English',  'French', 'German', 'Irish', 'Chinese']
# for i in range(len(myListRen)):
#     print(f"Language: {myListRen[i]}")



# myList = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# myList2 = [1, 2, 3, 4, 5, 6]

# enumerate....
#for i, fruit in enumerate(myList):
#    print(f"{i} index of {fruit}")

# zip....
#for i, j in zip(myList2, myList):
#    print(i, j)

# for i in reversed(sorted(myList)):
#     print(i)


#  Comprehension .......
# myList = [1,5,6,7,2,3]
# newList = []
# List of the squares of the odd numbers
# for i in myList:
#     if i%2 == 1:
#         newList.append(i*i)

# comList = [i**3 for i in myList if i%2==1]

# myList = [1, 2, 3, 4, 5, 6]

# From List............
# newList = [i+1 for i in myList]
# newDict = {i: i*i for i in myList}
# newSet = {i**3 for i in myList}
# newTuple = tuple(i**4 for i in myList)
# newTlist = [(i, i**2, i**3) for i in myList]
# print(newTlist)


#  Python Functions.....
#  positional arguments
# def hello(fname, lname):
#     print(f'Full Name: {fname} {lname}')
# hello('Ayon', 'Roy')

#  Arbitrary Arguments.....
# def func(*args):
#     printList = [item for item in args]
#     for i in printList:
#         print(f'iterate value: {i}')

# func('Ayon', 'Roy', 23, '13-Feb-2022')

# Arbitrary Keyword Arguments........
# def fun2(**kwargs):
#     print(kwargs['fname'])

# fun2(fname="Ayon", lname="Roy", age=25)


# lambda function and Anonymous function .........
# def add(x, y):
#     return x + y
# print((lambda x, y: x + y)(10, 15))

# map function...........
# def func(n):
#     return n*n*n
# l = [3, 4, 1, 0, 6]
# newL = list(map(lambda n: n*n*n, l)) # newL = [n*n*n for n in l]
# print(newL)

#  Filter functions ......
# l = [1, 3, 4, 6, 88, 4, 2, 9, 5]
# def func(n):
#     return n%2==1
# newList = list(filter(lambda n: n%2==1, l))
# print(newList)

# reduce....
# from functools import reduce
# li = [1, 2, 3, 4, 2 ,3 ,4]
# def func(x, y):
#     return x + y

# sum = reduce(lambda x, y: x+y, li)
# print(sum)

# Higher Order Functions .....
# def hof(fn):
#     print(fn.__name__)
#     fn()

# def hello():
#     print('Hello World!')

# def printName():
#     print('Hello Ayon!')

# hof(printName)


# li = [1,2,3,4,5,6]

# def myFilter(fn, l):
#     newL = []
#     for i in l:
#         if fn(i):
#             newL.append(i)

#     return newL

# newList = list(filter(lambda x: x%2 == 1, li))
# newList = myFilter(lambda x: x%2 == 1, li)
# print(newList)

# Higher Order Function -> Accepts function as argument or returns function......
# Wrapper
# def myWrapper(fn):
#     def test():
#         print("I am from test! Before")
#         fn()
#         print("I am from test! After")

#     return test

# # Decorators
# @myWrapper
# def greet():
#     print("Hello world!")

# @myWrapper
# def hello():
#     print("Hello Hello")

# # hello = myWrapper(hello)
# # #greet()
# hello()

# Simple AI Iphone Price Ditection Project ............
# import pandas as pd
# import matplotlib.pyplot as mlt
# from sklearn.linear_model import LinearRegression

# data = pd.read_csv('iphone_price_bd.csv')
# # print(data)
# # mlt.scatter(data['version'], data['price'])
# # mlt.show()
# model = LinearRegression()
# model.fit(data[['version']], data[['price']])
# print(model.predict([[15]]))



