package set;

import java.util.HashSet;
import java.util.Iterator;
import java.util.TreeSet;

public class MemberTreeSet {
	private TreeSet<Member> hashSet;
	
	public MemberTreeSet () {
		hashSet = new TreeSet<Member> ( new Member() );
	}
	
	public void addMember( Member member ) {
		hashSet.add( member );
	}
	
	public boolean removeMember( int memberId ) {
		Iterator< Member > ir = hashSet.iterator();
		while( ir.hasNext() ) {
			Member member = ir.next();
			if( member.getMemberId() == memberId ) {
				hashSet.remove( member );
				return true;
			}				
		}		
		System.out.println( memberId + "번호가 존재하지 않습니다." );
		return false;
	}
	
	public void showAllMember() {
		for( Member member : hashSet ) {
			System.out.println( member );
		}
	}
}
