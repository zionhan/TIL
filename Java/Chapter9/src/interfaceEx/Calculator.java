package interfaceEx;

public abstract class Calculator implements Calc {

	@Override
	public int add(int num1, int num2) {
		
		return num1 + num2 ;
	}

	@Override
	public int substract(int num1, int num2) {
		// TODO Auto-generated method stub
		return num1 - num2 ;
	}
	
//	public void description() {
//		System.out.println( "재정의 한 description" );
//	}

}
