package lecture;

import java.util.Scanner;
import java.io.*;

public class lecture_4 {

	public static void main(String[] args) {
		try {
			File file = new File("C:/Users/danny/Documents/GitHub/CodingAcademy/JAVA_Tutorial/Lecture_1/src/lecture/output.txt");
			Scanner sc = new Scanner(file);
			while(sc.hasNextInt()){
				System.out.println(sc.nextInt() * 1000);
			}
			sc.close();
			
		}
		catch(Exception e) {
			
		}
	}

}
