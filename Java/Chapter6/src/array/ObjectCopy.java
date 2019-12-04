package array;

public class ObjectCopy {
	public static void main( String[] args ) {
		Book[] library = new Book[5];	
		Book[] copyLibrary = new Book[5];
		
		
		for( int i=0; i<library.length; i++ ) {
			library[i] = new Book( "태박산맥"+i, "한도경" );
		}
		
		System.arraycopy(library, 0, copyLibrary, 0, 5); 
		// 얕은복사 주소를 복사! 원본이 바뀌면 같이 바뀐다!
		
		
		for( Book book : copyLibrary ) {
			book.showBookInfo();
		}
		
		library[0].setTitle( "나목" );
		library[0].setAuthor( "박완서" );
		
		for( Book book : library ) {
			book.showBookInfo();
		}
		
		for( Book book : copyLibrary ) {
			book.showBookInfo();
		}
	}

}
