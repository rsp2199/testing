# Exercise 1: Convert two lists into a dictionary
# Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30,44]

# d={i:j for i, j in zip(keys,values)}
# print(d)


# Exercise 2: Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Expected output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty':50}
# 1st way
# d={**dict1,**dict2}
# print(d)

# 2nd way

# d=dict1.copy()
# d.update(dict2)
# print(d)

# Exercise 3: Print the value of key ‘history’ from the below dict
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# Expected output:

# 80

# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sampleDict["class"]['student']['marks']['history'])

# Exercise 4: Initialize dictionary with default values
# In Python, we can initialize the keys with the same values.

# Given:

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# AD
# Expected output:

# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# d=dict.fromkeys(employees,defaults)
# print(d)

# Exercise 5: Create a dictionary by extracting the keys from a given dictionary
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# Given dictionary:

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]
# Expected output:

# {'name': 'Kelly', 'salary': 8000}

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# key=['name','salary']
# d={k:sample_dict[k] for k in key}
# print(d)

# Exercise 6: Delete a list of keys from a dictionary
# Given:

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# # Keys to remove
# keys = ["name", "salary"]
# Expected output:

# {'city': 'New york', 'age': 25}

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# key=['name', 'salary']

# for k in key:
#     sample_dict.pop(k)
# print(sample_dict)


# Write a Python program to check if value 200 exists in the following dictionary.

# Given:

# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# Expected output:

# 200 present in a dict
# sample_dict = {'a': 100, 'b': 200, 'c': 300}

# v= sample_dict.values()
# if 200 in v:
#     print('yes the value is present')
# else:
#     print("value is not present")

# Exercise 8: Rename key of a dictionary
# Write a program to rename a key city to a location in the following dictionary.

# Given:

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# sample_dict['location']=sample_dict.pop('city')
# print(sample_dict)

# Exercise 9: Get the key of a minimum value from the following dictionary

# sample_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }


# print(min(sample_dict,key= sample_dict.get))

# Exercise 10: Change value of a key in a nested dictionary
# Write a Python program to change Brad’s salary to 8500 in the following dictionary.

# Given:

# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# Expected output:

# {
#    'emp1': {'name': 'Jhon', 'salary': 7500},
#    'emp2': {'name': 'Emma', 'salary': 8000},
#    'emp3': {'name': 'Brad', 'salary': 8500}
# }
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
#     }
# sample_dict['emp3']['salary']=8500
# print(sample_dict)

# s={1,2,3,'ter','2',True}
# print(s)
# print(s)
# print(s)
# print(s)

# print(s)

# sort a dict using dic comprehension
# d={1:'s',5:"u",2:'f',3:'t',7:'e',4:'g'}
# a={x:y for x,y in sorted(d.items())}
# # a={x:y for x,y in sorted(d.items(),key=lambda a:a[1])}
# print(a)
