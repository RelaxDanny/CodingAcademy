package lecture;


final class subsub extends Calculator {
	public void sum() {
		System.out.println("���� �����" + (this.left+this.right)+ "�Դϴ�.");
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
//		overriding -> �������̵� �������� �Ƶ��� �ٲٴ°� 
		subsub c1 = new subsub();
		
		System.out.println(c1);
		c1.__init__(10,20);
		c1.sum();
		c1.avg();
		c1.subtract();
		//�޼ҵ��� �̸��� ���ƾ���
		//�޼ҵ��� �Ű������� ���ڿ� ������Ÿ�� ����, �Ű������� ����
		//�޼ҵ��� ���� Ÿ
	}

}

