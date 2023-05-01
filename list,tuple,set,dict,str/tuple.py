# Exercise 1: Reverse the tuple
# Given:

# tuple1 = (10, 20, 30, 40, 50)
# Expected output:

# (50, 40, 30, 20, 10)

# tuple1 = (10, 20, 30, 40, 50)

# tuple1=list(tuple1)
# tuple1.reverse()
# tuple1=tuple(tuple1)
# print(tuple1)


# Exercise 2: Access value 20 from the tuple
# The given tuple is a nested tuple. write a Python program to print the value 20.

# Given:

# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# Expected output:

# 20


# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

# print(tuple1[1][1])

# Exercise 3: Create a tuple with single item 50

# t=(50,)

# print (t)
# print (type(t))

# Exercise 4: Unpack the tuple into 4 variables
# Write a program to unpack the following tuple into four variables and display each variable.

# Given:

# tuple1 = (10, 20, 30, 40)
# Expected output:

# tuple1 = (10, 20, 30, 40)
# # Your code
# print(a) # should print 10
# print(b) # should print 20
# print(c) # should print 30
# print(d) # should print 40

#unpacking
# tuple1 = (10, 20, 30, 40)
# a,b,c,d=tuple1
# print(a) # should print 10
# print(b) # should print 20
# print(c) # should print 30
# print(d)

# #packing
# a,b,c,d,e,f=1,2,3,4,5,6
# tup=()
# tup=a,b,c,d,e,f
# print (tup)

# Exercise 5: Swap two tuples in Python
# Given:

# tuple1 = (11, 22)
# tuple2 = (99, 88)


# Expected output:

# tuple1: (99, 88)
# tuple2: (11, 22)

# tuple1 = (11, 22)
# tuple2 = (99, 88)

# tuple1,tuple2=tuple2,tuple1
# print('tuple 1 is',tuple1)
# print('tuple 2 is',tuple2)

# Exercise 6: Copy specific elements from one tuple to a new tuple
# Write a program to copy elements 44 and 55 from the following tuple into a new tuple.

# Given:

# tuple1 = (11, 22, 33, 44, 55, 66)
# Expected output:

# tuple2: (44, 55)

# tuple1 = (11, 22, 33, 44, 55, 66)
# l=[]
# for i in tuple1:
#     if i ==44 or i ==55:
#         l.append(i)
# l=tuple(l)
# print(l)


# Exercise 7: Modify the tuple
# Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222

# Given:



# tuple1 = (11, [22, 33], 44, 55)
# Expected output:

# tuple1: (11, [222, 33], 44, 55)


# Exercise 9: Counts the number of occurrences of item 50 from a tuple
# tuple1 = (50,23,56,89,50)
# print(tuple1.count(50))

# Exercise 10: Check if all items in the tuple are the same

# tuple1 = (45, 45, 45, 45)
# def check (n):
#  return all(n[0]==i for i in n)

# print(check(tuple1))