import java.awt.*;
import hsa_ufa.Console;

/**
 * Shows how to use the getKeyChar() and getLastKeyChar() methods.
 * @author Sam Scott
 **/
public class TestGetKeyChar
{
  static Console c = new Console();           // The output console
  
  public static void main (String[] args) throws InterruptedException
  {  
    c.println ("This is a test of c.getKeyChar() and c.getLastKeyChar().");
    c.println ("Char on the left is getKeyChar, and right is getLastKeyChar.");
    c.println ("Hit any key");
    c.getChar ();
    
    for (;;)
    {
      Thread.sleep (10);
      c.println ("   " + c.getKeyChar() + "\t" + c.getLastKeyChar());
    }
  } // main method
} // TestGetCurrentKey class
