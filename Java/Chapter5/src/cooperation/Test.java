package cooperation;

public class Test {
	public static void main( String[] args ) {
		Student Edward = new Student( "Edward", 20000 );
		
		Taxi taxi = new Taxi( 500 );
		
		Edward.takeTaxi( taxi );
		
		Edward.showInfo();
		taxi.showInfo();
		

		
	}

}
