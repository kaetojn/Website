package backEnd;

import java.awt.image.BufferedImage;
import java.io.IOException;

import javax.imageio.ImageIO;

public class Enemy implements Sprite {

	//The png image representation of our enemy
	private BufferedImage image;
	//x value coordinate of the enemy
	private int xval;
	//y value coordinate of the enemy
	private int yval;
	
	public Enemy(int x, int y) {
		//Current image used licenced under Creative Commons 3.0.  Attribution to: Irina Mir (irmirx)
		try {
			image = ImageIO.read(getClass(). getResourceAsStream("/zombie.png"));
		}
		catch(IOException e) {
			e.printStackTrace();
		}
		this.xval = x;
		this.yval = y;
	}
	
	public BufferedImage getImage() {
		return image;
	}
	public void setImage(BufferedImage image) {
		this.image = image;
	}
	
	public int getXval() {
		return xval;
	}
	public void setXval(int xval) {
		this.xval = xval;
	}
	
	public int getYval() {
		return yval;
	}
	public void setYval(int yval) {
		this.yval = yval;
	}
	
	public void moveDown(int num) {
		yval += num;
	}
	
	public boolean reachedbottom() {
		return yval >= 400;
	}
}
