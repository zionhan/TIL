package inheri;

public class OverridingTest {

	public static void main(String[] args) {
		Customer lee = new Customer( 10010, "�̼���" );
		lee.bonusPoint = 1000;
		
		VipCustomer kim = new VipCustomer( 10020, "������" );
		kim.bonusPoint = 10000;
		
		int priceLee = lee.calcPrice(10000);
		int priceKim = kim.calcPrice(10000);
		
		System.out.println( lee.showCustomerInfo() );
		
		System.out.println( kim.showCustomerInfo() );
		
		Customer na = new VipCustomer( 10030, "������" );
		na.bonusPoint = 10000;
		System.out.println( na.showCustomerInfo() );
	}

}
