package innerclass;

class OutClass {
	private int num = 10;
	private static int sNum = 20;
	private InClass inClass;
	
	public OutClass() {
		inClass = new InClass();
	}
	
	
	class InClass {
		int iNum = 100;
//		static in sInNum = 200;
		
		void inTest() {
			System.out.println( num );
			System.out.println( sNum );
		}
	}	
	public void usingInner() {
		inClass.inTest();
	}
	
	static class InStaticClass {
		int inNum = 100;
		static int sInNum = 200;
		
		void inTest() {
			System.out.println( inNum );
			System.out.println( sInNum );
//			System.out.println( num ); 		static inner Class 이기 때문에 static 변수만 사용 가능.
			System.out.println( sNum );
		}
		
		static void sInTest() {
//			System.out.println( inNum );
			System.out.println( sInNum ); 
			System.out.println( sNum );
		}
	}
	
}


public class innerTest {
	public static void main(String[] args ) {
		OutClass outClass = new OutClass();
		outClass.usingInner();
		
		OutClass.InClass myInClass = outClass.new InClass();	// 잘 사용하지 않는 문법	
		myInClass.inTest();
		
		OutClass.InStaticClass sInClass = new OutClass.InStaticClass();
		OutClass.InStaticClass.sInTest();
		sInClass.inTest();
	}

}
