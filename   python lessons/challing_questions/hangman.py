# import random
# def choose_word():
#     word =['binay','raj','parajuli']
#     return random.choice(word)
# def display(word, letter):
#     display = ""
#     for l in word:
#         if l in letter:
#             display += letter
#         else:
#             display += '-'
#     return display
# def hangman():
#     word_to_guess = choose_word()
#     attempts = 6
     
#     while attempts> 0:
#         letter = input("Enter the letter: ")
#         print(display(word_to_guess,word))
#         print(attempts)
        
        
#         if letter in display(word_to_guess,letter):
#             print("Good guess")
#             if word_to_guess == display(word_to_guess,letter):
#                 print("congo",word_to_guess)
            
            
#         else:
#             attempts -= 1
        
# hangman()           