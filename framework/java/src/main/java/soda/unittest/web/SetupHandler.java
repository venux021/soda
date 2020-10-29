package soda.unittest.web;

import java.util.Map;

import com.sun.net.httpserver.HttpExchange;

public class SetupHandler extends BaseHandler {
	
	private final ClassLoaderManager mgr;
	
	public SetupHandler(ClassLoaderManager mgr) {
		this.mgr = mgr;
	}

	@Override
	protected String handleJob(HttpExchange exchange) throws Exception {
		String content = getPostBody(exchange);
		Map<String, String> params = parseQuery(content);
		String runpath = params.get("runpath");
		mgr.set(runpath);
		String message = "Add Run path " + runpath;
		System.out.println(message);
		return message;
	}

}
