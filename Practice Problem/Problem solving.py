import random

three_digit = random.randint(100, 999)
tries = 10

while tries > 0 and tries <= 10:
    user_input = input("Enter a 3 digit number: ")

    if len(user_input) == 3:
        tries -= 1
        if int(user_input) == three_digit:
            print("correct guess")
            break
        else:
            print(f"try again you have {tries} tries left")
    else:
        print(f"Enter 3 digit number you entered {len(user_input)} digit number")
