package array;
/*
 * 	int[] arr = new int[10];
 * 	Book[] library = new Book[5];	// ��ü�� �ּҸ� ��� �迭
 */

public class ObjectArray {
	public static void main( String[] args ) {
		Book[] library = new Book[5];		
		
		
		for( int i=0; i<library.length; i++ ) {
			library[i] = new Book( "�¹ڻ��"+i, "�ѵ���" );			
			System.out.println( library[i] );
			library[i].showBookInfo();
		}
	}
	
}
