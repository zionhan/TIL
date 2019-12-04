package array;
/*
 * Array 논리적위치와 물리적 위치가 같다  => ArrayList 단점 보완.
 * Linked List 는 다르다. 연장이 좋다.
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
