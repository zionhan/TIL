package inheri;

public class CustomerTest {

	public static void main(String[] args) {
//		Customer lee = new Customer();
//		lee.setCustomerName( "�̼���" );
//		lee.setCustomerId( 10010 );
//		lee.setBonusPoint( 1000 );
//		System.out.println( lee.showCustomerInfo() );
		
		VipCustomer kim = new VipCustomer();
		kim.setCustomerName( "������" );
		kim.setCustomerId( 10020 );
		kim.setBonusPoint( 10000 ); 
		System.out.println( kim.showCustomerInfo() );
	}

}
