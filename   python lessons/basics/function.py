
# def add(i,j):
#     print(i + j)
    
# add(1,2)

# def info(fn, ln, age, balance = 0):
#     print(f" Hi {fn} and {ln} your {age} and {balance}")
    
# info("b")

# def max(i, j):
#     return (i if i > j else j)
# max_number = max(1, 2)
# print(max_number)

# def even(number):
#     return True if number % 2 == 0 else False

# print(even(2))
    
# def multify(list_number):
#     total = 1
#     for num in list_number:
#         total *= num 
#     return total

# list_number = [3,2,4,5,7,3]   
# print(multify(list_number) )
# # print(a)

# def string_name(string):
#     return string.upper()
# string = "Binay"
# print(string_name(string))


# def str_lenth(string1):
#     return len(string1)
# string1 = "Binay"
# c = str_lenth(string1)
# print(c)

# def full_name(fn, ln):
#     return f"{fn} {ln}"

# fname = full_name(fn = "Binay",ln = "Parajuli")
# print(fname)

# def vowel(string2):
#     strs = []
#     for str in string2:
#         if str == 'a' or str == 'e' or  str == 'i' or str == 'o' or str == 'u':
#             strs.append(str)
#             break
#     return strs     
            
# vowel_char = vowel(string2="binay")
# print(vowel(string2="binay"))

# def vowel(string2):
#     for str in string2:
#         if str != 'a':
#             return(str)
            
#         elif str !='e':
#             return(str)
            
#         elif str !='i':
#             return(str)
            
#         elif str !='o':
#             return(str)
            
#         elif str !='u':
#             return(str)
            
# vowel_char = vowel(string2="binay")
# print(vowel_char)


# def sum(number_lists):
#     total = 0
#     for num in number_lists:
#         total += num
#     return total
# a = list(sum([1,2,3,4,5]))
# print(a)

# def greatest(*args):
#     b = 0
#     for a in args:
#         if a > b:
#             b = a
#     return b    
# print(greatest(1,2,3,4,5))

# def counter(string_name):
#     vowel_count = 0
#     consonent_count = 0
#     for a in string_name:
#         if a.lower() in 'aeiou':
#             vowel_count += 1
#         else:
#             consonent_count += 1
#     return {'vowel':vowel_count, 'con':consonent_count}
# print(counter("binay"))

# def count_a(string_name):
#     count = 0
#     for a in string_name:
#         if a =='a':
#             count += 1
#     return count
# print(count_a("binaya"))

# def birth_date(date):
#     return date.split('-')
# date = "2023-07-22"
# # year  = int(input("enter "))
# # month = int(input("enter "))
# # day  = int(input("enter "))
# # date = f'{year}-{month}-{day}'
# print(birth_date(date))
# print(birth_date(date))

# def domain(email):
#     return email.split('@')[1]
# email_name = input("enter email: ")
# print(domain(email_name))

# def check(emial):
#     return'.edu' in emial
# print(check("binayparajuli@gamil.edu.com"))

# def birth_of_date(date):
    
# year = int(input("enter year: "))
# month = int(input("enter month: "))
# day = int(input("enter day: "))
# sign = input("enter - or /: ")
# if sign == '-' :
#     date = 'f{year}-{month}-{day}' 
# else:
#     date = 'f{year}/{month}/{day}'

# # print(birth_of_date(date))
# def c(date):
#     if '-' in date:
#         a = date.split('-')
#         return {'year': a[0], 'month': a[1], 'day': a[2] }
# b = c('2022-02-22')
# print(b)
############################
# def reverse(string_name):
#     result = ""
#     for char in string_name:
#         result = char + result
#     return result   
# print(reverse(string_name="binay"))

# def factorial(number):
#     result = 1
#     for n in range(1,number+1):
#         result *= n
#     return result
# print(factorial(int(input())))

# def area(radius):
#     return 3.14 * radius * radius
# print(area(int(input())))        

# def palindrome(string):  
#     return string==string[::-1]
# print(palindrome(input()))

# def check(string):

#         if '!' or '@' or '#' or '$' or '%' or '^' or '&' in string:
#             return True
# print(check("djf&"))        

# def even(number):
#     even_list = []
#     for n in range(1,number+1):
#         if n%2 == 0:
#             even_list.append(n)
#     return even_list
# print(even(4))

# def mean(*args):
#     total = 0
#     for a in args:
#         total += a
#     result = total / len(args)
#     return result
# print(mean(1,2,3,4,5,9))


# def check(string):
#     if string[0]== 'a' and string[-1] =='z':
#         return True
# print(check('addz'))

# def access(countries,capitals):
#     index = 0
#     for country in countries:
#         if country != 'Pakistan':
#             index += 1
#         elif country == 'Pakistan':
#               break    
#     return capitals[index]    
# countries = ['Nepal', 'India', 'Pakistan', 'USA']
# capitals = ['Kathmandu', 'Delhi', 'Islamabad', 'DC']
# print(access(countries,capitals ))

# def remove_whitespaces(string):
#     return string.strip()
# print(remove_whitespaces("  a   "))

# def person(fn , ln , balance=0):
#     return {
#         'first_name' : fn,
#         'last_name':ln,
#         'balance':balance
#     }
# print(person("binay","parajuli"))

# def check(number):
#     if number % 2 == 0 and number % 5 == 0:
#         return number
# print(check(10))

# def mean(list_name):
#     total = 0
#     for n in list_name:
#         total  += float(n.replace('$', ""))
#     mean = total/len(list_name)
#     return round(mean,2)
# list_name = ['$4.03333', '$5.0333', '$5.82222', '$8.99']
# print(mean(list_name))

# Let's write a Python program 
# *kwargs for a variable number of keyword arguments

# def myPrg(**kwargs):
# 	for key,value in kwargs.items():
# 		print (key,value)

# # Driver code for kwargs in python 
# myPrg(first ='Hello', mid ='Welcome', last='Hello')
# print(myPrg)

# dicta = {
#     'key':'value'
# }
# print(dicta.items())

# def c(s):
#     for i in s:
#         return True if s in '!@#$%^' else False
     
# print(c("!@#$%^"))

# countries = ['Nepal', 'India', 'Pakistan', 'USA']
# capitals = ['Kathmandu', 'Delhi', 'Islamabad', 'DC']

# countries.index('Pakistan')
# print(countries.index('Pakistan'))

# while True:
#     try:
#         num1 = int(input("Enter"))
#         num2 = int(input("enter"))
#         div = num1/num2
#         print(div)
#     except ZeroDivisionError:
#         print("dont enter 0")
#     except ValueError:
        
#     except Exception as e:
#         print("error")

# string = "Deerwalk Institute of Technology"
# try:
#     s_index = int(input("Enter index"))
#     print(string[s_index])
# except IndexError:
#     print("ERROR NO INDEX")
# except Exception as e:
#     print(type(e))
# finally:
#     print("thanks")


# string_name = 'Binay'
# try:
#     index = int(input("Enter the index: "))
#     print(string_name[index])
# except ValueError:
#     print("Enter nubmer")
# except IndexError:
#     print("Enter index in range")
# except Exception as e:
#     print(type(e))
# finally:
#     print("Thank you!!!!")


# with open("abc.txt",'r') as f:
#     f.readline()

# student_grade = {
#     'ram':28,
#     'hari':00
# }
# while True:
#     try:
#         name = input("Enter name: ")
#         print(f"{name} is {student_grade[name]}")
#     except KeyError:
#         print("enter valid name")
#     except Exception as e:
#         print("ERRORRRR")
#     finally:
#         print("eijfd")

# f = open("abc.txt", 'a')
# print(f.read(5))
# print(f.read())
# print(f.readlines())
# for line in f.readlines():
#     print(line.strip())
# f.close()
# f.read()
# f.append('hello')
# f.write("hello\n")

# with open('xyz.txt', 'a') as f:
#     print(f.write(" OK"))
    
# print(f.closed)

# with open("abc.txt", 'r') as f:
#     try:
#         print(f.write("\nMy name is parajuli"))
#     except Exception as e:
#         print("error")
# print(f.closed)

# import random


# def choose_word():
#     # List of words to choose from
#     word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
#     return random.choice(word_list)

# def display_word(word, guessed_letters):
#     # Display the word with dashes for unknown letters
#     display = ""
#     for letter in word:
#         if letter in guessed_letters:
#             display += letter
#         else:
#             display += "_"
#     return display

# def hangman():
#     word_to_guess = choose_word()
#     guessed_letters = []
#     attempts = 6  # Number of attempts before the game is over

#     print("Welcome to Hangman!")
    
#     while attempts > 0:
#         print("\nAttempts left:", attempts)
#         print(display_word(word_to_guess, guessed_letters))

#         guess = input("Guess a letter: ").lower()

#         if len(guess) != 1 or not guess.isalpha():
#             print("Invalid input. Please enter a single letter.")
#             continue

#         if guess in guessed_letters:
#             print("You've already guessed that letter.")
#             continue

#         guessed_letters.append(guess)

#         if guess in word_to_guess:
#             print("Good guess!")
#             if word_to_guess == display_word(word_to_guess, guessed_letters):
#                 print("Congratulations! You've guessed the word:", word_to_guess)
#                 break
#         else:
#             print("Wrong guess.")
#             attempts -= 1

#     if attempts == 0:
#         print("\nOut of attempts. The word was:", word_to_guess)

# import random

# def choose_word():
#     # List of words to choose from
#     word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
#     return random.choice(word_list)

# def display_word(word, guessed_letters):
#     # Display the word with dashes for unknown letters
#     display = ""
#     for letter in word:
#         if letter in guessed_letters:
#             display += letter
#         else:
#             display += "_"
#     return display

# def hangman():
#     word_to_guess = choose_word()
#     guessed_letters = []
#     attempts = 6  # Number of attempts before the game is over

#     print("Welcome to Hangman!")
    
#     while attempts > 0:
#         print("\nAttempts left:", attempts)
#         print(display_word(word_to_guess, guessed_letters))

#         guess = input("Guess a letter: ").lower()

#         if len(guess) != 1 or not guess.isalpha():
#             print("Invalid input. Please enter a single letter.")
#             continue

#         if guess in guessed_letters:
#             print("You've already guessed that letter.")
#             continue

#         guessed_letters.append(guess)

#         if guess in word_to_guess:
#             print("Good guess!")
#             if word_to_guess == display_word(word_to_guess, guessed_letters):
#                 print("Congratulations! You've guessed the word:", word_to_guess)
#                 break
#         else:
#             print("Wrong guess.")
#             attempts -= 1

#     if attempts == 0:
#         print("\nOut of attempts. The word was:", word_to_guess)

# if __name__ == "__main__":
#     hangman()


# n = int(input())
# for num in range(1,n+1):
#     print(num,end=' ')