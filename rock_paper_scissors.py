
import random

computer_guess = random.choice(['rock', 'paper', 'scissors'])
user_guess = input('Which one do you choose: rock, paper or scisors?\n')

if computer_guess == user_guess:
    print("It's a tie! Computer chose " + computer_guess)
elif user_guess == 'rock' and computer_guess == 'scissors':
    print('You win! Computer chose ' + computer_guess)
elif user_guess == 'paper' and computer_guess == 'rock':
    print('You win! Computer chose ' + computer_guess)
elif user_guess == 'scissors' and computer_guess == 'paper':
    print('You win! Computer chose ' + computer_guess)
else:
    print('You lose! Computer chose ' + computer_guess)
