package abstractEx;

public class TestComputer {
	public static void main( String args[] ) {
		
		Computer computer = new DeskTop();
		computer.display();
		computer.turnOn();
		computer.turnOff();
		
	}
}
