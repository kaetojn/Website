package backEnd;

import java.awt.Graphics;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

import javax.swing.JPanel;

public class GameArea extends JPanel {

	private static final long serialVersionUID = 1L;
	private ArrayList<Enemy> enemies;
	public ArrayList<Player> players;
	public ArrayList<Effect> explosions;
	
	//the list of our current lesson, could be changed to a single lesson maybe?
	private Lesson currentLesson;
	private boolean showLesson;
	private boolean gameover;

	
	public GameArea() {
		enemies = new ArrayList<Enemy>();
		players = new ArrayList<Player>();
		explosions = new ArrayList<Effect>();
		//currentLesson = new Lesson(0, 0);
		showLesson = false; //set to true initially
		gameover = false;
	}
	
	public void setLesson(Lesson l) {
		this.currentLesson = l;
		this.showLesson = true;
	}
	
	public void setGameOver() {
		gameover = true;
	}
	
	@Override
	public void paint(Graphics g) {
		super.paint(g);
		
		//Add a bool for whether to draw
		//TODO add the paint for lessons
		
		if (gameover) {
			GameOver gameover_graphic = new GameOver();
			g.drawImage(gameover_graphic.getImage(), gameover_graphic.getXCoor(),
					gameover_graphic.getYCoor(),this.getSize().width,this.getSize().height,null);

		} 
		else if (showLesson){
			g.drawImage(currentLesson.getImage(), currentLesson.getXCoor(),
					currentLesson.getYCoor(),this.getSize().width,this.getSize().height,null);
		}//only render the lesson if we have it set to true
		
		else {
			
			for (Player player : players) {
				//Add two more parameters after getYval to set image dimensions
				g.drawImage(player.getImage(), player.getXval(), player.getYval(), 40, 52, null);
			}
			
			
			for (Enemy enemy : enemies) {
				//Add two more parameters after getYval to set image dimensions
				g.drawImage(enemy.getImage(), enemy.getXval(), enemy.getYval(), 30, 46, null);
			}
			for (Effect explode : explosions) {
				//Add two more parameters after getYval to set image dimensions
				g.drawImage(explode.getImage(), explode.getXval(), explode.getYval(), 30, 37, null);
			}
		}
	}


	public ArrayList<Enemy> getEnemies() {
		return enemies;
	}
	
	public ArrayList<Player> getPlayers() {
		return players;
	}
	
	//returns the list for the current lessons
	public Lesson getLesson() {
		return this.currentLesson;
	}
	//toggle Lesson
	public void toggleLesson() {
		this.showLesson = !this.showLesson;
		//switch back and forth between shoing the lesson or not
	}
	
	public boolean isLessonActive() {
		return this.showLesson;
	}
	
	public boolean getGameOver() {
		return gameover;
	}

	public void addEnemy(Enemy enemy) {
		enemies.add(enemy);
	}

	public void addPlayer(Player player) {
		players.add(player);
	}
	
	public void addExplosion(Effect explode) {
		explosions.add(explode);
	}
	
	public void removeEnemy(int index) {
		if (enemies.size() > index) {
			enemies.remove(index);
		}
	}
	public void removePlayer(int index) {
		if (players.size() > index) {
			players.remove(index);
		}
	}
	public void removeExplosion() {
		while(explosions.size() != 0){
		explosions.remove(0);
		}
	}
}
