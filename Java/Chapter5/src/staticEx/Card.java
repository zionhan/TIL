package staticEx;

public class Card {
	private static int standard = 1000;
	private int number;
	public Card() {
		number = standard++;
	}
	
	
	public int getCardNumber() {
		return number;
	}
	
	
}
