package backEnd;

import java.awt.Color;
import java.util.ArrayList;

import javax.swing.JLabel;
import backEnd.*;
import userInterface.*;

public class PlayerHealth {
	private Window w;
	private GameArea g;
	private JLabel PlayerHealth;
	private int player_health;
	private boolean gameover;
	
	
	public PlayerHealth(Window w) {
		this.w = w;
		g = w.getGameArea();
		gameover = g.getGameOver();
		PlayerHealth = w.getPlayerHealth();
		player_health = 100;

	}	
	public void resetHealth(){
		gameover = g.getGameOver();
		player_health = 100;
		PlayerHealth.setText("Health: " + player_health + "%");
		PlayerHealth.setForeground(Color.GREEN.darker());
	}
	
	public void updateHealth(ArrayList<Enemy> enemies){

		boolean need_to_remove= false;
		int num_remove = 0;
		for (Enemy enemy : enemies) {
			
			if ((enemy.reachedbottom())) {
				need_to_remove = true;
				num_remove += 1;
				player_health -= 20;
				if (player_health > 0) {
					if (player_health < 25) {
						PlayerHealth.setForeground(Color.red);
					} else if (player_health < 55) {
						PlayerHealth.setForeground(Color.orange);
					}
					PlayerHealth.setText("Health: " + player_health + "%");

				} else {
					g.setGameOver();
				}
			}
		}
		if (need_to_remove) {
			for (int i=0; i < num_remove; i++){
				g.removeEnemy(0);
				g.repaint();
			}
			
		}
	}	
	
}
