# class Person:
#     def init(self,fn,ln,age,add):
#         self.firstname = fn
#         self.lastname = ln
#         self.age = age
#         self.address = add

# P1 = Person('Binay','Parajuli', 'Pokhara', 20)
# print(P1)
# print(P1.address)
# P1.age =10
# print(P1.age)

# class Student:
#     def init(self,fn,ln,roll,age,add):
#         self.firstname = fn
#         self.lastname = ln
#         self.age = age
#         self.roll_number = roll
#         self.address = add

# s1 = Student('binay', 'parajuli',23,15,'pokhara')
# s2 = Student('yanib','ilujarap',32,51,'arahkop')

# print(s2.age)

# class Human:
#     hand = 2
#     def init(self,fn,ln,age):
#         self.first_name = fn
#         self.last_name = ln
#         self.age = age
        
# h1 = Human('binay','parajuli',23)
# # del h1.first_name
# print(h1.first_name)
# print(Human.hand)

# class NMB_Bank:
#     bank_name = "NMB"
#     bank_headquater = "Kathmandu"
#     bank_CEO = "John Doe"
#     def init(self,fn,ln,age,address):
#         self.firstname = fn
#         self.lastname = ln
#         self.age = age
#         self.address = address
    
#     def get_full_name(self): 
#         return f'{self.firstname} {self.lastname}'
#     def get_address(self):
#         print(self.get_full_name())
#         print(self.bank_name)
#     @classmethod
#     def get_bank_name(cls):
#         print(e1.get_address())
#         return cls.bank_name
        
#     @classmethod
#     def get_headquarter(cls):
#         return cls.bank_headquater.capitalize()
#     @classmethod
#     def get_CEO(cls):
#         print(NMB_Bank.get_bank_name())
#         return cls.bank_CEO.capitalize()
#     @staticmethod
#     def call(a,b):
       
#         print(e1.get_full_name())
#         print(e1.get_address())
#         print(NMB_Bank.get_bank_name())
#         print(NMB_Bank.get_headquarter())
#         print(NMB_Bank.get_CEO())
#         print(a+b)
        
# e1 = NMB_Bank('binay', 'parajuli',23,'pokhara')
# print(e1.get_full_name())
# print(e1.get_address())
# print(NMB_Bank.get_bank_name())
# print(NMB_Bank.get_headquarter())
# print(NMB_Bank.get_CEO())
# NMB_Bank.call(1,2)

######################################

# class StudentInfo:
#     __school_name = "Global School"
#     __school_address = "Pokhara"
    
#     def __init__(self,fn,ln,roll):
#         self.__firstname = fn
#         self.__lastname = ln
#         self.__rollno = roll
    
#     def get_rollno(self):
#         print(self.__rollno)
    
#     def set_rollno(self,new_roll):
#         if new_roll > 0:
#             self.__rollno = new_roll
#         else:
#             print("Invalid")
        
#     def get_name(self):
#         self.get_rollno()
#         print(f'{self.__firstname} {self.__lastname}')
        
#     @classmethod
#     def get_school_name(cls):
#         print(StudentInfo.__school_name)
    
#     @classmethod
#     def get_school_address(cls):
#         StudentInfo.get_school_name()
#         print(StudentInfo.__school_address)
    
    
# s1 = StudentInfo("binay", "parajuli", 17)

# StudentInfo.get_school_address()
# s1.set_rollno(15)
# s1.get_rollno()


#########inheritance

# class Employee:
#     def __init__(self,fn):
#         self.__first = fn
#     def get(self):
#         print("Parent")
    
# class FulltimeEmployee(Employee):
#     pass
#     # def get(self):
#     #     print("Chid")
# f1 = FulltimeEmployee("binay")
# f1.get()


#####################################################
#Bank Application

# class Bank:
#     __interest = 12
#     __government_holidays = ["New Year", "dashian", "Tihar", "Saturdays", "Holi"]
    
#     def __init__(self,fn,ln,add):
#         self.__firstname = fn
#         self.__lastname = ln
#         self.__addresss = add
#         self.__balance = 0
    
#     def account_info(self):
#         return {'fn': self.__firstname.capitalize(), 'ln': self.__lastname, 'address': self.__addresss, 'balance': self.__balance}
        
#     def check_balance(self):
#         return f'Hello {self.__firstname.capitalize()} . Your current balance: {self.__balance}'
    
#     def deposit(self, new_balance):
#         if new_balance > 0:
#             self.__balance += new_balance
#             return True
    
#     def withdraw(self,withdraw_balance):
        
#         if self.__balance == 0 or self.__balance < withdraw_balance:
#             return None
#         self.__balance -= withdraw_balance

#     @classmethod
#     def get_holidays(cls):
#         return cls.__government_holidays
#     @staticmethod
#     def get_interest():
#         return Bank.__interest
#     @staticmethod
#     def change_interest(new_interest):
#         if new_interest != 0:
#             Bank.__interest = new_interest
#             return True
        
         
    
# # c1 = Bank("binay", "parajuli","pokhara")
# c1 = None
# # print(" 1.Cheak Balance\n 2.Deposit\n 3.Withdraw\n 4.Holiday List\n 5.Interest value\n 6.Exit")
# while True:
    
#     try:
#         print('#'*50)
#         n = input("0.Open account\n 1.Cheak Balance\n 2.Deposit\n 3.Withdraw\n 4.Holiday List\n 5.Interest value\n 6.Exit\n")
        

#         if n=='0' and c1 is not None:
#             fn = input("Enter first nane: ")
#             ln = input("Enter last nane: ")
#             add = input("Enter adddress: ")
#             c1 = Bank(fn,ln,add)
#             print("YOUR AccOUNT HAS BEEN CREATED")
#             info = c1.account_info()
#             print(f"firstname = {info['fn']},lastname = {info['ln'].capitalize()}, address = {info['address']}, balance = {info['balance']}")
#         elif n=='1' and c1 is not None:    
#             if '1'  :
#                 print(c1.check_balance())
                
#         elif n=='2' and c1 is not None:
#                 d_amount = int(input("Enter th amount you want to deposit: "))
#                 result = c1.deposit(d_amount)
#                 if result  is None:
#                     print("Amount should be greater than 0")
#                 else:
#                     print(c1.check_balance())
#         elif n=='3' and c1 is not None:
#             w_amount = int(input("Enter the amount you want to withdraw: "))
#             result = c1.withdraw(w_amount)
#             if result is None:
#                 print("fuck you")
#             else:
#                 print(c1.check_balance())
#         elif n=='4':
#             print(Bank.get_holidays())
#         elif n=='5':
#             print(Bank.get_interest())
#         elif n=='7':
#             new_interest = int(input("enter new interest: "))
#             result = Bank.change_interest(new_interest)
#             if result is None:
#                 print("Must be more ")
#             else:
#                 print(f"New interset is {result}")
                
            
#         elif n=='6':
#             print("Thank you!")
#             break
#         elif c1 is None:
#             print("Enter data")
        
        
#     except Exception as e:
#         print("Enter a integer")


