import random 

def determine_winner(player, computer, winning_moves):
    if player == computer:
        winner = "tie"
    elif winning_moves[player] == computer:
        winner = "player"
    else:
        winner = "computer"
    return winner
        

def update_score(winner, score):
    if winner == "tie":
        score["ties"] += 1
        print("It is a tie.")
    elif winner == "player":
        score["wins"] += 1
        print("You win!")
    else:
        score["losses"] += 1
        print(f"You lose :(")

def display_score(score):
    print("-----------------")
    print("     Score")
    print("-----------------")
    for key, value in score.items():
        print(f"{key.capitalize()}: {value}")
    print("-----------------")

      
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

    running = True
    
    while running:
        player = None
        computer = random.choice(list(winning_moves))

        while player not in winning_moves:
            player = input("Enter a choice (rock, paper, scissors): ").lower()

        print(f'Player: {player} \nComputer: {computer}')

        winner = determine_winner(player, computer, winning_moves)
        update_score(winner, score)
        display_score(score)

        play_again = input("Play again? (y/n): ").lower()
        if not play_again == "y":
            running = False

    print("Thanks for playing")

play_game()

