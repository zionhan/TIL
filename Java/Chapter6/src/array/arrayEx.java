package array;
/*
 * Array ������ġ�� ������ ��ġ�� ����  => ArrayList ���� ����.
 * Linked List �� �ٸ���. ������ ����.
 */

public class arrayEx {	
	
	public static void main( String[] args ) {
//		int[] arr = new int[] { 1, 2, 3 };
		int[] arr = new int[10];
		
		System.out.println( arr );		
		
		for( int i=0, num=1; i<arr.length; i++, num++ ) {
			arr[i] = num;
			System.out.println( arr[i]);
		}
		
		
		char[] chr = new char[26];
		char ch = 'A';
		for( int i=0; i<chr.length; i++ ) {
			chr[i] = ch++;
			System.out.println( chr[i] );
		}
	}
	
}
