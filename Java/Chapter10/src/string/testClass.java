package string;

public class testClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = 5;
		int i,j;
		int x = 0;
		
		for ( i=0; i<n ; i++ ) {
			for( j=0; j<= i; j++ ) {
				x = x+j+1;
			}
		}
		System.out.println( x );

	}

}
