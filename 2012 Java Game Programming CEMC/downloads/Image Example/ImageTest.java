/**
 * Demonstrates how to load and display gif or jpg images in a console
 * application. May 13, 2008. Modified September 15, 2008, September 23, 2009,
 * and October 20, 2010.
 *
 * @author Sam Scott
 **/
package ExampleCode;

import java.awt.*;
import hsa_ufa.Console;

public class ImageTest
{
  static Console c;           // The output console
  
  public static void main (String[] args) throws InterruptedException
  {
    c = new Console ();
    
    // These two lines load the image "robot.jpg" into a variable of type Image (an object type)
    // Note that you have to include the package name in the file name
    Image jpgImage;
    jpgImage = Toolkit.getDefaultToolkit ().getImage (c.getClass().getClassLoader().getResource("ExampleCode/robot.jpg"));
    
    // These two lines load the image "robot.gif" into a variable of type Image (an object type)
    Image gifImage;
    gifImage = Toolkit.getDefaultToolkit ().getImage (c.getClass().getClassLoader().getResource("ExampleCode/robot.gif"));
    
    
    // NOTE - java can also handle images in the .png format, and will respect
    // transparency values.
    
    // This line displays the jpeg image at top left location 0, 0
    // Don't worry about what null means, but you do need to include it
    // Note that the image name "jpgImage" is the first parameter
    c.drawImage (jpgImage, 0, 0);
    
    // These lines draw some more images scaled to 100 by 100 pixels.
    c.drawImage (jpgImage, 400, 0, 100, 100);
    c.drawImage (gifImage, 400, 100, 100, 100);
    c.drawImage (jpgImage, 400, 200, 100, 100);
    c.drawImage (gifImage, 400, 300, 100, 100);
    
    // *************************************
    // THE DRAWIMAGE COMMANDS ARE
    // c.drawImage(image, x, y, null) OR
    // c.drawImage(image, x, y, width, height, null)
    // *************************************
    
  } // main method
} // ImageTest class

