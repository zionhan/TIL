# | Thread

### Thread란?
#### Process
	실해중인 프로그램
	OS로부터 메모리를 할당 받음
#### Thread<br>
	실제 프로그램이 수행되는 작업의 최소 단위
	하나의 프로세스는 하나 이상의 Thread를 가지게 됨
	
### Thread 구현하기
 - extend Thread
 - implements Runnable
 
### Multi-Thread 프로그래밍
 - 동시에 여러 개의 Thread가 수행되는 프로그래밍
 - Thread는 각각의 작업공간( context )를 가짐
 - 공유 자원이 있는 경우 race condition이 발생
 - critical section에 대한 동기화( synchronization )의 구현이 필요
 - Thread가 CPU에 의해 메모리 할당 받기 위해선 Runnable 상태어야 한다.
 - sleep(), wait(), join() 에 의해 Not Runnalbe 상태
 - 시간이 지나거나, notify(), other thread exits Runnable 상태
 - Thread 우선순위 : setPriority