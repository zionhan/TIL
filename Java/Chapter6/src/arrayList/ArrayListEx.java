package arrayList;

import java.util.ArrayList;

/*	�ڹٿ��� �����Ǵ� ��ü �迭�� ������ Ŭ����
 *	��ü �迭�� ����ϴµ� �ʿ��� �޼������ �����Ǿ� ����
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
