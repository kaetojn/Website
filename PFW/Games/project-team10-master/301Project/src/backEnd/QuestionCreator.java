package backEnd;

import java.util.List;
import java.util.Random;

import javax.xml.xpath.*;

import org.w3c.dom.*;

import backEnd.Question.type;

public class QuestionCreator implements QuestionFactory {
	
	Document doc;
	XPath xpath;
	
	
	public QuestionCreator(Document doc, XPath xpath) {
		this.doc = doc;
		this.xpath = xpath;
	}
	
	public Question getQuestionByExpr(String strexpr) {
		
		Question q = null;
		try {
			// Get the list of nodes satisfying expr
//			String strepr = "//question";
			XPathExpression expr = xpath.compile(strexpr);
			NodeList nl = (NodeList) expr.evaluate(this.doc, XPathConstants.NODESET);
			Random r = new Random();
			int index = r.nextInt(nl.getLength());
			
			
			// pull a random question out
			Element e = (Element) nl.item(index);
			// Get all the children elements
			NodeList childs = e.getChildNodes();
			
			// Even indexes are the element names, odd indices are the text of the previous element
			// So based on current xml, childs[1] gets the question, and childs[3] gets the answer
			
			// TODO: get hints as well
			String question = childs.item(1).getTextContent().replace("\\n", "\n").replace("\\t", "\t");
			
			String answer = childs.item(3).getTextContent().replace("\\n", "\n").replace("\\t", "\t");
			int difficulty = Integer.parseInt(e.getAttributes().getNamedItem("difficulty").getNodeValue());
			
			
			// TODO: find reason to have different question implementations, as currently no reason
			if (e.getParentNode().getNodeName() == "true-false-questions") {
				q = new TrueFalseQuestion(question, answer, difficulty);
			}
			
			else if (e.getParentNode().getNodeName() == "return-value-questions") {
				q = new ReturnValueQuestion(question, answer, difficulty);
			}
			
		} catch (XPathExpressionException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return q;
		
	}

	public Question getRandomQuestion() {
		
		return getQuestionByExpr("//question");
	}
	
	
	public Question getRandomQuestionByDiff(int difficulty) {
		
		return getQuestionByExpr("//question[@difficulty=" + difficulty + "]");
	}
	
	// Gets a random question that has type t
	public Question getRandomQuestionByType(type t) {
		
		return getQuestionByExpr("//question[types/" + t.toString() + "]");
	}

	// Gets a random question that has ALL types in lt
	public Question getRandomQuestionByTypes(List<type> lt) {
		// TODO Auto-generated method stub
		String format_types = "[";
		for (type t : lt) {
			format_types = format_types.concat("types/" + t.toString() + " and ");
		}
		// removes last &
		
		format_types = format_types.substring(0, format_types.lastIndexOf("and") - 1);
		format_types = format_types.concat("]");
		System.out.println(format_types);
		return getQuestionByExpr("//question" + format_types);
		
	}

}
