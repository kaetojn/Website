package backEnd;

import java.io.File;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathFactory;

import org.w3c.dom.Document;

public class QuestionCreatorFactory {

	public QuestionCreator getInstance() {
		
		QuestionCreator qc = null;
		try {
			
			
			// Open up the XML database
			File input = new File("src" + File.separator + "recources" + File.separator + "questions.xml");
			// Parse it, and store it as a document
			DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
			factory.setValidating(true);
			DocumentBuilder builder = factory.newDocumentBuilder();
			Document doc = builder.parse(input);
			// Set up document for reading with XPath
			XPathFactory xpathfactory = XPathFactory.newInstance();
			XPath xpath = xpathfactory.newXPath();
			// Creates a new question creator
			qc = new QuestionCreator(doc, xpath);
			
			
			//Generate questions to text
			
			
		}
		catch (Exception e) {
			e.printStackTrace();
		}
		
		return qc;
	}
}
