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
		System.out.println( num + "번 지하철의 승객은 " +  cnt + "명 이고  수입은 " + money + "입니다." );
	}
}
