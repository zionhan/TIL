package polymorphism;

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
}

class Tiger extends Animal{
	public void move() {
		System.out.println( "ȣ���̰� �� �߷� �ݴϴ�." );
	}
}

class Eagle extends Animal{
	public void move() {
		System.out.println( "�������� �ϴ��� ���ư��ϴ�." );
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
		
	}
	
	public void moveAnimal( Animal animal ) {
		animal.move();
	}
}
