package generic;

public class Powder extends Material {
	public String toString() {
		return "재료는 Powder 입니다.";
	}
	
	@Override
	public void doPrinting() {
		// TODO Auto-generated method stub
		System.out.println( "Powder로 프린트 합니다." );
		
	}
}
