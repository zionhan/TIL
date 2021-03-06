package gameEx;

public abstract class PlayerLevel {
	public abstract void run();	
	public abstract void jump();
	public abstract void turn();
	public abstract void showLevel();
	public void go( int level ) {
		run();
		for( int i=0; i<level; i++ ) {
			jump();
		}		
		turn();
	}

}
