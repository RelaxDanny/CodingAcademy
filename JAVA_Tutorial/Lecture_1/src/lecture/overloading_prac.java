package lecture;

class overloadingDemo{
	void A() {
		System.out.println("Void A()");
	}
	void A(int arg1) {
		System.out.println("Void A(int arg1)");
	}
	private void A(String arg1) {
		System.out.println("Void A(String arg1)");
	}
}

public class overloading_prac extends overloadingDemo{
	void A(String arg1, String arg2) {
		System.out.println("void A(String arg1, String arg2)");
	}
	void A() {
		System.out.println("sub class : void A()");
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		overloading_prac od = new overloading_prac();
		od.A();
		od.A(1);
//		od.A("codiung");
		od.A("coding", "KYH");
	}

}
//
//
//overriding: 매개변수는 고정, 메소드의 내용만 바꾸고, 
//	
//overloading: 매게변수의 갯수를 바꿀 수 있는 -> 메소드의 이름이 같음
//
//rule: overriding's signature
//	1. 이름
//	2. 리턴타입
//	3. 매게변수
//
//rule: overloading's signature
//	1. 이름이 같아야함
//	2. 리턴타입이 달라도 됨.