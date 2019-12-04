package thisEx;

public class Test {
	public static void main( String[] args ) {
		Person lee = new Person();
		lee.showInfo();
		
		Person hong = new Person( "ȫ�浿", 44 );
		hong.showInfo();
		
		System.out.println( lee );
		System.out.println( lee.getSelf() );
	}
}
