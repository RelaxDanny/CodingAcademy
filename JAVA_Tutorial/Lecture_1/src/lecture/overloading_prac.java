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
//overriding: �Ű������� ����, �޼ҵ��� ���븸 �ٲٰ�, 
//	
//overloading: �ŰԺ����� ������ �ٲ� �� �ִ� -> �޼ҵ��� �̸��� ����
//
//rule: overriding's signature
//	1. �̸�
//	2. ����Ÿ��
//	3. �ŰԺ���
//
//rule: overloading's signature
//	1. �̸��� ���ƾ���
//	2. ����Ÿ���� �޶� ��.