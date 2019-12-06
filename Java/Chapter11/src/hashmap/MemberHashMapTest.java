package hashmap;

public class MemberHashMapTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		MemberHashMap manager = new MemberHashMap();
		
		Member memberLee = new Member( 100, "Lee" );
		Member memberKim = new Member( 200, "Kim" );
		Member memberPark2 = new Member( 300, "Park1" );
		Member memberPark = new Member( 300, "Park2" );		
		
		
		manager.addMember(memberLee);
		manager.addMember(memberPark2);	
		manager.addMember(memberPark);
		manager.addMember(memberKim);
		
		
		manager.showAllMember();
		
		manager.removeMember( 200 );
		manager.showAllMember();
	}
}
