package hw;

import java.util.ArrayList;

public class Student {
	String stName;
	ArrayList<Book> bookList;
	
	public Student( String stName ) {
		this.stName = stName;
		bookList = new ArrayList<Book>();
	}
	
	public void addBook( String bookName ) {
		Book book = new Book( bookName );
		bookList.add( book );
	}
	
	public void viewInfo() {
		String book = "";
		for( Book s : bookList ) {
			book += s.getName() + " ";
		}
		System.out.println( stName + " 학생이 읽은 책은 : " + book + " 입니다." );		
	}
}
