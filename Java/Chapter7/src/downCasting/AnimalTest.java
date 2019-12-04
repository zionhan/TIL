package downCasting;

import java.util.ArrayList;

class Animal{
	public void move() {
		System.out.println( "������ �����Դϴ�." );
	}
}

class Human extends Animal{
	public void move() {
		System.out.println( "����� �ι߷� �Ƚ��ϴ�." );
	}
	public void readBook() {
		System.out.println( "����� å�� �н��ϴ�." );
	}
}

class Tiger extends Animal{
	public void move() {
		System.out.println( "ȣ���̰� �� �߷� �ݴϴ�." );
	}
	
	public void hunting() {
		System.out.println( "ȣ���̰� ����� �մϴ�." );
	}
}

class Eagle extends Animal{
	public void move() {
		System.out.println( "�������� �ϴ��� ���ư��ϴ�." );
	}
	
	public void flying() {
		System.out.println( "�������� ������ �� ��� ���ư��ϴ�." );
	}
}



public class AnimalTest {
	public static void main( String[] args ) {
		Animal human = new Human();
		Animal tiger = new Tiger();
		Animal eagle = new Eagle();		
		
		human.move();
		tiger.move();
		eagle.move();
		
		Human h = (Human) human;
		h.readBook();
		
//		Eagle e = (Eagle) human;
		if( human instanceof Eagle ) {	// �ٿ� ĳ���ý� ������ ����. ���������� ����ȯ.
			Eagle e = (Eagle) human;
			
		}
		
		AnimalTest test = new AnimalTest();
		test.moveAnimal(human);
		test.moveAnimal(tiger);
		test.moveAnimal(eagle);
		
		ArrayList<Animal> animalList = new ArrayList<Animal> ();
		animalList.add( human );
		animalList.add( tiger );
		animalList.add( eagle );
		
		for( Animal animal : animalList ) {
			animal.move();
		}
		
		test.testDownCasting( animalList );
		
	}
	
	public void testDownCasting( ArrayList<Animal> list ) {
		for ( int i=0; i<list.size(); i++ ) {
			Animal animal = list.get(i);
			
			if( animal instanceof Human ) {
				Human human = (Human) animal;
				human.readBook();
			} else if ( animal instanceof Tiger ) {
				Tiger tiger = (Tiger) animal;
				tiger.hunting();
			} else if ( animal instanceof Eagle ) {
				Eagle eagle = (Eagle) animal;
				eagle.flying();
			} else {
				System.out.println( "Error" );
			}			
		}
	}
	
	
	public void moveAnimal( Animal animal ) {
		animal.move();
	}
}
