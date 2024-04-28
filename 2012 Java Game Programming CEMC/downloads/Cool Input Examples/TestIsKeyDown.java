import java.awt.*;
import hsa_ufa.Console;

/**
 * Shows how to use the isKeyDown() method.
 * @author Sam Scott
 **/
public class TestIsKeyDown
{
  static Console c = new Console();           // The output console
  
  public static void main (String[] args) throws InterruptedException
  {  
   
    for (;;)
    {
      Thread.sleep (10);
      c.clear();
      c.println ("This is a test of c.isKeyDown().");
      c.println ("Try it by pressing 'a' and 'Shift'.");
      c.setCursor(10,10);
      if (c.isKeyDown('A')) // can be used with a char
        c.println("A is down");
      c.setCursor(11,10);
      if (c.isKeyDown(Console.VK_SHIFT))  // can also be used with an ascii code
        c.println("Shift key is down");
    }
  } // main method
} // TestGetCurrentKey class
