package hiding;

/*	정보 은닉
 *	접근 제어자(  access modifier )
 *	변수, 메서드, 생성자에 대한 접근 권한 지정
 * 	public, private, protected, 아무것도 안쓰는 경우( default )
 */


/*	this의 역할
 * 	자신의 메모리를 가르킴
 * 	생성자에서 다른 생성자를 호출 함
 * 	인스턴스 자신의 주소를 반환
 */

public class MyDate {
	private int day;
	private int month;
	private int year;
	
	public void setDay( int day ) {
		this.day = day;
	}
	
	public int getDay() {
		return day;
	}
	
	
	public int getMonth() {
		return month;
	}

	public void setMonth(int month) {
		this.month = month;
	}

	public int getYear() {
		return year;
	}

	public void setYear(int year) {
		this.year = year;
	}

	public void showDate() {
		System.out.println( year + "년" + month + "월");
	}
}
