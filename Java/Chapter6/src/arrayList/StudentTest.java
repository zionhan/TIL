package arrayList;

public class StudentTest {

	public static void main(String[] args) {
		Student lee = new Student( "이상호" );
		lee.addSubject( "국어", 100 );
		lee.addSubject( "수학", 90 );
		lee.showStudentInfo();
		
		System.out.println("=====================");
		
		Student park = new Student( "박상호" );
		park.addSubject( "국어", 90 );
		park.addSubject( "수학", 80 );
		park.addSubject( "바보", 70 );
		park.showStudentInfo();

	}

}
