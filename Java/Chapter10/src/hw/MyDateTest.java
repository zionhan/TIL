package hw;


class MyDate {
	int day;
	int month;
	int year;
	
	public MyDate( int day, int month, int year ) {
		this.day = day;
		this.month = month;
		this.year = year;
	}
	
	public boolean equals( Object obj ) {
		if( obj instanceof MyDate ) {
			MyDate date = ( MyDate ) obj;
				return this.year == date.year && this.day == date.day && this.month == date.month ;
		}				
		return false;
	}

	@Override
	public int hashCode() {		
		return this.day + this.month + this.year;
	}
	
	
	
}


public class MyDateTest {

	public static void main(String[] args) {
		
		MyDate date1 = new MyDate( 5, 12, 2019 );
		MyDate date2 = new MyDate( 5, 12, 2019 );
		
		System.out.println( date1.equals( date2 ) );
		
		System.out.println( date1.hashCode() );
		System.out.println( date2.hashCode() );

	}

}
