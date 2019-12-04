package staticEx;

public class CardCompany {
	
	private CardCompany() {};
	
	private static CardCompany instance = new CardCompany();	
	
	public static CardCompany getInstance() {
		return instance;
	}
	
	public Card createCard() {
		return new Card();
	}
	
}
