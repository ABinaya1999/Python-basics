#change the case of characters
# print("BINAY".lower())
# print("binay".upper())
# print("binay".capitalize())
# print("binay parajuli".title())

#replace
# print("binay parajuli".replace("binay","raj"))

# split
# a = "a,b,c,d"
# print(a.split(","))

#strip
# a = "           a aaa aa        "
# print(a.strip())

#format
# a = 10
# print("the result {}".format(a))

# cost_of_ice_bag = 1.25
# profit_margin = .2
# number_of_bags = 50
# total_profit = cost_of_ice_bag * profit_margin * number_of_bags
# output_message = "{} {} {} {}"
# print(output_message.format(cost_of_ice_bag, profit_margin * 100, number_of_bags, total_profit))

# print ("the" + str(cost_of_ice_bag) + str(profit_margin) + str(number_of_bags))

# a = True
# print(str(a)+ "1" )

# string_name = "Binay"
# print(string_name[1:3])
# for char in string_name:
#     print(char)

# string_name = "Deerwalk Institute of Technology"
# print(string_name[:8], string_name[9:18], string_name[22:])
# print("Deerwalk" in string_name)

# list_name = [1, 2, 3, 4]
# print(list_name[1:3])
# print(len(list_name))

# print(list(("a","a")))

# dictionary_name = {
#     1: 'key1',
#     2: 'key2'
# }
# print(dictionary_name[1])
# print(len(dictionary_name))
# print(1 in dictionary_name)
# dictionary_name[3] = 'key3'
# print(dictionary_name)

# print(list(range(10,15)))
# print(list(range(10, 21, 2)))

# dictionary_name = {
#     'ram': 25,
#     'shyam': 35,
#     'hari': 85,
#     'rita' : 68
# }
# name = input("Enter the name: ").lower()
# print(f"Hi {name.capitalize()}. Your grade is {dictionary_name[name]} ")

# number = int(input("Enter the number from user: "))
# print(list(range(0, number + 1, 2)))

# result = True if number % 2 == 0 else False
# print(result)

# if number % 5 == 0:
#     print(True)

# for item in range(2, 10):
#     print(item)

# names = ['ram', 'shyam', 'hari', 'rita', 'sita', "Hunter"]

# for name in names.startswith('h') or names.startswith('H'):
#     print(name)

name = input("Enter name: ")
print(f"Good Afternoon {name.capitalize()}")