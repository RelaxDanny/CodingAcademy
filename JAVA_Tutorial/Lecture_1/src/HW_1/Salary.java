package HW_1;

import java.util.Scanner;

public class Salary {
	public static void main(String[] args) {

		double hourlyWage;
		double hoursWorked;
		double weeklySales;
		double grossPay = 0;
		double taxes;

		Scanner console = new Scanner(System.in);

		System.out.print("Select employee type: (c) corporate (h) hourly (s) sales: ");
		String employeeType = console.next();
		System.out.println("Type:" + employeeType);
		if (employeeType.equals("c")) {
			System.out.print("Enter weekly salary: ");
			grossPay = console.nextDouble();

		} else if (employeeType.equals("h")) {
			System.out.print("Enter hourly wage: ");
			hourlyWage = console.nextDouble();
			System.out.print("Enter hours worked: ");
			hoursWorked = console.nextDouble();
			grossPay = hourlyWage * hoursWorked;
			// They earn 2x over 40 hours, so add in their wage a second time
			if (hoursWorked > 40) {
				grossPay += (hoursWorked - 40) * hourlyWage;
			}
		}
		else if (employeeType.equals("s")) {
			System.out.print("Enter weekly sales: ");
			weeklySales = console.nextDouble();
			grossPay = 500 + 0.06*weeklySales;
		}

		System.out.printf("Gross pay: $%.2f\n", grossPay);

		taxes = grossPay * 0.145;
		System.out.printf("Taxes: $%.2f\n", taxes);

		System.out.printf("Net pay: $%.2f\n", grossPay-taxes);

	}
}
