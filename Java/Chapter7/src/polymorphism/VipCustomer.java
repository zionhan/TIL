package polymorphism;

public class VipCustomer extends Customer {
	double salesRatio;
	private int agentId;
	
	public VipCustomer() {				
		customerGrade = "VIP";
		bonusRatio = 0.05;
		salesRatio = 0.1;				
		System.out.println( "VIPCustomer( int, String ) ������ ȣ��" );
	}

	public VipCustomer( int customerId, String customerName ) {
		super( customerId, customerName );		
		customerGrade = "VIP";
		bonusRatio = 0.05;
		salesRatio = 0.1;				
		System.out.println( "VIPCustomer( int, String ) ������ ȣ��" );
	}
	
	@Override
	public int calcPrice( int price ) {
		bonusPoint += price * bonusRatio;
		return price - (int)( price * salesRatio );
	}
}
