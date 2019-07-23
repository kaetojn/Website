import java.io.File;
import java.util.Arrays;
import java.util.List;
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

public class LevelGenerator {
	
	
	
	// code moved to Level
	// use this to generate the levels
	private int curLevel;
	private Window window;
	private QuestionFactory qf;
	
	public LevelGenerator(Window w, QuestionFactory qf) {
		
		this.curLevel = 0;
		this.qf = qf;
		this.window = w;
		
	}
	
	public Level createLevel(Lesson lesson, List<type> qtypes, PlayerHealth health) {
		
		this.curLevel++;

		Level level = new Level(this.window.getQuestionText(), this.window.getInputMatcher(), this.window.getGameArea(),  this.qf, lesson, qtypes, health);
		
		
		return level;
	}
		
	
}
