package thread;

//class MyThread extends Thread {
//	public void run() {
//		int i;
//		for( i=0; i<=200; i++ ) {
//			System.out.print( i + "\t" );
//		}		
//		try {
//			sleep(1000);
//		} catch (InterruptedException e) {
//			// TODO Auto-generated catch block
//			e.printStackTrace();
//		}
//	}
//}

class MyThread implements Runnable {
	public void run() {
		int i;
		for( i=0; i<=200; i++ ) {
			System.out.print( i + "\t" );
		}		
		try {
			Thread.sleep( 100 );
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}

public class ThreadTest {

	public static void main(String[] args) {
		System.out.println( "start" );
//		MyThread th1 = new MyThread();
//		MyThread th2 = new MyThread();	

		
//		MyThread runner1 = new MyThread();
		Thread th1 = new Thread( new MyThread() );
		
//		MyThread runner2 = new MyThread();
		Thread th2 = new Thread( new MyThread() );
		
		th1.start();
		th2.start();
		
		Thread t = Thread.currentThread();
		System.out.println( t );
		
		System.out.println( "end" );		

	}

}
