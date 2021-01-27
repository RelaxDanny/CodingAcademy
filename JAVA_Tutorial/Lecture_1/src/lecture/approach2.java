package lecture;



class Calculator5{
	
	private int left, right;
	
	public void __init__(int left, int right) {
		this.left = left;
		this.right = right;
	}
	
	private int sum() {
		return this.left + this.right;
	}
	
	private int avg() {
		return (this.left + this.right) / 2;
	}
	
	public void sumDecoPlus() {
		System.out.println("++++"+sum()+"++++");
	}
	
	public void sumDecoMinus() {
		System.out.println("----"+sum()+"----");
		
	}
	
	public void avgDecoPlus() {
		System.out.println("++++"+avg()+"++++");
	}
	
}

public class approach2 {
	public static void main(String[] args) {
		Calculator5 c1 = new Calculator5();
		c1.__init__(10, 20);
		c1.sumDecoMinus();
		c1.sumDecoPlus();
		c1.avgDecoPlus();
//		c1.sum();
	}
}
