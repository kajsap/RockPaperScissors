#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>

struct Score
{
    int wins;
    int losses;
    int ties;
};

int determineMode(){
    int modes[] = {3, 5, 8};
    int gameMode;

    do
    {
        printf("1) First to 3\n");
        printf("2) First to 5\n");
        printf("3) First to 8\n");
        printf("Which mode do you want to play (1,2,3)? ");

        if (scanf("%d", &gameMode) != 1)
        {
            printf("Please enter a number.\n");

            while (getchar() != '\n')
            {
                continue;
            }
        }
        
        if (gameMode < 1 || gameMode > 3)
        {
           printf("Please choose 1, 2 or 3.\n");
        }
        
    } while (gameMode < 1 || gameMode > 3);
    
    return modes[gameMode -1];
}

char *determineWinner(char *player, char *computer){
    if (strcmp(player, computer) == 0)
    {
        return "tie";
    }
    else if (strcmp(player, "rock") == 0 && strcmp(computer, "scissors") == 0){
        return "player";
    }
    else if (strcmp(player, "paper") == 0 && strcmp(computer, "rock") == 0){
        return "player";
    }
    else if (strcmp(player, "scissors") == 0 && strcmp(computer, "paper") == 0){
        return "player";
    }
    else{
        return "computer";
    }
}

char *playRound(char *moves[], int size){
    char player[20];
    int x = rand() % size;
    char *computer = moves[x];

    int valid = 0;

    while (!valid)
    {
        printf("Enter a choice (rock, paper, scissors): ");
        scanf("%19s", player);

        for (int i = 0; player[i] != '\0'; i++)
        {
            player[i] = tolower(player[i]);
        }
        

        for (int i = 0; i < size; i++)
        {
            if (strcmp(player, moves[i]) == 0)
            {
                valid = 1;
                break;
            }
        }

        if (!valid)
        {
            printf("Invalid choice. Please choose between rock, paper, scissors.\n");
        } 
    }

    printf("Player: %s\n", player);
    printf("Computer: %s\n", computer);

    char *winner = determineWinner(player, computer);
    return winner;
}

void updateScore(char *winner, struct Score *score){
    if (strcmp(winner, "tie") == 0)
    {
        score->ties++;
        printf("It is a tie.\n");
    }
    else if (strcmp(winner, "player") == 0){
        score->wins++;
        printf("You win!\n");
    }
    else{
        score->losses++;
        printf("You lose :(\n");
    }
}

void displayScore(struct Score *score){
    printf("-----------------\n");
    printf("     Score\n");
    printf("-----------------\n");
    printf("Wins: %d\n", score->wins);
    printf("Losses: %d\n", score->losses);
    printf("Ties: %d\n", score->ties);
    printf("-----------------\n");

}

int playAgain(){
    char again;

    printf("Play again (y/n)? ");
    scanf(" %c", &again);

    again = tolower(again);
    return again == 'y';
}

void playGame(){
    char *moves[] = {"rock", "paper", "scissors"};
    struct Score score ={0, 0, 0};
    int size = sizeof(moves) / sizeof(moves[0]);

    int mode = determineMode();
    int endGame = 0;
    int roundNum = 1;

    while (!endGame)
    {
        printf("---- Round %d ----\n", roundNum);
        char *winner = playRound(moves, size);
        updateScore(winner, &score);
        displayScore(&score);

        if (score.wins == mode){
            printf("CONGRATULATIONS YOU WIN!!!\n");
            endGame = 1;
        }
        else if (score.losses == mode){
            printf("OH NO!! The computer won :(\n");
            endGame = 1;
        }

        roundNum += 1;
    }
}

int main(){
    srand(time(NULL));
    int running = 1;
    
    while (running)
    {
        playGame();
        running = playAgain();
    }

    printf("Thanks for playing!");
    return 0;
}