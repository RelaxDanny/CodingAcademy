package lecture_1;

public class Number {

	public static void main(String[] args) {
		System.out.println(1+5);
		System.out.println("Quote: \"I am a boy\"");
		System.out.println("¿µÈ£"+"±è");
		
		int a;
		a = 1;
		System.out.println(a+1);
		
		String first = "coding";
		System.out.println(first + " academy");
		//
		/* 
		
		long -> 8 byte  -9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807
		byte -> 1 byte  -128 ~ 127
		short -> 2 byte -32.768 ~ 32,767
		int -> 4 byte -2,147,483,648 ~ 2,147,483,647
		*/
	}
	
	public static int number(int a, int b) {
		int output;
		output = a + b;
		return output;
	}
	
}