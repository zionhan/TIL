package cooperation;

public class Bus {
	int num;
	int cnt;
	int money;
	
	public Bus( int num ) {
		this.num = num;
	}
	
	public void take( int money ) {
		this.money += money;
		this.cnt += 1;		
	}
	
	public void showInfo() {
		System.out.println( num + "�� ������ �°��� " +  cnt + "�� �̰�  ������ " + money + "�Դϴ�." );
	}
	
}
