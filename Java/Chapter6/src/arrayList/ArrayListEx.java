package arrayList;

import java.util.ArrayList;

/*	자바에서 제공되는 객체 배열이 구현된 클래스
 *	객체 배열을 사용하는데 필요한 메서드들이 구현되어 있음
 */
public class ArrayListEx {
	public static void main( String[] args ) {
		ArrayList<String> list = new ArrayList<String>();
		
		list.add( "aaa" );
		list.add( "bbb" );
		list.add( "ccc" );
		
		for( int i=0; i<list.size(); i++ ) {
			System.out.println( list.get(i) );
		}
		
		
		for( String lst : list ) {
			System.out.println( lst);
		}
	}
	

}
