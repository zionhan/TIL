package array;

public class ObjectDeepCopy {
	public static void main( String[] args ) {
		Book[] library = new Book[5];	
		Book[] copyLibrary = new Book[5];
		
		
		for( int i=0; i<library.length; i++ ) {
			library[i] = new Book( "태박산맥"+i, "한도경" );
			copyLibrary[i] = new Book( library[i].getTitle(), library[i].getAuthor() );
			// 깊은 복사. 주소 복사가 아니라 새로운 인스터에 값을 입력
		}

		library[0].setTitle( "나목" );
		library[0].setAuthor( "박완서" );
		
		// 향상된 for문ㄴㅁ
		for( Book book : library ) {
			book.showBookInfo();
		}
		
		for( Book book : copyLibrary ) {
			book.showBookInfo();
		}
	}
}
