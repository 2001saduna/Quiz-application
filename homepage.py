import random
import operator
import time
import csv
from datetime import datetime
# import pandas as pd

difficulty_level = {
    'e': 10,
    'm': 20,
    'h': 30
}

operator_dict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

user_input_name = str(input("What is your name?"))

Username = user_input_name

user_input_difficulty = str(input("Would you like to play on easy, medium, or hard?"
                                  "\nType 'e' for easy, 'm' for medium, or 'h' for hard!")).lower()

if user_input_difficulty not in ['e', 'm', 'h']:
    user_input_difficulty = str(
        input("Hey! You entered the wrong answer - Would you like to play on easy, medium, or hard?"
              "\nType 'e' for easy, 'm' for medium, or 'h' for hard!")).lower()

try:
    user_input_numberofrounds = int(input("How many rounds would you like to play?"))
except ValueError:
    try:
        user_input_numberofrounds = int(
            input("you need to input an INTEGER! - How many rounds would you like to play?"))
    except ValueError:
        print('Your input was wrong - the number of round is set at 3')
        user_input_numberofrounds = 3

user_input_operator = input("What operator would you like?")

score = 0
games_round = 1

start = datetime.now()
while games_round <= user_input_numberofrounds:

    number1 = random.randint(1, difficulty_level[user_input_difficulty])
    number2 = random.randint(1, difficulty_level[user_input_difficulty])
    operator1 = operator_dict[user_input_operator]
    final_answer = operator1(number1, number2)

    try:
        user_answer = float(input(f"What is {number1} {user_input_operator} {number2}?"))
    except ValueError:  # This prevents user entering letters or symboles
        print('You should only enter integers')
        user_answer = float(input(f"What is {number1} {user_input_operator} {number2}?"))

    if user_answer == final_answer:
        score += 1
        print("You are correct")
        print(f'Your current score is :{score}')
    else:
        print("incorrect")
        print(f'The final answer is {final_answer}')
    print(f'this is the {games_round} game')

    games_round = games_round + 1  # games_round += 1

end = datetime.now()
game_time = end - start
print(f'Game finished and your score is {score}')
print(f'You took {game_time} for this game')

with open('user.csv', 'a', newline='') as csvfile:  # a : append
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow([Username, game_time, score])  # row
