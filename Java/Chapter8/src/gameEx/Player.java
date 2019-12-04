package gameEx;

public class Player {
	
	private PlayerLevel level;
	
	public Player() {
		level = new Beginner();
		level.showLevel();
	}
	
	public PlayerLevel getLevel() {
		return level;
	}
	
	public void upgradeLevel( PlayerLevel level ) {
		this.level = level;
		level.showLevel();
	}
	
	public void play( int count ) {
		level.go( count );
	}
}
