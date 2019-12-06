package treemap;

public class MemberTreeMapTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		MemberTreeMap manager = new MemberTreeMap();
		
		Member memberLee = new Member( 100, "Lee" );
		Member memberPark = new Member( 400, "Park2" );
		Member memberKim = new Member( 200, "Kim" );
		Member memberPark2 = new Member( 300, "Park1" );
				
		manager.addMember(memberKim);
		manager.addMember(memberLee);
		manager.addMember(memberPark2);	
		manager.addMember(memberPark);		
		
		manager.showAllMember();
		
		manager.removeMember( 200 );
		manager.showAllMember();
	}
}
