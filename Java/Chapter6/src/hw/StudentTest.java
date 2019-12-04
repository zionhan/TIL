package hw;

public class StudentTest {

	public static void main(String[] args) {
		Student lee = new Student( "이순신" );
		lee.addBook( "태백산맥1" );
		lee.addBook( "태백산맥2" );
		lee.viewInfo();
		
		System.out.println( "===================" );
		Student kim = new Student( "Kim" );
		kim.addBook( "토지1" );
		kim.addBook( "토지2" );
		kim.viewInfo();

		Student yee = new Student( "이순신" );
		yee.addBook( "태백산맥1" );
		yee.addBook( "태백산맥2" );
		yee.viewInfo();
	}

}
