package staticEx;

import java.util.Calendar;

public class CompanyTest {
	public static void main( String[] args ) {
//		Company company = new Company();
		Company company1 = Company.getInstance();
		Company company2 = Company.getInstance() ;
		
		
//		System.out.println( company );
		System.out.println( company1 );
		System.out.println( company2 );
		
		Calendar calendar = Calendar.getInstance();
		System.out.println( calendar );
		
	}
}
