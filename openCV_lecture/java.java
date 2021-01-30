package project;
import java.util.Scanner;
public class Salary {
    public static void main (String[]arg) {
        Scanner sc = new Scanner(System.in);
        String corporate = "c";
        String hourly = "h";
        String sales = "s";
        System.out.print("Select employee type: (c) corporate (h) hourly (s)sales : ");
        String name = sc.nextString(); 
        if(name == "c"){
            // System.out.print("Select employee type: (c) corporate (h) hourly (s)sales : c");
            System.out.println("Enter weekly sales : ");
            double weekly_salary = sc.nextDouble(); // 무조건 소수로 바꾼다.
            double tax = weekly_salary * (145/1000);
            System.out.print("Gross pay : " + weekly_salary);
            System.out.print("Taxes :" + tax);
            System.out.print("Net pay :" + weekly_salary - tax);
        }
        if(name == "h"){

        }
        if(name == "s"){
            
        }
    }
}

//String = 문자열 = 영어
//int = 정수 = -1, 0, 1
//double = 소수 = 1.1, 0.0, 0.1
