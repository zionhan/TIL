# | 스트림

### | 입출력 스트림 구분?
 - I/O 대상 기준 : 입력 스트림, 출력 스트림
 - 자료의 종류 : 바이트 스트림, 문자 스트림
 - 스트림의 기능 : 기반 스트림, 보조 스트림
 
### | 입출력 스트림이란?
 - 네트윅에서 자료의 흐름이 물과 같다는 의미에서 유래
 - 다양한 입출력 장치에 독립적으로 일관성 있는 입출력 방식 제공
 - 입출력이 구현 되는 곳에서는 모두 I/O 스트림을 사용
 	: 키보드, 파일 디스크, 메모리 등
 	
### | 입출력 스트림과 출력 스트림
 - 입력 스트림 : 대상으로 부터 자료를 읽어 들이는 스트림( 자바 응용 프로그램 <- 입출력 자료 )
 - 출력 스트림 : 대상으로 자료를 출력하는 스트림 ( 자바 응용 프로그램 -> 입출력 자료 )
 - 스트림의 예 

 | 종류 | 예시 |
 | ---| --- |
 | 입력 스트림 | FileInputStream, FileReader, BufferedInputStream, BufferedReader 등 |
 | 출력 스트림 | FileOutputStream, FileWriter, BufferedOutputStream, BufferedWriter 등 |


### | 기반 스트림과 보조 스트림
 - 기반 스트림 : 대상에 직접 자료를 읽고 쓰는 기능의 스트림
 - 보조 스트림 : 직접 읽고 쓰는 기능은 없고 추가적인 기능을 제공해 주는 스트림
 			기반 스트림이나 또 다른 보조 스트림을 생성자의 매개변수로 포함함


### | Scanner 클래스
 - java.util 패키지에 있는 입력 클래스
 - 문자뿐 아니라 정수, 실수 등 다양한 자료형을 읽을 수 있음
 - 생성자가 다양하여 여러 소스로 부터 자료를 읽을 수 있음

| 생성자 | 설명 |
| --- | --- |
| Scanner( File source ) | 파일을 매개변수로 받아 Scanner를 생성합니다. |
| Scanner( InputStream source ) | 바이트 스트림을 매개변수로 받아 Scanner를 생성합니다. |
| Scanner( String source ) | String을 매개변수로 받아 Scanner를 생성합니다. |
 
#### | 바이트 단위 스트림
 - InputStream : 바이트 단위 입력 스트림 최상위 클래스
 - OutputStream : 바이트 단위 출력 스트림 최상위 클래스


### | 직력화( Serialization ) 
 - 인스턴스의 상태를 그대로 저장하거나 네트윅으로 전송하고 이를 다시 복원 하는 방식
 - ObjectInputStream과 ObjectOutputStream 사용
 
 
### | 데코레이터 패턴 ( Decorator Pattern ) 
 - 자바의 입출력 스트림은 데코레이터 패턴을 사용
 - 실제 입출력 기능을 가진 객체( 컴포넌트 ) 와 그 외 다양한 기능을 제공하는 데코레이터 ( 보조스트림 )을 사용하여 다양한 입출력 기능을 구현
 - 상속보다 유연한 확정성을 가짐
 - 지속적인 서비스의 증가와 제거가 용이함