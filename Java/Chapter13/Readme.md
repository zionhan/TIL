# | 오류란 무엇인가
 - 컴파일 오류 : 프로그램 코드 작성 중 발생하는 문법적 오류
 - 실행 오류 : 실행 중인 프로그램이 의도 하지 않은 동작을 하거나(bug) 프로그램이 중지 되는 오류( runtime error )
 - 자바는 예외 처리를 통하여 프로그램의 비정상 종료를 막고  log를 남길 수 있음
 
 
 ## | 오류와 예외 클래스
  - 시스템 오류( error ) : 가상 머신에서 발생, 프로그래머가 처리 할 수 없음, 동적 메모리를 다 사용한 경우, stack over flow 등
  - 예외 ( Exception )
  
 ## | try - catch 문의로 예외 처리
 ```java
 	try {
 		예외가 발생 할 수 있는 코드 부분
 	} catch( 처리할 예외 타입 e ) {
 		try 블록 안에서 예외가 발생했을 때 수행되는 부분
 	} finally {
 		예외 발생 여부와 상관없이 항상 수행 되는 부분
 		리소르를 정리하는 코드를 주로 씀
 	}
 ```
 
 
 ## | try - with - resource 문
  - 리소스를 자동으로 해제 하도록 제공해주는 구문
  - 해당 리소스가 AutoCloseable을 구현한 경우 close()를 명시적으로 호출하지 않아도 
  	try {} 블록에서 오픈된 리소스를 정상적인 경우나 예외가 발생한 경우 모두 자동으로 close()가 호출 됨
  	
  - FileInputStream의 경우 AutoCloseable을 구현 하고 있음
  
  
  
 ## | 예외 처리 미루기
 - throws 를 사용하여 예외 처리 미루기
 - try{} 블록으로 예외를 처리 하지 않고, 메서드 선언부에 throws를 추가
 - 예외가 발생한 메서드에서 예외 처리를 하지 않고 메서드를 호출한 곳에서 예외 처리를 한다는 의미
 - main() 에서 throws를 사용하면 가상머신에서 처리 됨
 
 
 ## | 사용자 정의 예외
  - JDK 에서 제공되는 예외 클래스 외에 사용자가 필요에 의해 예외 클래스를 정의하여 사용
  - 기존 JDK 클래스에서 상속받아 예외 클래스 만듬
```java
	public class IDFormatException extends Exception {
		public IDFormatException( String message ) {
			super( message );
		}
	}
```
 - throw 키워드로 예외를 발생 시킴

