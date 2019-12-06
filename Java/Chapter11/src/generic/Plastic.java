package generic;

public class Plastic extends Material {
	
	public String toString() {
		return "재료는 Plastic 입니다.";
	}
	
	@Override
	public void doPrinting() {
		// TODO Auto-generated method stub
		System.out.println( "Plastic으로 프린트 합니다." );
	}
	
	
}
