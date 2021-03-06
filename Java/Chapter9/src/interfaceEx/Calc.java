package interfaceEx;


public interface Calc {
	public static final double PI = 3.14;
	public static final int ERROR = -999999999;
	
	int add( int num1, int num2 );
	int substract( int num1, int num2 );
	int times( int num1, int num2 );
	int divide( int num1, int num2 );	
	
	// default 메서드
	default void description() {
		System.out.println( "정수 계산기를 구현합니다." );
		myMethod();
	}
	
	// static 메서드, 인스턴스 생성하지 않고  interface 명으로 사용 가능.
	static int total( int[] arr ) {
		int total = 0;
		for( int i : arr ) {
			total += i;
		}		
		myStaticMethod();
		return total;
	}
	
	// private method는 인터페이스 내에서만 사용 가능.
	private void myMethod() {
		System.out.println( "private method" );
	}
	
	// private static method는 static 변수에서만 사용 가능
	private static void myStaticMethod() {
		System.out.println( "private static method" );
	}
}
