package abstractEx;

public abstract class Computer {
//	public void display() {}   => 추상메서드가 아니다
	
	public abstract void display();	
	public abstract void typing();
	
	
	public void turnOn() {
		System.out.println( "전원을 켭니다." );
	}
	
	public void turnOff() {
		System.out.print( "전원을 끕니다." );
	}
}
