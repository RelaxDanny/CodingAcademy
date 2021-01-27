package HW_1;

import java.util.Scanner;

public class WhatDay {
  public static void main(String[] args) {

    Scanner console = new Scanner(System.in);
    System.out.print("Enter the year (e.g. 1968): ");
    int year = console.nextInt();
    System.out.print("Enter month (1-12): ");
    int month = console.nextInt();
    if (month <= 2) {
      month += 12;
      year -= 1;
    }
    System.out.print("Enter the day of the month (1-31): ");
    int day = console.nextInt();

    int k = year % 100;
    int j = year / 100;

    int number = (day + (13*(month+1))/5 + k + k/4 + j/4 + 5*j) % 7;
    String dayName = "";
    if (number == 0) {
      dayName = "Saturday";
    }
    else if (number == 1) {
      dayName = "Sunday";
    }
    else if (number == 2) {
      dayName = "Monday";
    }
    else if (number == 3) {
      dayName = "Tuesday";
    }
    else if (number == 4) {
      dayName = "Wednesday";
    }
    else if (number == 5) {
      dayName = "Thursday";
    }
    else if (number == 6) {
      dayName = "Friday";
    }

    System.out.println("The day of the week is " + dayName);
  }
}
