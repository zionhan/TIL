package array;

public class ObjectDeepCopy {
	public static void main( String[] args ) {
		Book[] library = new Book[5];	
		Book[] copyLibrary = new Book[5];
		
		
		for( int i=0; i<library.length; i++ ) {
			library[i] = new Book( "�¹ڻ��"+i, "�ѵ���" );
			copyLibrary[i] = new Book( library[i].getTitle(), library[i].getAuthor() );
			// ���� ����. �ּ� ���簡 �ƴ϶� ���ο� �ν��Ϳ� ���� �Է�
		}

		library[0].setTitle( "����" );
		library[0].setAuthor( "�ڿϼ�" );
		
		// ���� for������
		for( Book book : library ) {
			book.showBookInfo();
		}
		
		for( Book book : copyLibrary ) {
			book.showBookInfo();
		}
	}
}
