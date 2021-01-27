package lecture;



class SubtractionableCalculator extends Calculator {
	public SubtractionableCalculator(int a, int b) {
		//»ý¼ºÀÚ -> Constructor
	}
	public void subtract() {
		System.out.println(this.left - this.right);
	}
}

public class inheritance {

	public static void main(String[] args) {
		SubtractionableCalculator c1 = new SubtractionableCalculator(10,20);
		c1.__init__(10,20);
		c1.sum();
		c1.avg();
		c1.subtract();
		
	}

}
