package classpart;

public class StudentTest {
	public static void main( String[] args ) {
		Student lee = new Student();
		// �ν��Ͻ� ������ �ɹ��������� Heap �޸� ������ �Ҵ� ( ���� �޸� )
		// Garbage Collector( Thread ) 
		
		lee.studentName = "�ѵ���";
		lee.address = "����";
		lee.showStudentInfo();
		
		Student kim = new Student();
		kim.studentName = "�赵��";
		kim.address = "����";
		
		System.out.println( lee );	// JVM �� �Ҵ��� ���� hash ��
		System.out.println( kim );
		
	}
}