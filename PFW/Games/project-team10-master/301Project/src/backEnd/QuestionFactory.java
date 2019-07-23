package backEnd;

import java.util.List;

import backEnd.Question.type;

public interface QuestionFactory {

	public Question getQuestionByExpr(String strexpr);
	
	public Question getRandomQuestion();
	
	public Question getRandomQuestionByDiff(int difficulty);
	
	public Question getRandomQuestionByType(type t);
	
	public Question getRandomQuestionByTypes(List<type> lt);
}
