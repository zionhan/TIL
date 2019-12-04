package staticEx;
/*	프로그램 변수의 유형
 * 	변수 유형			선언위치		사용범위			메모리	생성과 소멸
 * 	지역변수(로컬변수)	함수 내부에 선언	함수 내부에서만 사용	스택		함수가 호출될때 생성, 끝나면 소멸		
 * 	맴버변수(인스턴스변수)	클래스 멤버 변수	클래스 내부에서 사용	힙		인스턴스 생성시 생성, 가비지 컬렉터가 수거시 소멸
 * 	static(클래스변수)	static 예약어	클래스 내부에서 사용	데이터영역	프로그램이 시작 생성, 종료 소멸
 */	

public class Student {
	public static int serialNum = 1000;
	private int studentId;
	public String studentName;
	public String address;
	
	public Student() {}
	
	public Student( String name ) {
		studentName = name;
		serialNum ++;
		studentId = serialNum;
	}
	 
	public Student( int id, String name ) {
		studentId = id;
		studentName = name;
		address = "주소 없음";
		serialNum ++;
	}
	
	public void showStudentInfo() {
		System.out.println( studentName + "," + address );
	} 
	
	public String getStudentName( ) {
		return studentName;
	}
}
