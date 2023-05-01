# . Python Program for factorial of a number with and without recursion 
# 

# def fac(n):
#     if n==0 or n== 1 :
#          return 1
#     else:
#         fac=1
#         for i in range (1,n+1):
#          fac=fac*i
#         return fac
    
# fact=fac(4)
# print(fact)

# def fact (n):
#     if n == 0 | n==1:
#         return 1
#     else:
#         return n* (fact(n-1))
    
# facto=fact(5)
# print(facto)

# python Program to check Armstrong Number

# n=1531
# m=n
# pow=len(str(n))
# sum=0

# while m!=0:
#     t=m%10
#     sum+=t**pow
#     m=m//10

# if sum==n:
#     print("yes")
# else:
#  print("no")

#Python program to print all Prime numbers in an Interval 
# n=1
# n2=10
# for i in range(n,n2+1):
#  if i> 1:
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#       print(i)

# 4. Python Program for Fibonacci numbers 
# num=6
# n1=0
# n2=1
# sum=0

# while sum<num:
#  print(n1) 
#  fib=n1+n2
#  n2=n1
#  n1=fib
#  sum+=1

# Python Program to find sum of array (using multiple approach)

# l1=[1,2,30,4,5,6] 
# print(l1[::-1])