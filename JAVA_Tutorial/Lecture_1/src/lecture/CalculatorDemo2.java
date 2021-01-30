package lecture;

//from tensorflow import Calculator

class Calculator{
	
	int left, right;
	
	public void __init__(int left, int right) {
		this.left = left;
		this.right = right;
	}
	
	public void sum() {
		System.out.println(this.left + this.right );
	}
	
	public int avg() {
		return (this.left + this.right) / 2;
	}
	
}


class Calculator3{
	public static void sum(int left, int right) {
		System.out.println(left+right);
	}
	public static void avg(int left, int right) {
		System.out.println((left+right)/2);
	}
}

public class CalculatorDemo2 {

	public static void main(String[] args) {
		Calculator3.sum(10, 20);
		Calculator3.avg(10, 20);
		
	}

}
