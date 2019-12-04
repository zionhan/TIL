package array;
/*
 * 	int[] arr = new int[10];
 * 	Book[] library = new Book[5];	// 객체의 주소를 담는 배열
 */

public class ObjectArray {
	public static void main( String[] args ) {
		Book[] library = new Book[5];		
		
		
		for( int i=0; i<library.length; i++ ) {
			library[i] = new Book( "태박산맥"+i, "한도경" );			
			System.out.println( library[i] );
			library[i].showBookInfo();
		}
	}
	
}
