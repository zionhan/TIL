package hw;

public class StudentTest {

	public static void main(String[] args) {
		Student lee = new Student( "�̼���" );
		lee.addBook( "�¹���1" );
		lee.addBook( "�¹���2" );
		lee.viewInfo();
		
		System.out.println( "===================" );
		Student kim = new Student( "Kim" );
		kim.addBook( "����1" );
		kim.addBook( "����2" );
		kim.viewInfo();

		Student yee = new Student( "�̼���" );
		yee.addBook( "�¹���1" );
		yee.addBook( "�¹���2" );
		yee.viewInfo();
	}

}
