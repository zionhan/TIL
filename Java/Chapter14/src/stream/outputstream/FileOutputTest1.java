package stream.outputstream;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class FileOutputTest1 {

	public static void main(String[] args) {
		byte[] bs = new byte[26];
		byte data = 65;
		for( int i=0; i<bs.length; i++ ) {
			bs[i] = data;
			data++;
		}
		
		try( FileOutputStream fos = new FileOutputStream( "input.txt", true );
			 FileInputStream fis = new FileInputStream( "input.txt" ) ) {
			fos.write( bs );
			int ch;
			
			while( (ch = fis.read( bs ) ) != -1 ) {
//				System.out.print( (char) ch );
				for( byte b : bs ) {
					System.out.print( (char) b );
				}
				System.out.println();
			}			
			
		} catch( IOException e ) {
			System.out.println( e );
		}

	}

}
