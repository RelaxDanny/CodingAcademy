package lecture;

import java.io.*;

public class lecture_3 {
	
	public static String numbering(int init, int limit) {
		int i = init;
		String ouput = "";
		while (i < limit) {
			ouput += i;
			i++;
		}
		
		return ouput;
	}
	
	public static void main(String[] args) {
		String result = numbering(1,5);
		System.out.println(result);
		
		try {
			BufferedWriter out = new BufferedWriter(new FileWriter("C:/Users/danny/Documents/GitHub/CodingAcademy/JAVA_Tutorial/Lecture_1/src/lecture/output.txt"));
			out.write(result);
			out.close();
		}
		catch(IOException e){
			
		}
	}

}
