package inheri;

public class Customer {
	private int customerId;
	private String customerName;
	protected String customerGrade;
	int bonusPoint;
	double bonusRatio;
	
	public Customer() {
		this.customerGrade = "Silver";
		this.bonusRatio = 0.01;		
		
		System.out.println( "Customer( ) 생성자 호출" );
	}
	
	public Customer( int customerId, String customerName ) {
		this.customerGrade = "Silver";
		this.bonusRatio = 0.01;
		this.customerId = customerId;
		this.customerName = customerName;
		
		System.out.println( "Customer( int, String ) 생성자 호출" );
	}
	
	
	public int calcPrice( int price ) {
		bonusPoint += price * bonusRatio;
		return price;
	}
	
	public String showCustomerInfo() {
		return customerName + "님의 등급은 " + customerGrade + "이며, 적립된 보너스 포인트는 " + bonusPoint + "점 입니다.";	
	}
	

	public int getCustomerId() {
		return customerId;
	}

	public void setCustomerId(int customerId) {
		this.customerId = customerId;
	}

	public String getCustomerName() {
		return customerName;
	}

	public void setCustomerName(String customerName) {
		this.customerName = customerName;
	}

	public String getCustomerGrade() {
		return customerGrade;
	}

	public void setCustomerGrade(String customerGrade) {
		this.customerGrade = customerGrade;
	}

	public int getBonusPoint() {
		return bonusPoint;
	}

	public void setBonusPoint(int bonusPoint) {
		this.bonusPoint = bonusPoint;
	}

	public double getBonusRatio() {
		return bonusRatio;
	}

	public void setBonusRatio(double bonusRatio) {
		this.bonusRatio = bonusRatio;
	}
	
}
