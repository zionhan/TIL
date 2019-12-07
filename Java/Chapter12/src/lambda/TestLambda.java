package lambda;

interface PrintString {
	void showString( String str );	
}


public class TestLambda {
	public static void main( String[] args ) {
		PrintString lambdastr = s -> System.out.println( s );
		lambdastr.showString("Test");
		
		showMyString( lambdastr );
		
		PrintString test = returnString();
		test.showString( "Test3" );
	}

	
	public static void showMyString( PrintString p ) {
		p.showString( "Test2" );
	}
	
	public static PrintString returnString() {
		return s -> System.out.println( s+ "!!!" );
	}
}
