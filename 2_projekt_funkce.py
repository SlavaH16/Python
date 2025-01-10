from random import randint

oddelovac = "-" * 50

def heading():
    print("""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Miloslav Houška
email: slava.89@seznam.cz
    """)
    print(oddelovac)
    print("Hi there!")
    print(oddelovac)
    print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
    print(oddelovac)

def ending():
    print(f'''Correct, you've guessed the right number 
in {len(user_tips)} corrects guesses!''')
    print(oddelovac)
    print("That's amazing")   

def secret_number(number1,number2):
    return str(randint(number1,number2))

def user_guess():
    return input("Enter a number: ")

def game():
    for index, number in enumerate(game_number):
            
            if number in user_tip and user_tip[index] == number:
                 result['bulls'] += 1    
            elif number in user_tip and user_tip[index] != number:
                result['cows'] += 1

def print_result():
    if result['bulls'] < 2 and result['cows'] < 2:
        print(f'bull: {result['bulls']}, cow: {result['cows']} ')
        
    if result['bulls'] < 2 and result['cows'] > 1:
        print(f'bull: {result['bulls']}, cows: {result['cows']} ')
        
    if result['bulls'] > 1 and result['cows'] < 2:
        print(f'bulls: {result['bulls']}, cow: {result['cows']} ')

    if result['bulls'] > 1 and result['cows'] > 1:
        print(f'bulls: {result['bulls']}, cows: {result['cows']} ') 

def wrong_value():
    print('''Wrong value. You don't give 4 numeric characters, 
the first number can't be 0 or you enter the same number''')
    
heading()

game_number = secret_number(1000,9999)
game_cont = True
user_tips = []

while game_cont:
    user_tip = user_guess()

    if user_tip.isnumeric() and user_tip[0] != '0' and len(user_tip) == 4 and user_tip not in user_tips:
        user_tips.append(user_tip)
        
        if user_tip == game_number:
            game_cont = False
            break
        
        result = {'bulls': 0, 'cows': 0}
        
        game()

        print_result()

        print(oddelovac)
 
    else:
        wrong_value
 
ending()
