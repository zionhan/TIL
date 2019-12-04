package staticEx;

/*	singleton Patter : �� �ϳ��� �����ϴ� �ν��Ͻ�
 * 	�����ڴ� private ����
 * 	static���� ������ ��ü ����
 * 	�ܺο��� ������ ��ü�� ������ �� �ִ� public static get() �ż��� ����
 */

public class Company {
	
	private static Company instance = new Company();
	
	private Company() {}
	
	public static Company getInstance() {
		if( instance == null ) {
			instance = new Company();
		}
		return instance;
	}
	


}
