package polymorphism;

import java.util.ArrayList;

class Animal{
	public void move() {
		System.out.println( "동물이 움직입니다." );
	}
}

class Human extends Animal{
	public void move() {
		System.out.println( "사람이 두발로 걷습니다." );
	}
}

class Tiger extends Animal{
	public void move() {
		System.out.println( "호랑이가 네 발로 뜁니다." );
	}
}

class Eagle extends Animal{
	public void move() {
		System.out.println( "독수리가 하늘을 날아갑니다." );
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
