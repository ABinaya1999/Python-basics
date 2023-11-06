# print(list(range(10,21,2)))

# persons ={
#     'ram':25,
#     'shyam':35,
#     'hari':85,
#     'rita':68
# }
# print(persons['ram'])

# name = input("enter name: ").lower()
# print(f"Hi {name} Your grade is {persons[name]}")

# number =  int(input("enter number"))
# print(list(range(0,number+1,2)))


# print(list(range(5, 10)))

# print(list(range(10,21,2)))

# persons = {
#     'ram':25,
#     'shyam':35,
#     'hari':85,
#     'rita':68
# }
# name = input("enter name: ").lower()
# print(f'Hi {name.capitalize()} Your grade is {persons[name]}')

# number = int(input("enter the number: "))
# print(list(range(0,number+1,2)))

# print(number % 2 == 0)

# print(number % 5 == 0)

# info = {
#     'fn':"binay",
#     'ln':"parajuli",
#     'address':{
#         'city':'pokhara',
#         'street':'kolpatan'
#     }
    
# }
# print(info['address']['city'])

# number = 8

# if number == 8:
#     print("The number is 8")

# if number % 2 == 0:
#     print("The number is even")

# if number > 5 :
#     print("The number is greater than 5")
# else:
#     print("I am else")    


# fn = 'john'
# ln = 'doe'

# if fn == 'john':
#     if ln == 'doe':
#         print('yo yo')
#     elif ln == 'dd':
#         print("gu gu")
#     else:
#         print("dff")
 
 
        
# first_number = int(input("Enter first number: "))
# second_number = int(input("Enter the second number: "))

# if first_number < second_number:
#     print(first_number)
# else:
#     print(second_number)

# if first_number < second_number:
#      print(f"The smallest number between {first_number} and {second_number} is {first_number} ")
# elif first_number > second_number:
#      print(f"The smallest number between {first_number} and {second_number} is {second_number} ")
# else:
#     print("equal")

# number = int(input("enter number: "))
# result = "even" if number % 2 == 0 else "odd"
# print(result)
    
# salary = float(input("enter the salary: "))
# months = int(input("enter the months: "))
# avg = salary / months
# if avg > 10000:
#     print("rich")
# else:
#     print("poor")

# student_grade = {
#     'ram': 85,
#     'shyam': 63,
#     'hari': 55,
#     'rita': 20
# }
# name = input("enter name: ")
# if student_grade[name] >= 80:
#     print(f"Congratulation {name} , you got distinction")
# elif student_grade[name] >= 60:
#      print(f" first division {name} ")  
# elif student_grade[name] >=50:
#     print(f"second division {name}")
# else:
#     print("Mom's flying chappal received")

# my_info = { 'name': 'ram', 'age': 25, 'address':'Nepal'}
# for iteam in my_info.items():
#     print(iteam)


# names = ['ram', 'shyan', 'hari', 'rita', 'sita', 'Hunter', 'Harry', 'hilary' ]
# for name in names:
#     if name.startswith('h') or name.startswith('H'):
#         print(name)

# for number in range (10, 21):
#     if number % 2 == 0:
#         print(number)
    
# number = int(input("Enter the number: "))
# even_numbers = []
# odd_numbers = []
# for num in range(0, number+1):
    
#     if num % 2 == 0:
#          even_numbers.append(num)
#     else:
#         odd_numbers.append(num)
# print("Even numbers:", even_numbers)
# print("Odd numbers:", odd_numbers)

# student_grade = {
#     'ram': 85,
#     'shyam': 63,
#     'hari': 55,
#     'rita': 20
# }


# while True:
#     name = input("Enter name: ") 
#     if name in student_grade:  
#         # grade = student_grade[name]
#         print(f"Hi {name.capitalize()}, your grade is {student_grade[name]}")            
#     else:
#         print("Not present")
# name_list =[]
# names = ['ram', 'shyam', 'hari', 'rita', 'sita', 'Hunter', 'Harry', 'hilary']
# for name in names:
#     if name.startswith('h') or name.startswith('H'):
#         name_list.append(name)        
# print(name_list) 
       
# even_number = []
# odd_number = []   
# for number in list(range(1 , 11):
#     if number % 2 == 0:
#         even_number.append(number)
        
#     else:
#         odd_number.append(number)
        
# print(f"even numbers: {even_number}")
# print(f"odd numbers: {odd_number}")



# list_name = []
# names = ['ram', 'shyan', 'hari', 'rita', 'sita', 'Hunter', 'Harry', 'hilary' ]
# for name in names:
#     if name.startswith('h') or name.startswith('H'):
#         list_name.append(name)
# print(list_name)

# even_numbers =[]
# for number in list(range(10, 21, 2)):
#     even_numbers.append(number)
# print(even_numbers)

# student_grade = {'ram': 85, 'shyam': 63, 'hari': 55, 'rita': 20}
# for student in student_grade:
#     print(f"Hi {student.capitalize()}.Your grade is {student_grade[student]}")
    
# even_number = []
# odd_number = []   
# for number in list(range(1 ,11)):
#     if number % 2 == 0:
#         even_number.append(number)
        
#     else:
#         odd_number.append(number)        
# print(f"even numbers: {even_number}")
# print(f"odd numbers: {odd_number}")


# student_grade = {
#     'ram': 85,
#     'shyam': 63,
#     'hari': 55,
#     'rita': 20
# }    
# while True:
#     name = input("enter the name: ")
#     if name not in student_grade:
#          print('not found')
         
#     else: 
                   
#         if student_grade[name] >= 80:
#                 print(f"Congratulation {name} , you got distinction")
#         elif student_grade[name] >= 60:
#                 print(f" first division {name} ")  
#         elif student_grade[name] >=50:
#                 print(f"second division {name}")
#         else:
#                 print("Mom's flying chappal received")
           
# def sum(**num):  
#     return num
# print(sum(n=1,b=2,m=3))
        
# a ="    bb      "
# print(a.strip(''))

# def check(**kwargs):
#     print(f"My name is {kwargs['ln']}")
# check(fn="binay", mn="raj", ln="parajuli")

# def check(*args):
#     print(f"MY name is {args[0]}")
# check("binay", "parajuli")
##################################################
# def check(**kwargs):
#     print(f"First name is: {kwargs["nn"]}")
# check(nn = "binay", ln = "parajuli")
##################################################
# dictii = {
#     'name':1
# }
# print(dictii["name"])

# import os
# os.mkdir("hello")

# os.rmdir("hello")

# from webbrowser import open
# title = input("enter: ")
# open(f'https://www.youtube.com/results?search_query={title}')
    
# def my_function(function_name, iterables):
#     result = []
#     for items in iterables:
#         new_items = function_name(items)
#         result.append(new_items)
#     return (result)

# print(my_function(lambda x : x**3, [3,5,8]))

# r = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)

# try:
#     user_input = r.recognize_sphinx(audio)
#     print(user_input)
# except sr.UnknownValueError:
#     print("Sphinx could not understand audio")
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))

# if 'play' in user_input.lower():
#     video_title = user_input.replace('play', '')
#     pywhatkit.playonyt(video_title)

# import pywhatkit
# song = input('Enter song title ')
# pywhatkit.playonyt(song)
# num = list(range(1,10))
# new_list = [x for x in num if x%2==0]
# print(new_list)

# months = ['jan', 'feb', 'mar', 'apr', 'may', 'june', 'july', 'august', 'sept', 'oct', 'nov', 'dec']
# new_months = [month.capitalize() for month in months if 'a' in month]
# print(new_months)
# a ='Abb'
# print(a.lower().startswith('a'))
# a

# text = "Hello 1world"
# uppercase_chars = [char for char in text if char.isalpha()]
# Result: ['H', 'E', 'L', 'L', 'O', 'W', 'O', 'R', 'L', 'D']
# print(uppercase_chars)

# function_name = lambda x, y : x + y
# print(function_name(1,2))

# multi = lambda x: x**2
# print(multi(2))

# check = lambda s : True if s.lower().startswith('u') else False
# print(check("UUMM"))

# print(list(filter(lambda m: True if 'a' in m else False,['january', 'feburary', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'])))

# even = list(range(1,11))

# even_list = [number for number in even if number % 2 == 0]
# even_filter = list(filter(lambda num: True if num%2==0 else False, even))
# print(even_list)
# print(even_filter)


# square_list = [num**2 for num in even]
# square_map = list(map(lambda x:x**2, even))
# print(square_list)
# print(square_map)

# names = ['ram', 'shyam', 'hari', 'rita', 'sita']
# cname = [name.capitalize() for name in names ]
# lname = list(map(lambda x:x.capitalize(),names))
# print(cname)
# print(lname)

# from functools import reduce

# sum = reduce(lambda x,y: x+y , range(1,10))
# print(sum/9)
# a = []
# for item in range(0,10):
#     if item%2==0:
#         a.append(item)
# print(a)

# a = [item for item in range(0,10) if item%2==0]
# print(a)
# result= []
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# for i in range(0,x+1):
#     for j in range(0,y+1):
#         for k in range(0,z+1):
#             permuation = [i,j,k]
#             if sum(permuation) <n:
#                 result.append(permuation)
# print(result)
# print(sum([1,2]))
# my_dict = {'a': 10, 'b': 20, 'c': 30}
# total = sum(my_dict.values())
# print(total)
# try :
#     a = 1
#     b = 0
#     print(a//b)
# except Exception as e:
#     print(e)

# n = int(input())
# error = []
# for i in range(n):
#     try:
#         x,y = map(int,input().split())
#         error.append(x//y)
#     except Exception as e:
#         error.append(f'Error Code: {e}')
# for i in range(len(error)):
#     print(error[i])

# x, y = map(int, input().split())
# print(eval(input())== y)
# x = 1
# s = input()
# print(eval(s))
    
# input = [[input("Enter name"),input("Enter age")] for i in range(2)]
# print(*input)
    


