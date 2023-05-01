# Exercise 1A: Create a string made of the first, middle and last character
# a= "roshansanjaypatil"   #.....output- rnl
# str=''
# mid=len(a)//2

# str+=a[0]+a[mid]+a[-1]
# print(str)


# Exercise 1B: Create a string made of the middle three characters

# a='roshanpatil' #.....output- anp
# str=''
# mid=len(a)//2
# str+=a[mid-1]+a[mid]+a[mid+1]
# print(str)

# Exercise 2: Append new string in the middle of a given string

# a="roshanpatil" #.....output-rosha21npatil
# str='21'

# mid =len(a)//2
# a1=a[0:mid]+str+a[mid:]
# print(a1)

# Exercise 3: Create a new string made of the first, middle, and last characters of each input string
# a="America"   #.....output-AJrpan
# b="Japan"
# mid1=len(a)//2
# mid2=len(b)//2
# ans=a[0]+b[0]+a[mid1]+b[mid2]+a[-1]+b[-1]
# print(ans)

# Exercise 4: Arrange string characters such that lowercase letters should come first

# str1 = '5$Py$^%NaTiv355e'  #.....output-yaivePNT5355$$^%  first upper only second lower only third num only  and at last other
# lower=[]
# upper=[]
# num=[]
# other=[]
# for i in str1:
#     if i.islower():
#         lower.append(i)
#     elif i.isupper() :
#         upper.append(i)
        
#     elif i.isnumeric() :
#         num.append(i)
#     else:
#         other.append(i)
# ans=''.join(lower+upper+num+other)
# print(ans)

# Exercise 5: Count all letters, digits, and special symbols from a given string
'''output=The lower cha in giver string are -6 times
the upper char in given string are -0
times the numbers in given string are -0 times
the other special char in  given str are 0 times'''
# str1 = 'roshan'
# lower=[]
# upper=[]
# num=[]
# other=[]
# for i in str1:
#     if i.islower():
#         lower.append(i)
#     elif i.isupper() :
#         upper.append(i)
        
#     elif i.isnumeric() :
#         num.append(i)
#     else:
#         other.append(i)

# print(f'The lower cha in giver string are -{len(lower)} times\nthe upper char in given string are -{len(upper)}\ntimes the numbers in given string are -{len(num)} times\nthe other special char in  given str are {len(other)} times')


# Exercise 6: Create a mixed String using the following rules
# s1 = "Abc"
# s2 = "Xyz"  output=AzbycX

# s1 = "Abcfr"
# s2 = "Xyz"
# a=[]

# s3=s2[::-1]
# for i in range (0,len(s2)):
#     q=s1[i]+s3[i]
#     a.append(q)
# ans=''.join(a)
# print(ans)

# String characters balance Test
'''Case 1:

s1 = "Yn"
s2 = "PYnative"
Expected Output:

True
Case 2:

s1 = "Ynf"
s2 = "PYnative"
Expected Output:

False'''

# s='roshan'
# n='ro'
# flag=True
# for i in s:
#     if i in n:
#      continue
#     else:
#        flag=False
# print(flag)


# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case

# str1 = " USA USA USA USA Welcome usa  to USA. usa awesome USA, isn't USA usa it USA?"
# sub_string = "USA"
# temp=str1.lower()
# r= temp.count(sub_string.lower())
# print(r)

# Exercise 9: Calculate the sum and average of the digits present in a string

# str1 = "PYnative29@#8496" ...output-the avf of number in str is= 6.333333333333333

# str=""
# sum=0
# for i in str1:
#      if i.isnumeric():
#           str+=i

# n=len(str)
# for i in str:
#      sum=sum+int(i)
# print('the avf of number in str is=',sum/n)


# Exercise 10: Write a program to count occurrences of all characters within a string
# a='apple' #output- result:- {'a': 1, 'p': 2, 'l': 1, 'e': 1}
# dict={}
# for i in a:
#     value=a.count(i)
#     dict[i]=value
# print('result:-',dict)

# Exercise 11: Reverse a given string
# Given:

# str1 = "PYnative"
# # 1st way
# # print(str1[::-1])

# # 2nd way

# a=''.join(reversed(str1))
# print(a)

# Exercise 12: Find the last position of a given substring(Emma)
# str1 = "Emma is a data scientist who knows Python. Emma works at google."

# str =str1.lower()
# a=str.rfind('emma')
# print(a)

# Split a string on hyphens #output-Emma-is-a-data-scientist-who-knows-Python.-Emma-works-at-google.
# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# str=str1.split(' ')
# print('\n'.join(str))

# Exercise 14: Remove empty strings from a list of strings
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# 1st way
# for i in str_list:
#     if i ==None or i == "":
#      str_list.remove(i)
# print(str_list)

#2nd way
# str=[]
# for i in str_list:
#     if i:
#      str.append (i)
# print(str)

#3rd way 
# a=list(filter(None,str_list))
# print(a)

# Exercise 15: Remove special symbols / punctuation from a string
# import string
# str1 = "/*Jon is @developer88 & musici55an"
# new_str=str1.translate(str.maketrans('','',string.digits))
# print(new_str)

# Exercise 16: Removal all characters from a string except integers
# str1 = 'I am 25 years and 10 months old'
# str=''
# for i in str1:
#     if i.isnumeric():
#         str+=i
# print(str)


# Find words with both alphabets and numbers ----output= Emma25 scientist50


# str1 = "Emma25 is Data scientist50 and AI Expert" 
# ans=[]
# l=str1.split(' ')

# for item in l:
    
# #     if any(char.isalpha() for char in item)and any(char.isdigit() for char in item):
# #         ans.append(item)

# # for w in ans:
# #         print(w)
        
# Exercise 18: Replace each special symbol with # in the following string output= ##Jon is #developer # musician##
# import string
# str1 = '/*Jon is @developer & musician!!'
# replace_with='#'
# for i in string.punctuation:
#     str1=str1.replace(i,replace_with)
# print(str1)

# string is pallindrn or not
# s='nitin'
# n=len(s)
# x=0
# for i in range (n):
#     if s[i]!=s[n-i-1]:
#         x=1

# if x==0:
#     print('yes')
# else:

#     print('no')

# a=458
# ans=0
# while a>0:
#     r=a%10
#     ans=ans*10+r
    
#     a=a//10
# print(ans)

while a>0:
#     r=a%10
#     ans=ans*10+r
    
#     a=a//10
# print(ans)