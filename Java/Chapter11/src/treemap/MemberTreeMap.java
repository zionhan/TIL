package treemap;

import java.util.TreeMap;
import java.util.Iterator;

public class MemberTreeMap {
	private TreeMap<Integer, Member> TreeMap;
	
	public MemberTreeMap() {
		TreeMap = new TreeMap<Integer, Member>();		
	}
	
	public void addMember( Member member ) {
		TreeMap.put( member.getMemberId(), member );		
	}
	
	public boolean removeMember( int memberId ) {
		if( TreeMap.containsKey( memberId ) ) {
			TreeMap.remove(memberId);
			return true;
		}
		System.out.println( "회원 번호가 없습니다." );
		return false;
	}
	
	public void showAllMember() {
		Iterator<Integer> ir = TreeMap.keySet().iterator();
		while( ir.hasNext() ) {
			int key = ir.next();
			Member member = TreeMap.get(key);
			System.out.println( member );
		}
		System.out.println();
		
	}
}
