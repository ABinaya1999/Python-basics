# def palindrime_check(string):
#     string.replace(" ", '')
#     return string == string[::-1]
# while True:
#     string = input("Enter the string: ")
#     if palindrime_check(string):
#         print("is palindrome")
#         break
#     else:
#         print('not')
# print("Thanks")


# ***************************************************
# import random
# responses = {
#     "hello": ["Hello!", "Hi there!", "Hey!"],
#     "how are you": ["I'm good, thanks!", "I'm just a computer program, so I don't have feelings, but I'm here to help!"],
#     "weather": ["I'm sorry, I cannot provide weather information at the moment."],
#     "bye": ["Goodbye!", "See you later!", "Bye!"]
# }
       
# def response(user_input):
#     user_input.lower()
#     response=responses.get(user_input,["noo"])
#     return random.choice(response)
    
while True:
    user_input = input("You: ")
    if user_input == "bye":
        print("Chatbot: Goodbye!")
        break
    else:
        chatbot = response(user_input)
        print("Chatbot: ",chatbot)   
    
# import random

# responses = {
#     "hello": ["Hello!", "Hi there!", "Hey!"],
#     "how are you": ["I'm good, thanks!", "I'm just a computer program, so I don't have feelings, but I'm here to help!"],
#     "weather": ["I'm sorry, I cannot provide weather information at the moment."],
#     "bye": ["Goodbye!", "See you later!", "Bye!"]
# }

# def response(user_input):
#     user_input = user_input.lower()  # Convert user input to lowercase
#     response = responses.get(user_input,[ "I'm sorry, I don't understand that."])  # Provide a default response as a string
#     return random.choice(response)

# while True:
#     user_input = input("You: ")
#     if user_input == "bye":
#         print("Chatbot: Goodbye!")
#         break
#     else:
#         chatbot = response(user_input)
#         print("Chatbot:", chatbot)
