package soda.unittest.web;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Map;
import java.util.stream.Collectors;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;

public abstract class BaseHandler implements HttpHandler {
	
	@Override
	public void handle(HttpExchange exchange) throws IOException {
		try {
			String result = handleJob(exchange);
			sendMessage(exchange, 200, result);
		} catch (Exception ex) {
			ex.printStackTrace();
			String error = ex.getMessage();
			sendMessage(exchange, 500, error);
		}
	}
	
	protected abstract String handleJob(HttpExchange exchange) throws Exception;
	
	protected void sendMessage(HttpExchange exch, int code, String message) {
		try {
			byte[] data = message.getBytes("UTF-8");
			exch.sendResponseHeaders(code, data.length);
			exch.getResponseBody().write(data);
			exch.getResponseBody().close();
		} catch (IOException ex) {
			ex.printStackTrace();
		}
    }
	
	protected Map<String, String> parseQuery(HttpExchange exch) {
    	String query = exch.getRequestURI().getQuery();
    	return parseQuery(query);
    }
    
	protected Map<String, String> parseQuery(String query) {
    	return Arrays.stream(query.split("[&]"))
        		.map(s -> s.split("="))
        		.filter(ss -> ss.length == 2)
        		.collect(Collectors.toMap(ss -> ss[0], ss->ss[1]));
    }
	
	protected String getPostBody(HttpExchange exch) throws IOException {
    	BufferedReader reader = new BufferedReader(new InputStreamReader(exch.getRequestBody(), "UTF-8"));
    	StringBuilder buf = new StringBuilder();
    	String line = null;
    	while ((line = reader.readLine()) != null) {
    		buf.append(line);
    	}
    	reader.close();
    	return buf.toString();
    }
	
}

