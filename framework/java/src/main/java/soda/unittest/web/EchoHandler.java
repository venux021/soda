package soda.unittest.web;

import com.sun.net.httpserver.HttpExchange;

public class EchoHandler extends BaseHandler {

	@Override
	protected String handleJob(HttpExchange exchange) throws Exception {
		return exchange.getRequestURI().getQuery();
	}

}
