package multiInheriClass;

public class CustomerTest {

	public static void main(String[] args) {
		Customer customer = new Customer();
		
		customer.buy();
		customer.sell();
		customer.order();
		customer.sayHello();
		
		Buy buyer = customer;
		buyer.buy();
		buyer.order();		
		
		Sell seller = customer;
		seller.sell();
		seller.order();
		
		if( seller instanceof Customer ) {
			((Customer) seller).sayHello();
			((Customer) seller).buy();
			
		}

	}

}