package reference;

public class StudentTest {
	public static void main( String[] args ) {
		Student lee = new Student( 15, "이순신" );
		Student park = new Student( 14, "박유신" );
		
		
		lee.kor.setSjt(100);
		lee.math.setSjt(100);
		
		lee.showScore();
	}
}


