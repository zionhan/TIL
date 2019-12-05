# | Object 클래스
### 모든 클래스의 최상위 클래스
### java.lang.Object 클래스

- 모든 클래스는 Object 클래스에서 상속 받음
- 모든 클래스는 Object 클래스의 메서드를 사용할 수 있음
- 모든 클래스는 Object 클래스의 일부 메서드를 재정의 하여 사용할 수 있음


## toString() 메서드 : 객체의 출력 방식을 재정의 할 수 있다.
## equals() 메서드 : 두 객체의 동일함을 논리적으로 재정의 할 수 있음
	물리적 동일 : 같은 주소를 가지는 객체
	논리적 동일 : 같은 학번의 학생, 같은 주문 번호의 주문
	
## hashCode() 메서드 : 인스턴스가 저장된 가상머신의 주소를 10진수로 변환
	두개의 서로 다른 메모리에 위치한 인스턴스가 동일하다는 것은?
		논리적으로 동일 : eqauls()의 반환값이  true
		동일한 hashCode 값을 가짐 : hashCode()의 반환 값이 동일\
		
## clone() 메서드 : 
	### 객체의 복사본을 만듦
	### 기본 틀( prototype )으로 부터 같은 속성 값을 가진 객체의 복사본을 생성할 수 있음
	### 객체지향 프로그래밍의 정보은닉에 위배되는 가능성이 있으므로 복제할 객체는 Cloneable 인터페이스를 명시해야 함. implements Cloneable
	
	
## finalize() 메서드 : 직접 부르는 메서드가 아니다
	객체가 heap 메모리에서 해제 될 때 Garbage Collector에서 실행된다.

	
	
	
# | String 클래스
## String 클래스 선언하기
	String str1 = new String( "abc" );	// 인스턴스로 생성됨
	String str2 = "abc" ;					// 상수풀에 있는 문자열을 가리킴
## String은 immutable
	한번 선언되거나 생성된 문자열을 변경할 수 없음.( 맴버변수가 final로 선언돼있음 )
	String 클래스의 concat() 메서드 혹은 "+"를 이용하여 String을 연결하는 경우 문자열은 새로 생성 됨
	
# | String Buffer, Builder 클래스
	가변적인 char[] 배열을 멤버변수로 가지고 있는 클래스
	문자열을 변경하거나 연결하는 경우 사용하며 편리한 클래스
	
	StringBuffer는 멀티 쓰레드프로그래밍에서 동기화( Synchronization )이 보장됨
	단일 쓰레드 프로그래밍에서는 StringBuilder를 사용하는 것이 더 좋음
	
	toString() 메서드로  String 반환
	

# | Wrapper 클래스 : 기본 자료형에 대한 클래스