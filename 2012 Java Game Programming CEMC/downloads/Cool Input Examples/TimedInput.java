package ExampleCode;

import java.awt.*;
import hsa_ufa.Console;

/**
 * This is an example of how to use the hsa_ufa class to time the user's
 * input. May 12, 2008.
 *
 * @author Sam Scott
 **/
public class TimedInput
{
  static Console c;
  
  /**
   * Gives the user 2 seconds to answer a simple question.
   *
   * @param args
   * @throws InterruptedException
   **/
  public static void main (String[] args) throws InterruptedException
  {
    c = new Console ();
    
    char userInput = ' ';
    boolean answered;
    int time;
    
    // PROGRAM INTRO
    c.println ("Press enter to start.");
    while (c.getChar () != (char) 10)   // waits for enter (char 10)
      ;
    
    // THE QUESTION
    c.clear ();
    c.println ("Quick - what's your favorite color? (You have 2 seconds to answer)");
    c.println ("b = blue, r = red, g = green.");
    
    // THE TIMED INPUT LOOP
    answered = false;
    time = 0;
    
    for (int i = 0 ; i < 200 ; i++) // loop 200 times
    {
      Thread.sleep (10); // 10*200 = 2000 ms (2 seconds)
      userInput = c.getKeyChar ();
      if (userInput == 'b' | userInput == 'r' | userInput == 'g')
      {
        answered = true; // we got an answer
        time = i * 10; // how long it took
        break; // exit the for loop
      }
    }
    
    // FEEDBACK FOR THE USER
    if (answered)
    {
      switch (userInput)
      {
        case 'b':
          c.setColor (Color.blue);
          break;
        case 'r':
          c.setColor (Color.red);
          break;
        case 'g':
          c.setColor (Color.green);
          break;
      }
      c.println ("Good Choice");
      c.setColor (Color.black);
      c.println ("You answered in " + time + " ms.");
    }
    else
      c.println ("Too slow. I win.");
  }
}
