package arrayList;

public class StudentTest {

	public static void main(String[] args) {
		Student lee = new Student( "�̻�ȣ" );
		lee.addSubject( "����", 100 );
		lee.addSubject( "����", 90 );
		lee.showStudentInfo();
		
		System.out.println("=====================");
		
		Student park = new Student( "�ڻ�ȣ" );
		park.addSubject( "����", 90 );
		park.addSubject( "����", 80 );
		park.addSubject( "�ٺ�", 70 );
		park.showStudentInfo();

	}

}
