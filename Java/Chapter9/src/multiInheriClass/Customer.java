package multiInheriClass;

public class Customer implements Buy, Sell {

	@Override
	public void sell() {
		System.out.println( "customer sell" );	
	}

	@Override
	public void buy() {
		System.out.println( "customer buy" );		
	}

//	@Override
//	public void order() {
//		// TODO Auto-generated method stub
//		Buy.super.order();   Buy의  order를 쓰겠다
//	}
	
	public void order() {
		System.out.println( "customer order" );
	}
	
	public void sayHello() {
		System.out.println( "customer Hello" );
	}

}
