# -------------decorators--------------
# def dec(func):
#     def inner():
#         print('this is second')
#         return func()
#     print('first')   
#     return inner

# @dec
# def outer ():
#     print('last')
# outer()

#-----------comprihension--------------
# 1) list comprehension
# l=[i*i for i in range(20)if i%2!=0]
# print(l)

# l=[2,4,5]
# l2=[5,3,2,1]
# m=[i*j for i in l for j in l2]
# print (m)

# l=[2,4,5]
# l2=[5,3,2,1]
# m=[[i,j] for i in l for j in l2]
# print (m)

# ----------dict comprehension----------------

# d= {i:i*i for i in range(10) if i>=1}
# print(d)
#l1=[1,2,3,4,5,6,7,8,9,10]
# l2=["sun","mon","tue","wed","thr","fri","sat"]

# s={i:j for i,j in zip (l1,l2)}
# print(s)

# -------set comprehension------------
# l1=[2,1,4,5,2,1,2,3,5,3,2]
# s={i*i for i in l1}
# print(s)

# --------generator comprehension--------- 
# def gen(l1):
#     for i in l1:
#      if i %2==0:
#         yield i
# l1=[2,3,4,5,6,7,8,9,10]
# a=gen(l1)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

# l1=[2,3,4,5,6,7,8,9,10]
# s=(i for i in l1 if i%2==0)
# for i in s :
#     print (i)

# --------lambda,map ,filter--------- 
# a=[1,2,3,4,5,6,7,8,9]

# ans=list(filter(lambda x:x>7,a))
# print(ans)
# ans=list(map(lambda x:x*x,a))
# print(ans)

# t= lambda x,y :x*y
# print(t(4,5))
# --------files in django project----------
# prj
#  __init__.py
#  settings.py
#  asgi.py
#  wsgi.py
#  urls.py
# app
#  __init__.py
#  views.py
#  test.py
#  admin.py
#  models.py
#  app.py
# db.sqllite3
# manage.py
# a=[8,3,1,8,10,2]
# n=len(a)
# for i in range(1,n):
#     ls=sum(a[0:i])
#     rs=sum(a[i+1:])
#     if ls==rs:
#      print(a[i])

# def d():
#     """printing the docsting"""
#     print("this is the docstring")
# print(d.__doc__)
# d()

# l1=[1,2,3,4]
# del l1[1]
# print(l1)

# import time
# # time1=time.strftime('%H')


# name='Roshan'
# time1=18
# if int(time1)<12:
#     print(f'Hello {name},Good Morning ...!')
# elif time1>12 and time1<18:
#     print(f'Hello {name},Good Afternoon ...!')
# else:
#     print(f'Hello {name},Good Evening ...!')

# kaun banenga corepati

# que=['what is the first alphabate?',
#    'how many vowels are in  alphabates A-Z?',
#    'how many alphabates are in A-Z?',
#    'how many days are in a year?']

# ans=[['A : D','B : A','C : Y','D : R'],
#      ['A : 5','B : 9','C : 7','D : 8'],
#      ['A : 22','B : 28','C : 25','D : 26'],
#      ['A : 364','B : 362','C : 365','D : 361']]

# correcet_ans =['B','A','D','C']

# amount=0
# que_no=0
# guesses=[]

# for q in que:
#     print('____________________________')
#     print(q)
#     for a in ans[que_no]:
#      print (a)
#     ans_in=input("Enter Your Choice A,B,C,D - ").upper()
#     print('____________________________')
    
#     guesses.append(ans_in)
#     if guesses[que_no]==correcet_ans[que_no]:
#         print('Correct')
#         amount+=100000
#     else:
#         print('Incorrect')
#         print("The correct Guess is",correcet_ans[que_no])
#     que_no+=1
# print('____________________________')
# print('The final Amount u won is -{} RS'.format(amount))
# print('____________________________')


# def roshan():
#     "this  is the docstring"
#     print('roshan function')

# roshan()

# print(roshan.__doc__)

# r=7.5601241
# print(f'{r:.2f}')

# def fact(n):
#     if n==0 or n==1:
#      return 1
#     else:
#      return n*fact(n-1)
# a=fact(5)
# print(a)


# a=set()
# a.add(10)
# a.add(10,20)
# a.add([10,20])
# a.add([10,20,30])
# print(a)
# a.update([10,20,30,40])
# print(a)roshan sanjay patil sanjay patil rosgab

l=['roshan']
for i,j in range(0,len(l)):
    print(i,j)