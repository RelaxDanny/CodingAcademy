package HW_1;

import java.util.Scanner;
import java.lang.Math.*;

public class Cylinder {
	public static void main(String[] args) {
		double radius;
		double height;

		Scanner console = new Scanner(System.in);
		System.out.print("Enter the radius of a cylinder(in cm): ");
		radius = console.nextDouble();
			
		System.out.print("Enter the height of the cylinder(in cm): ");
		height = console.nextDouble();

		double surfaceArea = 2*Math.PI*radius*height + 2*Math.PI*radius*radius;
		System.out.printf("The surface area of a cylinder is: %.2f sq. cm\n", surfaceArea);

	}
}
