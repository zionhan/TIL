package polymorphism;

public class GoldCustomer extends Customer {	
	double salesRatio;
	
	public GoldCustomer( int customerId, String customerName ) {
		super( customerId, customerName );
		
		customerGrade = "Gold";
		bonusRatio = 0.02;
		salesRatio = 0.1;		
	}
	
	public int calcPrice( int price ) {
		bonusPoint += price * bonusRatio;
		return price - (int)(price * salesRatio);
	}
}
