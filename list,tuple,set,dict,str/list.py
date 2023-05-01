# Exercise 1: Reverse a list in Python
# list1 = [100, 200, 300, 400, 500]
# print(list1[::-1])
# list1.reverse()
# print(list1)

# Exercise 2: Concatenate two lists index-wise
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# Expected output:

# ['My', 'name', 'is', 'Kelly']
# list1 = ["M", "na", "i", "Ke",'fshshg']
# list2 = ["y", "me", "s", "lly"]
# try:
#     for i in range(0,len(list1)):
#      list1[i]=list1[i]+list2[i]
#     print(list1)
# except:
#    print('exception occures')

# print(5+8)

#  Exercise 3: Turn every item of a list into its square

# numbers = [1, 2, 3, 4, 5, 6, 7]
# ans=[i*i for i in numbers]
# print(ans)


# Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Expected output:

# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# ans=[]
# for i in list1:
#     for j in list2:
#         ans.append(i+j)
# print(ans)

# Exercise 5: Iterate both lists simultaneously
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

# Given

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# Expected output:

# 10 400
# 20 300
# 30 200
# 40 100

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for i,j in zip(list1,list2[::-1]):
#     print(i,j)



# Exercise 6: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]


# Expected output:

# ["Mike", "Emma", "Kelly", "Brad"]
# ans=[]
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# for i in list1:
#     if i:
#      ans.append(i)
# print(ans)


# Exercise 7: Add new item to list after a specified item
# Write a program to add item 7000 after 6000 in the following Python List

# Given:

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Expected output:

# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# list1[2][2].append(7000)
# print(list1)


# Exercise 8: Extend nested list by adding the sublist
# You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.

# Given List:

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# # sub list to add
# sub_list = ["h", "i", "j"]
# Expected Output:

# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# l=["h", "i", "j"]
# list1[2][1][2].extend(l)
# print(list1)

# Exercise 9: Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.

# Given:

# list1 = [5, 10, 15, 20, 25, 50, 20]
# Expected output:

# [5, 10, 15, 200, 25, 50, 20]
# list1 = [5, 10, 15, 20, 25, 50, 20]
# index=list1.index(20)
# list1[index]=200
# print(list1)


# Exercise 10: Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.

# Given:

# list1 = [5, 20, 15, 20, 25, 50, 20]
# Expected output:

# [5, 15, 25, 50]
# val=20
# list1 = [5, 20, 15, 20, 25, 50, 20]
# l=[i for i in list1 if i!=val]
# print(l)

# sort list without sort ketyword

# l=[1,2,4,5,8,3,6]
# n=len(l)

# for i in range (n):
#     for j in range(i+1,n):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i] 
# print(l)
