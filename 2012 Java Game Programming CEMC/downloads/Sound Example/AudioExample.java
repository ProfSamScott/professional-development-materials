/**
 * This file is an example of how to play a sound in Java. Any sound you want
 * to play should have a .wav or a .mid extension (no mp3 files), and it must 
 * be in the same folder as your java program. Then cut and paste the lines that
 * are marked below...
 *
 * The .mid file format is "Midi" format. Midi files play cheezy-sounding synths
 * on your sound card. If you want music in your games, Midi is a great alternative
 * to Wav files, and gives the game a vintage sound. Lots of current songs are 
 * available as Midi files, often for ringtones.
 * 
 * WARNING: Wav files are uncompressed sound. They are VERY LARGE. Midi is often
 * a better choice.
 * 
 * Created September 8, 2008. 
 * Modified August 10, 2012. 
 * 
 * @author Sam Scott
 **/

package ExampleCode;

import hsa_ufa.Console;

// ****************************
// These lines have to be here. Cut and paste them into your code
import java.net.URL;
import java.applet.AudioClip;
import java.applet.Applet;
// ****************************

public class AudioExample
{
  static Console c;           // The output console
  
  // ******************************
  // NOTE: You have to have to add the "IOException" part to the end of the line below
  public static void main (String[] args) throws InterruptedException
    // ******************************
  {
    c = new Console ();
    
    // *****************************
    // THESE LINES PLAY THE SOUNDS. 
    // Cut and paste them into your program, and change the sounds to the ones
    // you want to play. 
    URL location = AudioExample.class.getResource("play_it2.wav"); // first sound
    AudioClip playIt = Applet.newAudioClip(location);
    
    location = AudioExample.class.getResource("eminem_therealslimshady.mid"); // second sound
    AudioClip song = Applet.newAudioClip(location);
    // *****************************
    
    playIt.play(); // this line starts the first sound
    
    // THE PROGRAM CONTINUES WHILE THE MUSIC PLAYS
    // You can also layer other audioclips, as in 
    // this Casablanca / Eminim remix.
    Thread.sleep(300);
    c.println("Play it!");
    Thread.sleep(1600);
    c.println("Yes Boss.");   
    Thread.sleep(1500);
    
    playIt.stop(); // stops the first sound
    song.play(); // starts the second sound
    
    Thread.sleep(500);
    c.println("Aww yeah!");
    Thread.sleep(7000);
    c.println("Here we go now.");
    Thread.sleep(7000);
    c.println("Uh huh.");
    Thread.sleep(4000);
    
    playIt.play();
    Thread.sleep(300);
    c.println("Play it!");
    Thread.sleep(1600);
    playIt.stop();
    Thread.sleep(2500);
    
    playIt.play();
    Thread.sleep(300);
    c.println("Play it!");
    Thread.sleep(1600);
    playIt.stop();
    Thread.sleep(2500);
    
    playIt.play();
    Thread.sleep(300);
    c.println("Play it!");
    Thread.sleep(1600);
    playIt.stop();
    Thread.sleep(2500);
    
    playIt.play();
    Thread.sleep(300);
    c.println("Play it!");
    Thread.sleep(1600);
    c.println("Yes boss.");
    Thread.sleep(2800);
    song.stop();
    
    c.setCursor(12, 39);
    c.println("Goodbye");
    
    Thread.sleep(1000);
    c.close();
    
  } // main method
} 

