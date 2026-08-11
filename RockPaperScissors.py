import random 


def determine_winner(player, computer, winning_moves):
    if player == computer:
        winner = "tie"
    elif winning_moves[player] == computer:
        winner = "player"
    else:
        winner = "computer"
    return winner
        

def display_score(winner, score):
    if winner == "tie":
        print(f"It is a tie. \nYour score is {score}")
    elif winner == "player":
        score += 1
        print(f"You win! \nYour score is {score}")
    else:
        print(f"You lose :( \nYour score is {score}")

    return score

      
def play_game():
    winning_moves = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    score = 0
    running = True
    
    while running:
        player = None
        computer = random.choice(list(winning_moves))

        while player not in winning_moves:
            player = input("Enter a choice (rock, paper, scissors): ").lower()

        print(f'Player: {player} \nComputer: {computer}')

        winner = determine_winner(player, computer, winning_moves)
        score = display_score(winner, score)

        play_again = input("Play again? (y/n): ").lower()
        if not play_again == "y":
            running = False

    print("Thanks for playing")

play_game()

