
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;

class RockPaperScissors {

    static Scanner scanner = new Scanner(System.in);
    static Random random = new Random();

    public static int determineMode(){
        int gameMode = 0;

        HashMap<Integer, Integer> modes = new HashMap<>();
        modes.put(1,3);
        modes.put(2,5);
        modes.put(3,8);

        while (!modes.containsKey(gameMode)){
            System.out.println("1) First to 3 \n2) First to 5 \n3) First to 8");

            try{
                System.out.print("Which mode do you want to play (1,2,3)? ");
                gameMode = scanner.nextInt();
                scanner.nextLine();

                if (!modes.containsKey(gameMode)){
                    System.out.println("Please choose 1, 2 or 3.");
                }
            }catch (Exception e){
                System.out.println("Please enter a number.");
                scanner.nextLine();
            }
        } 
        return modes.get(gameMode);  
    }

    public static String playRound(HashMap<String, String> winningMoves){
        List<String> choices = new ArrayList<>(winningMoves.keySet());
        String player = null;
        String computer = choices.get(random.nextInt(choices.size()));

        while (!winningMoves.containsKey(player)){
            System.out.print("Enter a choice (rock, paper, scissors): ");
            player = scanner.nextLine().toLowerCase();

            if (!winningMoves.containsKey(player)){
                System.err.println("Invalid choice. Please choose between rock, paper, scissors.");
            }
        }
        System.out.println("Player: "+ player + "\nComputer: " + computer);

        String winner = determineWinner(player, computer, winningMoves);

        return winner;
    }

    public static String determineWinner(String player, String computer, HashMap<String, String> winningMoves){
        if (player.equals(computer)){
            return "tie";
        }else if (winningMoves.get(player).equals(computer)){
            return "player";
        }else{
            return "computer";
        }
    }

    public static void updateScore(String winner, HashMap<String, Integer> score){
        if (winner.equals("tie")){
            score.put("ties", score.get("ties") + 1);
            System.out.println("It is a tie.");
        }
        else if (winner.equals("player")){
            score.put("wins", score.get("wins") + 1);
            System.out.println("You win!");
        }
        else{
            score.put("losses", score.get("losses") + 1);
            System.out.println("You lose :(");
        }
    }

    public static void displayScore(HashMap<String, Integer> score){
        System.out.println("-----------------");
        System.out.println("     Score");
        System.out.println("-----------------");

        for (Map.Entry<String, Integer> entry: score.entrySet()){
            String key = entry.getKey();
            int value = entry.getValue();

            key = key.substring(0,1).toUpperCase() + key.substring(1);

            System.out.println(key + ": " + value);
        }
        System.out.println("-----------------");
    }

    public static boolean playAgain(){
        System.out.print("Play again (y/n)? ");
        String again = scanner.nextLine().toLowerCase();
        return again.equals("y");
    }

    public static void playGame(){
        HashMap<String, String> winningMoves = new HashMap<>();
        winningMoves.put("rock", "scissors");
        winningMoves.put("paper", "rock");
        winningMoves.put("scissors", "paper");

        HashMap<String, Integer> score = new HashMap<>();
        score.put("wins", 0);
        score.put("losses", 0);
        score.put("ties", 0);

        int mode = determineMode();
        boolean endGame = false;
        int roundNum = 1;

        while (!endGame){
            System.out.println("---- Round " + roundNum + " ----");

            String winner = playRound(winningMoves);
            updateScore(winner, score);
            displayScore(score);

            if (score.get("wins") == mode){
                System.out.println("CONGRATULATIONS YOU WIN!!!");
                endGame = true;
            }
            else if (score.get("losses") == mode){
                System.out.println("OH NO!! The computer won :(");
                endGame = true;
            }

            roundNum += 1;
        }
    }

    public static void main(String[] args){
        boolean running = true;

        while (running){
            playGame();
            running = playAgain();
        }

        scanner.close();
        System.out.println("Thanks for playing!");
    }
}