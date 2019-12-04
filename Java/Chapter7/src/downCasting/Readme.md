## 하위 클래스로 형 변환, 다운 캐스팅
묵시적으로 상위 클래스 형변환된 인스턴스가 원래 자료형( 하위클래스 ) 으로 변환되어야 할 때 다운캐스팅이라고 함
하위 클래스로의 형 변환은 명시적으로 되어야 함
Customer vc = new VipCustoer();					// 묵시적
VipCustomer vCustomer = ( VipCustomer) vc;		// 명시적