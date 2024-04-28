/**
 * This class demonstrates how to use a for loop to make an object
 * move across the screen. November 7, 2006.
 * Updated January 19, 2010.
 *
 * @author Sam Scott
 **/
package ExampleCode;

import java.awt.*;
import hsa_ufa.Console;

public class ForLoopMovingObjects
{
  static Console c;           // The output console
  
  public static void main (String[] args) throws InterruptedException
  {
    c = new Console ();
    
    // This loop moves the object from left to right by changing
    // the x value from 0 to 1000. 
    for (int x = 0 ; x < 1000 ; x = x + 1)
    {
      synchronized(c) { // synchronize to avoid flicker
        c.clear();   // clear the screen
        c.drawStar (x, 100, 50, 50);    // draw the star
      }
      Thread.sleep (5);               // wait a little while (change to alter speed)
    }
  } // main method
} // MovingObjects class
