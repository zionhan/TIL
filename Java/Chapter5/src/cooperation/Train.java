package cooperation;

public class Train {
	int num;
	int cnt;
	int money;
	
	public Train( int num ) {
		this.num = num;
	}
	
	public void take( int money ) {
		this.money += money;
		this.cnt += 1;
	}
	
	public void showInfo() {
		System.out.println( num + "�� ����ö�� �°��� " +  cnt + "�� �̰�  ������ " + money + "�Դϴ�." );
	}
}
