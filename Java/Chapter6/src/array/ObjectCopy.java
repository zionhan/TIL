package array;

public class ObjectCopy {
	public static void main( String[] args ) {
		Book[] library = new Book[5];	
		Book[] copyLibrary = new Book[5];
		
		
		for( int i=0; i<library.length; i++ ) {
			library[i] = new Book( "�¹ڻ��"+i, "�ѵ���" );
		}
		
		System.arraycopy(library, 0, copyLibrary, 0, 5); 
		// �������� �ּҸ� ����! ������ �ٲ�� ���� �ٲ��!
		
		
		for( Book book : copyLibrary ) {
			book.showBookInfo();
		}
		
		library[0].setTitle( "����" );
		library[0].setAuthor( "�ڿϼ�" );
		
		for( Book book : library ) {
			book.showBookInfo();
		}
		
		for( Book book : copyLibrary ) {
			book.showBookInfo();
		}
	}

}
