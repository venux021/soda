package soda.unittest.web;

import java.io.File;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLClassLoader;
import java.util.HashMap;
import java.util.Map;

public class ClassLoaderManager {

	private Map<String, ClassLoader> loaderMap = new HashMap<>();
	
	public synchronized void set(String runpath) throws MalformedURLException {
		File file = new File(runpath);
		ClassLoader parent = ClassLoaderManager.class.getClassLoader();
    	URLClassLoader loader = new URLClassLoader(new URL[] {file.toURI().toURL()}, parent);
    	loaderMap.put(runpath, loader);
	}
	
	public synchronized ClassLoader get(String runpath) {
		return loaderMap.get(runpath);
	}
	
}
