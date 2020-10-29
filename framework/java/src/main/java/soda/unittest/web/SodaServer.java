package soda.unittest.web;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpServer;

public class SodaServer {

	private String bindAddress;
	
	private int port;
	
	private HttpServer server;
	
	private ExecutorService executor;
	
	private int concurrency = 20;
	
	private ClassLoaderManager classLoaderMgr = new ClassLoaderManager();
	
	public static void main(String[] args) throws Exception {
		int port = 9201;
		if (args.length > 0) {
			port = Integer.parseInt(args[0]);
		}
		SodaServer ss = new SodaServer("localhost", port);
		ss.start();
		System.out.println("server start");
	}
	
	public SodaServer(String bindAddress, int port) throws IOException {
		this.bindAddress = bindAddress;
		this.port = port;
		server = HttpServer.create(new InetSocketAddress(this.bindAddress, this.port), 0);
        executor = Executors.newFixedThreadPool(concurrency);
        server.setExecutor(executor);
        initialize();
	}
	
	private class StopHandler extends BaseHandler {
		@Override
		public String handleJob(HttpExchange exchange) throws Exception {
			stop();
			return "Stop signal sent";
		}
	}
	
	private void initialize() {
		// GET
		server.createContext("/soda/java/echo", new EchoHandler());
		
		// GET
		server.createContext("/stop", new StopHandler());
		
		// POST, application/json
		server.createContext("/soda/java/job", new JobHandler(classLoaderMgr, 5000));
		
		// POST, application/x-www-form-urlencoded
		server.createContext("/soda/java/setup", new SetupHandler(classLoaderMgr));
	}
	
	public void start() {
		server.start();
	}
	
	public void stop() {
		new Thread(() -> {
        	server.stop(1);
        	executor.shutdown();
        	try {
        		executor.awaitTermination(1, TimeUnit.SECONDS);
        		System.out.println("server stop");
        	} catch (Exception ex) {
        		ex.printStackTrace();
        	}
        }).start();
	}
	
}
