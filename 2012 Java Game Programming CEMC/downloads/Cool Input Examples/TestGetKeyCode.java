import java.awt.*;
import hsa_ufa.Console;

/**
 * Shows how to use the getKeyCode() and getLastKeyCode() methods.
 * @author Sam Scott
 **/
public class TestGetKeyCode
{
  static Console c = new Console();           // The output console
  
  public static void main (String[] args) throws InterruptedException
  {    
    c.println ("This is a test of c.getKeyCode() and c.getLastKeyCode().");
    c.println ("Char on the left is getKeyCode, and right is getLastKeyCode.");
    c.println ("Hit any key");
    c.getChar ();
    
    for (;;)
    {
      Thread.sleep (10);
      c.println ("   " + c.getKeyCode () + "\t" + c.getLastKeyCode ());
    }
  } // main method
} // TestGetCurrentKey class
