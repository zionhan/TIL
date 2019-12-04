package arrayList;

import java.util.ArrayList;

public class Student {
	private static int number = 100;
	int studentId;
	String studentName;
	ArrayList<Subject> subjectList;
	
	public Student( String studentName ) {
		number ++;
		studentId = number;
		this.studentName = studentName;	
		subjectList = new ArrayList<Subject>();
	}
	
	public void addSubject( String name, int score ) {
		Subject subject = new Subject( name, score );
		subjectList.add( subject );		
	}
	
	public void showStudentInfo() {
		int total = 0;		
		for( Subject subject : subjectList ) {
			total += subject.getScore();
			System.out.println( "학생 " + studentName + "의 " + subject.getName() + "과목의 성적은 " + subject.getScore() +"입니다." );			
		}
		System.out.println( "학생 " + studentName + "의 총점은 " + total + "입니다." );		
	}
}
