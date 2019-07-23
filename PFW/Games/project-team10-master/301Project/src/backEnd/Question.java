package backEnd;

public interface Question {
	
	public enum type {VAR, ARITHMETIC, LIST, FOR, WHILE, CALL}	
	
	public boolean isAnswered();
	
	public String getAnswer();
	
	public void setAnswered();
	
	public int getIndex();
	public void setIndex(int index);
	
	public int getDifficulty();
	
	@Override
	public abstract String toString();

}
