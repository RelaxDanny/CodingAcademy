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

//private 함수가 나오면 가장 먼저 private 함수를 호출 하는 public 함수를 찾아라.

public class approach {
	public static void main(String[] args) {
		
		A a = new A();
		System.out.println(a.y());
//		System.out.println(a.z());
		System.out.println(a.x());

	}
}


//
//접근제어자 -> 메소드 기준
//	1. Private -> 내 클래스 안에서만 나를 쓸 수 있음, 내 아들도 못씀
//	2. Default -> 내 클래스와 내 패키지 안에서만 나를 쓸 수 있음 내 아들은 씀 -> 다른 패키지에서 상속 시
//	3. Protected -> 내 클래스, 내 패키지, 남의 패키지에서만 나를 쓸 수 있음 -> 다른패키지와의 상속관계까진 다 됨
//	4. Public -> 남의 패키지 나를 쓸 수 있음 -> 다른패키지이고 상속관계 아님에도 가능.
//	

