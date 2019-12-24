## 공간 복잡도( Space Complexity )
	알고리즘 계산 복잡도는 다음 두가지 척도로 표현될 수 있음
	- 시간 복잡도 : 얼마나 빠르게 실행되는지
	- 공간 복잡도 : 얼마나 많은 저장 공간이 필요한지
	* 대용량 시스템이 보편화되면서, 시간 복잡도가 우선.

- 고정 공간( 알고리즘과 무관한 공간 ) : 코드 저장 공간, 단순 변수 및 상수
- 가변 공간( 알고리즘 실행과 관련있는 공간 ) : 실행 중 동적으로 필요한 공간

>> S(P) = c + Sp(n)
>>> c : 고정 공간, Sp(n) : 가변 공간

* 빅 오 표기법을 생각해 볼 때, 고정 공간은 상수이므로 공간 복잡도는 가변 공간에 좌우됨

``` python
def factorial( n )
	fac = 1
	for index in range( 2, n+1 );
		fac = fac * index
	return fac
	
	>> 공간복잡도 O(1)
```


``` python
def factorial( n ) :
	if n > 1 :
		return n * factorial( n-1 )
	else :
		return 1
		
	>> 공간복잡도 O(N) 
```