package classpart;
// 함수 Stack 메모리 사용!!

public class FuncTest {
	public static int addNum( int num1, int num2 ) {
		int result;
		result = num1 + num2;
		return result;
	}
	
	public static void sayHello( String greeting ) {
		System.out.println( greeting );
	}
	
	public static int calcSum() {
		int sum = 0;
		int i ;
		for( i = 9; i <= 100; i++ ) {
			sum += i;
		}
		return sum;
	}
	
	
	public static void main( String[] args ) {
		int n1 = 10;
		int n2 = 20;
		System.out.println( addNum(n1, n2) );		
		sayHello( "Hello" );
		System.out.println( calcSum() );		
	}
}
