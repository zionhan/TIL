package set;

import java.util.Comparator;
import java.util.TreeSet;

// 이미 Comparable이 구현된 경우 Comparator를 이용하여 다른 정렬 방식을 정의할 수 있음.
// ex) String 역순 정렬
class MyCompare implements Comparator<String> {
	@Override
	public int compare(String o1, String o2) {		
		return o1.compareTo(o2)*(-1);
	}
}

public class ComparatorTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		TreeSet<String> treeSet = new TreeSet<String>( new MyCompare() );
		
		treeSet.add( "홍길동" );
		treeSet.add( "강감찬" );
		treeSet.add( "이순신" );
		
		for( String str : treeSet ) {
			System.out.println( str );
		}
	}
}
