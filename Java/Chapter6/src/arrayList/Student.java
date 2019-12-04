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
			System.out.println( "�л� " + studentName + "�� " + subject.getName() + "������ ������ " + subject.getScore() +"�Դϴ�." );			
		}
		System.out.println( "�л� " + studentName + "�� ������ " + total + "�Դϴ�." );		
	}
}
