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
		
		System.out.println( "Customer( ) ������ ȣ��" );
	}
	
	public Customer( int customerId, String customerName ) {
		this.customerGrade = "Silver";
		this.bonusRatio = 0.01;
		this.customerId = customerId;
		this.customerName = customerName;
		
		System.out.println( "Customer( int, String ) ������ ȣ��" );
	}
	
	
	public int calcPrice( int price ) {
		bonusPoint += price * bonusRatio;
		return price;
	}
	
	public String showCustomerInfo() {
		return customerName + "���� ����� " + customerGrade + "�̸�, ������ ���ʽ� ����Ʈ�� " + bonusPoint + "�� �Դϴ�.";	
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
