package backEnd;

public class TrueFalseQuestion implements Question {

	private String question;
	private String answer;
	private int difficulty;
	private boolean isAnswered;
	private int index;
	

	public TrueFalseQuestion (String question, String answer, int difficulty) {
		this.question = question;
		this.answer = answer;
		this.difficulty = difficulty;
		this.isAnswered = false;
		this.index = 0;
	}
	
	public int getIndex() {
		return this.index;
	}
	
	public void setIndex(int index) {
		this.index = index;
	}
	
	public String getAnswer() {
		// TODO Auto-generated method stub
		return answer;
	}
	
	public int getDifficulty() {
		return difficulty;
	}


	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return "Is the following statement true or false?\n" + question;
	}
	
	@Override
	public boolean isAnswered() {
		
		return this.isAnswered;
	}
	
	public void setAnswered() {
		this.isAnswered = true;
	}



}
