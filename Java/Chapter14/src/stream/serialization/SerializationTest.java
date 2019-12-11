package stream.serialization;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

class Person implements Serializable {
	String name;
	transient String job;
	
	public Person( String name, String job ) {
		this.name = name;
		this.job = job;		
	}
	
	public String toString() {
		return name + ", " + job;
	}
}


public class SerializationTest {

	public static void main(String[] args) {
		Person personLee = new Person( "이순신", "엔지니어" );
		Person personKim = new Person( "김유신", "선생님" );
		
		try( FileOutputStream fos = new FileOutputStream( "serial.dat" );
				ObjectOutputStream oos = new ObjectOutputStream( fos );
				FileInputStream fis = new FileInputStream( "serial.dat" );
				ObjectInputStream ois = new ObjectInputStream( fis ) ) {
			
			oos.writeObject( personLee );
			oos.writeObject( personKim );
			
			Person p1 = (Person) ois.readObject();
			Person p2 = (Person) ois.readObject();
			
			System.out.println( p1 );
			System.out.println( p2 );
			
		} catch( IOException | ClassNotFoundException e ) {
			System.out.println( e );
		}
	}

}
