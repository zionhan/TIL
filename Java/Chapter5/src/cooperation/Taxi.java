package cooperation;

public class Taxi {
	int num;
	int cnt;
	int money;
	
	public Taxi( int num ) {
		this.num = num;
	}
	
	public void take( int money ) {
		this.money += money;
		this.cnt += 1;
	}
	
	public void showInfo() {
		System.out.println( num + "��  �ý��� �°��� " +  cnt + "�� �̰�  ������ " + money + "�Դϴ�." );
	}
}
