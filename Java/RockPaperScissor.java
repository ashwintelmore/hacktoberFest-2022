package practice;

import java.util.Random;
import java.util.Scanner;

public class RockPaperScissor {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        Random r = new Random();

        int ComputerPoints = 0, HumanPoints = 0;


        for (int i = 0; i < 5; i++) {
            System.out.print("1.Rock\n2.Paper\n3.Scissor\nEnter Your Choice: ");
            int HumanChoice = sc.nextInt();
            int CompChoice = r.nextInt(1,4);

            if (HumanChoice == CompChoice){
                System.out.println("Draw..");
                i--;
            }else if (HumanChoice == 1 && CompChoice == 2 || HumanChoice== 2 && CompChoice == 3 || HumanChoice== 3 && CompChoice == 1){
                HumanPoints++;
            }else{
                ComputerPoints++;
            }

        }

        if (ComputerPoints > HumanPoints){
            System.out.println("Computer Win..");
        }else{
            System.out.println("Human Win..");
        }
        sc.close();
    }
}


/*

1 1 --> draw
1 2 --> player 1 win
1 3 --> player 2 win
2 1 --> player 2 win
2 2 -->draw
2 3 --> player 1 win
3 1 --> player 1 win
3 2 --> player 2 win
3 3 --> draw

 */
