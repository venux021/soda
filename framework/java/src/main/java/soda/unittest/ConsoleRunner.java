package soda.unittest;

import java.util.Scanner;

public class ConsoleRunner {
    
    public void run(JobTemplate<?,?> job) throws Exception {
    	String res = new JobRunner().runJob(readStdin(), job);
    	System.out.println(res);
    }
    
    private static String readStdin() throws Exception {
        try (Scanner scan = new Scanner(System.in, "UTF-8")) {
            StringBuilder buf = new StringBuilder();
            while (scan.hasNextLine()) {
                buf.append(scan.nextLine());
            }   
            return buf.toString();
        }
    }
    
}