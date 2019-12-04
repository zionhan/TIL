package reference;

public class Student {
	int stId;
	String stName;
	
	Subject kor;
	Subject math;
	
	public Student( int id, String name ) {
		stId = id;
		stName = name;
		
		kor = new Subject();
		math = new Subject();
	}
	
	public void showScore() {
		System.out.println( kor.sjtScore + math.sjtScore );
	}
	
}
