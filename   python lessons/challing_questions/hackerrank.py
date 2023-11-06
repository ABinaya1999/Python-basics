# import random
# options =['s','w', 'g']
# def check(options):
#     return random.choice(options)

# rounds = int(input("Enter number of rounds: "))
# user_wins= 0
# computer_wins = 0
# round = 1
# while round <= rounds:
    
#     print(f"Round: {round}")
#     print("Snake: s \n Water: w\n Gun: g")
#     try :
#         choose =input("Choose yout options: ")
#     except Exception as e:
#         print(e)
    
#     if choose not in 'swg':
#         print("Invalid ")
#         continue
    
#     if choose  check:
#         print(f"You won Round {round}")
#         user_wins += 1
#     else:
#         print(f"You loose Round {round}")
#         computer_wins += 1
#     round += 1
    

# if user_wins > computer_wins:
#     print("COngo")
# else:
#     print("Fail")
# n=[2,3,6,6,4]
# numbers = list(map(int,n))
# numbers = list(set(numbers))
# numbers.remove(max(numbers))
# numbers.sort()
# print(sorted(numbers))
# print(max(numbers))


# if __name__ == '__main__':
#     n = [2,3,6,6,5]
#     arr = list(map(int,n))
#     arr = list(set(arr))
#     arr.remove(max(arr))
#     print(max(arr))

# students = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     students.append([name,score])

# b = sorted(list(set([i[1] for i in students ])))
# c =sorted([i[0] for i in students if i[1] == b[1]])
# for i in c:
#     print(i)


# n = int(input("enter: "))
# students = []
# for i in range(n):
#     name = input("Enter name")
#     grade = int(input("Enter grade: "))
#     students.append([name,grade])

# sorted_number = sorted(list(set([i[1] for i in students])))
# name = sorted([i[0] for i in  students if i[1] == sorted_number[1]])
# for i in name:
#     print(i)
      
# a = input().split()
# print(a[1])

# import tkinter as tk
# window = tk.Tk()
# greeting = tk.Label(text="Hello, Tkinter")

# s = "binay 1"
# # s1= s.split()
# # print(' '.join(s1))
# l=[1,2,3]
# print(''.join(str(i) for i in l))

# print(s)

# l =["hello", "binay"]
# s = ' '
# for i in l:
#     s += ' ' + i
# print(s.strip())

# l = [1,2,3]
# print(''.join(str(i) for i in list(map(int,l))))
# print(list(map(lambda l: True if l>1 else False,l)))
# num = [1,2,3,4]
# a = [i for i in num if i%2 == 0 ]
# print(a)
# l=[1,2,3,4]
# print([True for n in l if n%2==0 ])
# s = "binay"
# print(any(i.islower() for i in s))

# print(list(i for i in l if i%2==0))

# x = int(input())
# y = x*3
# a = []
# for i in range(x):
#     r = []
#     for j in range(y):
#         r.append("-")
#     a.append(r)
        
# print(". ".join(a))      

# s = "binay parajuli"
# l = s.split()
# print(" ".join(l))

# a= 2
# print(f"{a:.2f}")
# print("%.2f" %a)

# width = 15
# print("hackerrank".rjust(width))
# print("hackerrank".center(width,'-'))
# print("HackerRank".rjust(width))

# c = 'H'
# thickness = 5
# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#   # Top Pillars
# for i in range(thickness + 1):
#     print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
# for i in range((thickness + 1) // 2):
#     print((c * thickness * 5).center(thickness * 6))
    
# n = 17   
# w=len(bin(n)[2:])
# for i in range(1,n+1):
#   o = oct(i).replace('0o','')
#   h = hex(i).replace('0x', '').capitalize()
#   b = bin(i).replace('0b', '')
#   print(f'{i}'.rjust(w)+f'{o}'.rjust(w)+f'{h}'.rjust(w)+f'{b}'.rjust(w))
# from itertools import *
# s,n = input().split()
# n = int(n)
# s = s.upper()
# so = sorted(s)
# for i in range(1,n+1):
#     a = [''.join(ii) for ii in combinations(so,i)]
#     for i in a:
#         print(i)
# import calendar
# y,m,d = map(int,input().split())
# i = calendar.weekday(y,m,d)
# match i:
#     case 0:
#         print("Monday")
#     case 1:
#         print("Tuesday")
#     case 2:
#         print("Wednesday")
#     case 3:
#         print("Thursday")
#     case 4:
#         print("Friday")
#     case 5:
#         print("Saturday")
#     case 6:
#         print("Sunday")
    
