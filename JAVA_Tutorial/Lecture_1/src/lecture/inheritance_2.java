package lecture;


class Calculator4{
	int left, right;
	
//	public Calculator4() {}
	
	public Calculator4(int left, int right) {
		this.left=left;
		this.right=right;
	}
	
	public void sum() {
		System.out.println(this.left + this.right);
	}
	
	public void avg() {
		System.out.println((this.left+this.right)/2);
	}
}

class subCal extends Calculator4{
	
	public subCal(int left, int right) {
		super(left, right);
	}
	
	public void subtract() {
		System.out.println(this.left - this.right);
	}
}

public class inheritance_2 {
		
	public static void main(String[] args) {
		subCal c1 = new subCal(10,20);
		c1.sum();
	}

}
