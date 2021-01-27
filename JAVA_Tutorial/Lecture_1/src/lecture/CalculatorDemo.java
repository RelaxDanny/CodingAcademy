package lecture;

class Calculator_{
	int left, right, third;
	
	//생성자! 초기화 __init__
	public void __init__(int left, int right) {
		this.left = left;
		this.right = right;
	}
	
	public void __init__(int left, int right, int third) {
		this.left = left;
		this.right = right;
		this.third = third;
	}
	
	public void sum() {
		System.out.println(this.left + this.right);
	}
	
	public void avg() {
		System.out.println((this.left+this.right)/2);
	}
}

public class CalculatorDemo {
	
	public static void main(String[] args) {
		Calculator_ c1 = new Calculator_(); //인스턴스
		//클래스 = 설계도
		//인스턴스 = 제품
		c1.__init__(10, 50);
		c1.sum();
		c1.avg();
		
		Calculator_ c2 = new Calculator_();
		c2.__init__(10, 50, 100);
		c2.sum();
		c2.avg();
	}
	
}

