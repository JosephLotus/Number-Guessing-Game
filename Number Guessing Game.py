import random

logo = '''
 _____                       _   _            _   _                 _               
|  __ \                     | | | |          | \ | |               | |              
| |  \/_   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | __| | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |_\ \ |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
 \____/\__,_|\___||___/___/  \__|_| |_|\___| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                    
'''


game_over = False

def compare_numbers(secret, player):
    if secret == player:
        return "You are correct!"
    elif player < secret:
        return "Too low."
    elif player > secret:
        return "Too high."

while game_over == False:
    print (logo)
    print ("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")
    secret_number = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    guesses_remaining = 10
    if difficulty == 'hard':
        guesses_remaining = 5
    player_guess = '0'
    while guesses_remaining > 0 and player_guess != secret_number:
        print(f"You have {guesses_remaining} attempts remaining to guess the number.")
        player_guess = int(input("Make a guess: "))
        print (compare_numbers(secret_number, player_guess))
        guesses_remaining -= 1
        if guesses_remaining > 0:
            print ("Guess again.")
    if guesses_remaining == 0:
        print(f"You lose. The secret number was {secret_number}.")
    play_again = input("Would you like to play again? Type 'y' for yes or 'n' for no: ")
    if play_again == 'n':
        game_over = True

print("Thanks for playing!")