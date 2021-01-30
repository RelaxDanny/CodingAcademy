package HW_1;

import java.util.Scanner;

public class ForeignMoney {
	public static void main(String[] args) {

		int dotsToLine = 6;
		int linesToStack = 60;
		int stacksToBrick = 50;
		
		int dots;
		Scanner console = new Scanner(System.in);

		System.out.print("Enter the number of dots: ");
		dots = console.nextInt();

		System.out.println("The number of dots is the same as:");
		
		int bricks = dots / (dotsToLine * linesToStack * stacksToBrick);
		dots = dots % (dotsToLine * linesToStack * stacksToBrick);

		int stacks = dots / (dotsToLine * linesToStack);
		dots = dots % (dotsToLine * linesToStack);

		int lines = dots / dotsToLine;
		dots = dots % dotsToLine;

		System.out.println(bricks + " bricks");
		System.out.println(stacks + " stacks");
		System.out.println(lines + " lines");
		System.out.println(dots + " dots");
	}
}
