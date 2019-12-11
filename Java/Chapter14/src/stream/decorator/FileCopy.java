package stream.decorator;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;

public class FileCopy {

	public static void main(String[] args) throws IOException {
		
		long milliseconds = 0;
		
		try( FileInputStream fis = new FileInputStream( "a.zip" );
				FileOutputStream fos = new FileOutputStream( "copy.zip" ) ) {
			milliseconds = System.currentTimeMillis();
			int i;
			
			while( ( i = fis.read() ) != -1 ) {
				fos.write( i );
			}
			
			milliseconds = System.currentTimeMillis() - milliseconds;
		} catch( IOException e ) {
			System.out.println( e );
		}
		
		System.out.println( "시간 : " + milliseconds );
		
		Socket socket = new Socket();
		
		BufferedReader isr = new BufferedReader( new InputStreamReader( socket.getInputStream() ) );
		isr.readLine();
		
		System.out.println( "시간 : " + milliseconds );

	}

}
