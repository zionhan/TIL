package hiding;

/*	���� ����
 *	���� ������(  access modifier )
 *	����, �޼���, �����ڿ� ���� ���� ���� ����
 * 	public, private, protected, �ƹ��͵� �Ⱦ��� ���( default )
 */


/*	this�� ����
 * 	�ڽ��� �޸𸮸� ����Ŵ
 * 	�����ڿ��� �ٸ� �����ڸ� ȣ�� ��
 * 	�ν��Ͻ� �ڽ��� �ּҸ� ��ȯ
 */

public class MyDate {
	private int day;
	private int month;
	private int year;
	
	public void setDay( int day ) {
		this.day = day;
	}
	
	public int getDay() {
		return day;
	}
	
	
	public int getMonth() {
		return month;
	}

	public void setMonth(int month) {
		this.month = month;
	}

	public int getYear() {
		return year;
	}

	public void setYear(int year) {
		this.year = year;
	}

	public void showDate() {
		System.out.println( year + "��" + month + "��");
	}
}
