package hw;

import java.io.IOException;

public class SortTest {

	public static void main(String[] args) throws IOException {
		int arr[] = { 1, 2, 3, 4, 5 };
		
		Sort sort = null;
		
		System.out.println( "정렬방식을 선택하세요." );
		System.out.println( "B : BubbleSort" );
		System.out.println( "H : HeapSort" );
		System.out.println( "Q : QuickSort" );
		int ch = System.in.read();
		System.out.println( ch );
		System.out.println( 'B' );
		
		if ( ch == 'B' ) {
			sort = new BubbleSort();
		} else if ( ch == 'H' ) {
			sort = new HeapSort();
		} else if ( ch == 'Q' ) {
			sort = new QuickSort();
		} else {
			System.out.println( "잘못된 입력입니다." );
		}
		
		sort.ascending(arr);
		sort.descending(arr);
		sort.description();

	}

}
