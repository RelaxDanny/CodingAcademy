package lecture;

class A{ // default class
	public String y() {
		return "public void y();";
	}
	
	private String z() {
		return "private void z()";
	}
	
	public String x() {
		return z();
	}
}

//private �Լ��� ������ ���� ���� private �Լ��� ȣ�� �ϴ� public �Լ��� ã�ƶ�.

public class approach {
	public static void main(String[] args) {
		
		A a = new A();
		System.out.println(a.y());
//		System.out.println(a.z());
		System.out.println(a.x());

	}
}


//
//���������� -> �޼ҵ� ����
//	1. Private -> �� Ŭ���� �ȿ����� ���� �� �� ����, �� �Ƶ鵵 ����
//	2. Default -> �� Ŭ������ �� ��Ű�� �ȿ����� ���� �� �� ���� �� �Ƶ��� �� -> �ٸ� ��Ű������ ��� ��
//	3. Protected -> �� Ŭ����, �� ��Ű��, ���� ��Ű�������� ���� �� �� ���� -> �ٸ���Ű������ ��Ӱ������ �� ��
//	4. Public -> ���� ��Ű�� ���� �� �� ���� -> �ٸ���Ű���̰� ��Ӱ��� �ƴԿ��� ����.
//	

