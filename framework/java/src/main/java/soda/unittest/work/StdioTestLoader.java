package soda.unittest.work;

import java.io.IOException;
import java.util.Scanner;

public class StdioTestLoader implements TestLoader {

	@Override
	public String load() throws IOException {
		try (Scanner scan = new Scanner(System.in, "UTF-8")) {
            StringBuilder buf = new StringBuilder();
            while (scan.hasNextLine()) {
                buf.append(scan.nextLine());
            }   
            return buf.toString();
        }
	}

	@Override
	public void store(String message) throws IOException {
		System.out.print(message);
	}

}
