package object;

class Student {
	int studentNum;
	String studentName;
	
	public Student( int studentNum, String studentName ) {
		this.studentName = studentName;
		this.studentNum = studentNum;
	}
	
	public boolean equals( Object obj ) {
		// TODO Auto-generated method stub
		if( obj instanceof Student ) {
			Student std = ( Student ) obj;			
			return this.studentNum == std.studentNum && this.studentName == std.studentName;
		}		
		return false; 
	}

	
	public int hashCode() {
		return studentNum;
	}	
	
}

public class EqualsTest {
	public static void main( String[] args ) {
		String str1 = new String( "abc" );
		String str2 = new String( "abc" );
		
		System.out.println( str1 == str2 );
		System.out.println( str1.equals( str1 )  );
		
		
		Student lee = new Student( 100, "이순신" );
		Student lee2 = lee;
		Student shin = new Student( 100, "이순신" );
		
		System.out.println( lee == lee2 );
		System.out.println( lee.equals( lee2 ));
		System.out.println( lee == shin );
		System.out.println( lee.equals( shin ) );
		
		
		System.out.println( System.identityHashCode( lee ) );
		System.out.println( System.identityHashCode( shin ) );
		
		System.out.println( lee.hashCode() );
		System.out.println( shin.hashCode() );		
	}
}
