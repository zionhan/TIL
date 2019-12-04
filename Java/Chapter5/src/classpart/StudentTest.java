package classpart;

public class StudentTest {
	public static void main( String[] args ) {
		Student lee = new Student();
		// 인스턴스 생성시 맴버변수들은 Heap 메모리 영역에 할당 ( 동적 메모리 )
		// Garbage Collector( Thread ) 
		
		lee.studentName = "한도경";
		lee.address = "서울";
		lee.showStudentInfo();
		
		Student kim = new Student();
		kim.studentName = "김도경";
		kim.address = "경주";
		
		System.out.println( lee );	// JVM 이 할당한 가상 hash 값
		System.out.println( kim );
		
	}
}