package lecture;


final class subsub extends Calculator {
	public void sum() {
		System.out.println("실행 결과는" + (this.left+this.right)+ "입니다.");
	}
	
	public int avg() {
		return super.avg();
	}
	
	public void subtract() {
		System.out.println(this.left-this.right);
	}
}

public class overriding_prac {

	public static void main(String[] args) {
//		overriding -> 오버라이딩 엄마꺼를 아들이 바꾸는거 
		subsub c1 = new subsub();
		
		System.out.println(c1);
		c1.__init__(10,20);
		c1.sum();
		c1.avg();
		c1.subtract();
		//메소드의 이름이 같아야함
		//메소드의 매개변수의 숫자와 데이터타입 숫자, 매개변수의 순서
		//메소드의 리턴 타
	}

}

