package abstractEx;

public class DeskTop extends Computer {

	@Override
	public void display() {
		// TODO Auto-generated method stub
		System.out.println( "DeskTop display" );		
	}

	@Override
	public void typing() {
		// TODO Auto-generated method stub
		System.out.println( "DeskTop typing" );
	}
	
	public void turnOff() {
		System.out.println( "DeskTop turnOff" );
	}
	
}
