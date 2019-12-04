package inheri;

public class OverridingTest {

	public static void main(String[] args) {
		Customer lee = new Customer( 10010, "ÀÌ¼ø½Å" );
		lee.bonusPoint = 1000;
		
		VipCustomer kim = new VipCustomer( 10020, "±èÀ¯½Å" );
		kim.bonusPoint = 10000;
		
		int priceLee = lee.calcPrice(10000);
		int priceKim = kim.calcPrice(10000);
		
		System.out.println( lee.showCustomerInfo() );
		
		System.out.println( kim.showCustomerInfo() );
		
		Customer na = new VipCustomer( 10030, "³ª¸ô¶ó" );
		na.bonusPoint = 10000;
		System.out.println( na.showCustomerInfo() );
	}

}
