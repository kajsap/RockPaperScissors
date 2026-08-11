import random

def determine_mode():
    valid = [1, 2, 3]
    game_mode = None
    modes = {
        1: 3, 
        2: 5,
        3: 8
    }

    while game_mode not in valid:
        print("1) First to 3 \n2) First to 5 \n3) First to 8")

        try:
            game_mode = int(input("Which mode do you want to play (1,2,3)?  "))

            if game_mode not in valid:
                print("Please choose 1, 2 or 3")
        except ValueError:
            print("Please enter a number")

    return modes[game_mode]

def play_round(winning_moves):
    player = None
    computer = random.choice(list(winning_moves))

    while player not in winning_moves:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

        if player not in winning_moves:
            print("Invalid choice. Please chose between rock, paper, scissors.")

    print(f'Player: {player} \nComputer: {computer}')
    
    winner = determine_winner(player, computer, winning_moves)

    return winner

def determine_winner(player, computer, winning_moves):
    if player == computer:
        return "tie"
    elif winning_moves[player] == computer:
        return"player"
    else:
        return "computer"
        
def update_score(winner, score):
    if winner == "tie":
        score["ties"] += 1
        print("It is a tie.")
    elif winner == "player":
        score["wins"] += 1
        print("You win!")
    else:
        score["losses"] += 1
        print("You lose :(")

def display_score(score):
    print("-----------------")
    print("     Score")
    print("-----------------")
    for key, value in score.items():
        print(f"{key.capitalize()}: {value}")
    print("-----------------")

def play_again():
    again = input("Play again? (y/n): ").lower()
    return again == "y"

def play_game():
    winning_moves = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    score = {
        "wins": 0,
        "losses": 0,
        "ties": 0
    }

    mode = determine_mode()
    end_game = False
    round_number = 1

    while not end_game:
        print(f"---- Round {round_number} ----")

        winner = play_round(winning_moves)
        update_score(winner, score)
        display_score(score)

        if score["wins"] == mode:
            print("CONGRATULATIONS YOU WIN!!!")
            end_game = True
        elif score["losses"] == mode:
            print("OH NO!! The computer won :(")
            end_game = True

        round_number += 1

def main():
    running = True

    while running:
        play_game()
        running = play_again()

    print("Thanks for playing!")

main()

