package lecture;

public class lecture_2 {
	
	public static void main(String[] args) {
		
		//String 배열 생성 
		String[] members = {"A", "B", "C"};
		for(String each : members) {
			each += each;
			System.out.println(each);
		}
	}
}
