package staticEx;

/*	singleton Patter : 단 하나만 존재하는 인스턴스
 * 	생성자는 private 으로
 * 	static으로 유일한 객체 생성
 * 	외부에서 유일한 객체를 참조할 수 있는 public static get() 매서드 구현
 */

public class Company {
	
	private static Company instance = new Company();
	
	private Company() {}
	
	public static Company getInstance() {
		if( instance == null ) {
			instance = new Company();
		}
		return instance;
	}
	


}
