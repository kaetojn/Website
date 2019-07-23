package backEnd;

import java.awt.image.BufferedImage;
import java.io.IOException;

import javax.imageio.ImageIO;

public class Lesson {
	
	//The jpeg image representation of our Lesson
	private BufferedImage image;
	//x value coordinate of the lesson -> should be centered
	private int xCoor;
	//y value coordinate of the lesson -> should be centered
	private int Ycoor;
	
	public Lesson(int x, int y, String path) {
		//get the image and load it as the variable
		try {
			image = ImageIO.read(getClass(). getResourceAsStream(path));
		}
		catch(IOException e) {
			e.printStackTrace();
		}
		this.xCoor = x;
		this.Ycoor = y;
	}
	
	//return the image -> the lesson image
	public BufferedImage getImage() {
		return image;
	}
	
	//set the lesson to a new image -> would suggest a single instance of lesson?
	public void setImage(BufferedImage image) {
		this.image = image;
	}
	
	//get the xcoor
	public int getXCoor() {
		return xCoor;
	}
	
	//set the xcoor -> how big should it be -> where should it be?
	public void setXCoor(int xval) {
		this.xCoor = xval;
	}
	
	//return the ycoor
	public int getYCoor() {
		return Ycoor;
	}
	
	//set the yccor
	public void setYCoor(int yval) {
		this.Ycoor = yval;
	}
	

}
