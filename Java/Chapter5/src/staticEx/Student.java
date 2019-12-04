package staticEx;
/*	���α׷� ������ ����
 * 	���� ����			������ġ		������			�޸�	������ �Ҹ�
 * 	��������(���ú���)	�Լ� ���ο� ����	�Լ� ���ο����� ���	����		�Լ��� ȣ��ɶ� ����, ������ �Ҹ�		
 * 	�ɹ�����(�ν��Ͻ�����)	Ŭ���� ��� ����	Ŭ���� ���ο��� ���	��		�ν��Ͻ� ������ ����, ������ �÷��Ͱ� ���Ž� �Ҹ�
 * 	static(Ŭ��������)	static �����	Ŭ���� ���ο��� ���	�����Ϳ���	���α׷��� ���� ����, ���� �Ҹ�
 */	

public class Student {
	public static int serialNum = 1000;
	private int studentId;
	public String studentName;
	public String address;
	
	public Student() {}
	
	public Student( String name ) {
		studentName = name;
		serialNum ++;
		studentId = serialNum;
	}
	 
	public Student( int id, String name ) {
		studentId = id;
		studentName = name;
		address = "�ּ� ����";
		serialNum ++;
	}
	
	public void showStudentInfo() {
		System.out.println( studentName + "," + address );
	} 
	
	public String getStudentName( ) {
		return studentName;
	}
}
