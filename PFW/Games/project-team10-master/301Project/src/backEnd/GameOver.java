package backEnd;

import java.awt.image.BufferedImage;
import java.io.IOException;

import javax.imageio.ImageIO;

public class GameOver {

	private BufferedImage game_over_image;
	//x value coordinate of game_over_image -> should be centered
	private int xCoor;
	//y value coordinate of game_over_image -> should be centered
	private int Ycoor;
	
	public GameOver() {
		//get the image and load it as the variable
		try {
			game_over_image = ImageIO.read(getClass(). getResourceAsStream("/gameover.jpg"));
		}
		catch(IOException e) {
			e.printStackTrace();
		}
		this.xCoor = 0;
		this.Ycoor = 0;
	}
	
	public BufferedImage getImage() {
		return game_over_image;
	}
	
	public int getXCoor() {
		return xCoor;
	}


	public int getYCoor() {
		return Ycoor;
	}
	
	
	

}
