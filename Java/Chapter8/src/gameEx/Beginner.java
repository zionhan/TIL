package gameEx;

public class Beginner extends PlayerLevel {

	@Override
	public void run() {
		System.out.println( "천천히 달립니다." );		
	}

	@Override
	public void jump() {
		System.out.println( "점프 못하지롱" );		
	}

	@Override
	public void turn() {
		System.out.println( "turn 못하지롱" );
		
	}
	@Override
	public void showLevel() {
		System.out.println( "*******초급자 레벨입니다.*******" );		
	}
}
