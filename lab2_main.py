print("This is the Number Analyzer: Decision Maker\n")
divider = '=' * 30 + '\n'
print(divider)

on_off = True
name_input = input("Hello, what is your name? \n")
while (on_off == True):
    input_int = int(input(f"{name_input}, please input a number between 1 and 100: "))
    # if/elif/else statement
    if (1 <= input_int <= 100):
        if (input_int % 2 == 1) and (input_int < 60):  # odd numbers
            print("Odd and less than 60")
        elif(input_int % 2 == 1) and (input_int > 60):
            print("Odd and greater than 60")
        elif(input_int % 2 == 0 and 2 <= input_int <= 24):
            print("Even and less than 25.")
        elif(input_int % 2 == 0 and 26 <= input_int <= 60):
            print("Even and between 26 and 60 inclusive.")
        elif(input_int % 2 == 0 and input_int > 60):
            print("Even and greater than 60")

        question = input(f'{name_input}, would you like to continue? (y/n) ')
        if (question == 'n' or question == 'N'):
            print("Thank you.\n"
                  "<End Program>")
            on_off = False
            break
    elif(input_int > 100):
        print("Number is out of range, please enter a number between 1 and 100")
        question = input("Would you like to continue? (y/n) ")
        if (question == 'n' or question == 'N'):
            print("Thank you.\n"
                  "End Program.")
            on_off = False
            break
    else:
        print('You did not enter a positive integer, or entered zero')
        question = input("Would you like to continue? (y/n) ")
        if (question == 'n' or question =='N'):
            print("Thank you.\n"
                  "End Program.")
            on_off = False
            break

