import random

user_input = input ('Write yout choice rock, paper or scissors: ')
computer = random.choice(['rock', 'paper', 'scissors'])

print(f'You chose {user_input}, computer chose {computer}')
if user_input == computer:
    print(f"Both players selected {user_input}. It's a tie!")
elif user_input == "rock":
    if computer == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_input == "paper":
    if computer == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_input == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")