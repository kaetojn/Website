import java.awt.Color;
import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Timer;
import java.util.TimerTask;

import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.JTextArea;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathFactory;

import org.w3c.dom.Document;

import userInterface.*;
import backEnd.*;
import backEnd.Question.type;

public class Level {
	
	//private TimerTask spawnQuestion;
	private QuestionFactory qc;
	private JTextArea QuestionPage;
	private inputMatcher matcher;
	private GameArea garea;
	private long length;
	private int numQuestions;
	private Lesson lesson;
	private List<type> qtypes;
	
	private Player player;
	
	private ImageIcon icon;
	private PlayerHealth health;


	public Level(JTextArea Question, inputMatcher matcher, GameArea gamearea, QuestionFactory qc, Lesson lesson, List<type> qtypes, PlayerHealth health) {

		
		this.garea = gamearea;
		this.QuestionPage = Question;
		this.matcher = matcher;
		//timer = new Timer();
		this.qc = qc;
		this.lesson = lesson;
		
		this.length = 60000; // 60 secs in millisec
		this.numQuestions = 0;
		this.qtypes = qtypes;
		// TODO: change this to parameter to allow variable level duration
		
		this.health = health;

	}
	
	// return the system time in millis each question will be spawned at -  should 
	// be able to use this to spawn enemies at  same time?
	
	public List<Long> startLevel() {
		
		long start_time = System.currentTimeMillis();
		
		Timer t = new Timer();
		
		long previous = 0;
		
		List<Long> sl = new ArrayList<>();
		
		System.out.println("1");
		garea.setLesson(lesson);
		System.out.println("2");
		
		while (garea.isLessonActive()) { //loop until player starts
			garea.repaint();
		}

		/*	try {
				Thread.sleep(10000);                 //10000 milliseconds is ten seconds.
			} catch(InterruptedException ex) {
			    Thread.currentThread().interrupt();
			}
			*/
			//garea.toggleLesson();
		//}
		//else {
		
			
		//}
		
		spawnQuestionByTypes();
		while (previous <= this.length) {
			
			TimerTask spawner = new TimerTask() {
				@Override
				public void run() {
					spawnQuestionByTypes();	
				}
			};
			
			
			long delay = new Random().nextInt(4000) + 11000; // random int between 0 and 4000 (0 and 4 seconds)
			// add 11000 to this so qs are spawned randomly every 11 to 15 secs
			// TODO: Find apropriate delay, maybe based on level/dificulty
			long curDelay = delay + previous;
			t.schedule(spawner, curDelay);
			sl.add(curDelay + start_time);
			previous = curDelay;
			this.numQuestions ++;
			
		}
		
		Timer timer = new Timer();
		
		
		timer.schedule(new TimerTask() {
			public void run() {
				ArrayList<Enemy> enemies = garea.getEnemies();
				for (Enemy enemy : enemies) {
					enemy.moveDown(1);
				}
				health.updateHealth(enemies);
				garea.repaint();
			}
		}, 0, 1*250); //0 is the delay before the timerTask starts running, 1*250 is how often it goes off (meaning it goes off every quarter second)
		
		return sl;
	}
	
	
	
	
	//Create new Question return that question. -> input matcher should change its name, it stores all questions
	//but also sets them up
	//public void Question1() {
	//	timer.schedule (spawnQuestion, 0l, 1000*10);
		
	
	//}
	//Add code for other difficulties or add a random function
	
	
	public int getNumQuestions() {
		return numQuestions;
	}
	
	public void spawnQuestionByTypes() {
		
		
		System.out.println("x");
		Question q = qc.getRandomQuestionByTypes(this.qtypes);
		System.out.println(q);
		
		//add to the matcher
		this.matcher.addToCurrentQuestions(q);
		this.matcher.incrementNumIndex();
		
		//set  the index of that question reletive to the list
		q.setIndex(this.matcher.getNumIndex());
		
		//add to the question window.
		this.QuestionPage.append("\n" + this.matcher.getNumIndex() + ": "+ q.toString() + "\n");
		System.out.println("the answer is " + q.getAnswer() + "\nlen is " + q.getAnswer().length());
		
		//Can also use Default Caret Bottom.
		QuestionPage.setCaretPosition(QuestionPage.getDocument().getLength());
		
		//Spawn monsters (amount based on difficulty)
		spawnEnemies(q.getDifficulty());
		spawnPlayer();
		if(garea.players.size() > 1){
			garea.removePlayer(0);
		}
	}

	//spawn random questions of a specific difficulty and spawns the appropriate number
	//of enemies
	public void spawnQuestion(int diff) {
		
			// Compiles XPath expression that gets questions of a certain difficulty
			
			// Uses the Question creator, and passes it the expr, in order to get a random question satisfying the expression
			Question q = qc.getRandomQuestionByDiff(diff);
		
			
			//add to the matcher
			this.matcher.addToCurrentQuestions(q);
			
			this.matcher.incrementNumIndex();
			
			//set  the index of that question reletive to the list
			q.setIndex(this.matcher.getNumIndex());
			
			//add to the question window.
			this.QuestionPage.append("\n" + this.matcher.getNumIndex() + ": "+  q.toString() + "\n");
			
			//Can also use Default Caret Bottom.
			QuestionPage.setCaretPosition(QuestionPage.getDocument().getLength());
			
			
			//Spawn monsters (amount based on difficulty)
			spawnEnemies(q.getDifficulty());
			
	}
	
	//spawn random questions  and the appropriate amount of enemies
	public void spawnQuestion() {

		// Compiles XPath expression that gets questions of a certain difficulty
		
		// Uses the Question creator, and passes it the expr, in order to get a random question satisfying the expression
		Question q = qc.getRandomQuestion();
		
		//add to the matcher
		this.matcher.addToCurrentQuestions(q);
		this.matcher.incrementNumIndex();
		
		//set  the index of that question reletive to the list
		q.setIndex(this.matcher.getNumIndex());
		
		//add to the question window.
		this.QuestionPage.append("\n" + this.matcher.getNumIndex() + ": "+ q.toString() + "\n");
		System.out.println("the answer is " + q.getAnswer() + "\nlen is " + q.getAnswer().length());
		
		//Can also use Default Caret Bottom.
		QuestionPage.setCaretPosition(QuestionPage.getDocument().getLength());
		
		//Spawn monsters (amount based on difficulty)
		spawnEnemies(q.getDifficulty());
		spawnPlayer();
		if(garea.players.size() > 1){
			garea.removePlayer(0);
		}
	}
	
	public void displayLesson1() {
		//load lesson 1
		/*
		icon = new ImageIcon(this.getClass().getResource("C:\\Users\\HisProdigalSon/Desktop/301/project/project-team10/301Project/graphics/Lessons/lessonOperators.png"));
		JLabel label = new JLabel(icon);
		label.setVisible(true);
		garea.add(label);
		*/
	}
	
	//cancels the input timertask
	public void stopWave(TimerTask t) {
		t.cancel();
		
	}
	
	//give a delay to the in
	public void delayWave(TimerTask t,long l ) throws InterruptedException {
		try {
			t.wait(l);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	int px;
	//spawns an enemy located at the top of the game area with a random x coordinate
	public void spawnEnemies(int qDifficulty) {
		int i = 0;
		//For each level of difficulty of the question, add an additional enemy
		while (i < qDifficulty) {
			//Make a random x coordinate
			int randX =  new Random().nextInt(486);
			//Reroll the random x value if it overlaps with previous enemy. Not foolproof
			for (Enemy enemy: garea.getEnemies()) {
				if ((randX > enemy.getXval() - 20) && (randX < enemy.getXval() + 20)) {
					randX =  new Random().nextInt(486);
				}
			}
			//Add the enemy to the game area
			px = randX;
			this.garea.addEnemy(new Enemy(randX, 10));
			i++;
		}
	}
		
	public void spawnPlayer() {
			this.garea.addPlayer(new Player(px, 400));	
	}
	
}
