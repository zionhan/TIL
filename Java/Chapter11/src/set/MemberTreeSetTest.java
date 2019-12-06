package set;

public class MemberTreeSetTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		MemberTreeSet manager = new MemberTreeSet();
		
		Member memberLee = new Member( 100, "Lee" );
		Member memberKim = new Member( 200, "Kim" );
		Member memberPark = new Member( 300, "Park" );
		Member memberPark2 = new Member( 300, "Park2" );
		
		manager.addMember(memberLee);
		manager.addMember(memberPark);
		manager.addMember(memberKim);
		manager.addMember(memberPark2);
		manager.showAllMember();
		System.out.println("-------------------");
		manager.removeMember(100);
		manager.showAllMember();

	}
}
