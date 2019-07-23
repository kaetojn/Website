package backEnd;

import java.awt.image.BufferedImage;

public interface Sprite {

	public BufferedImage getImage();
	
	public void setImage(BufferedImage image);
	
	public int getXval();
	
	public void setXval(int xval);
	
	public int getYval();
	
	public void setYval(int yval);
}
