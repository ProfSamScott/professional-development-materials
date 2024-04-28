/**
 * This is a template for developing your own web app using the HTML5 canvas.
 * 
 * Don't forget to change this comment header, along with the comment headers for any
 * functions you decide to use. And add your name below.
 * 
 * @author your name here
 * @author Sam Scott, Sheridan College, 2013
 */

// *** YOUR GLOBAL VARIABLES AND FUNCTIONS HERE


// *******************************************

/*
 * This method executes once at the beginning of your web app, after the
 * page has loaded.
 */
function init() {
	// CUSTOMIZE YOUR APP
	setTitle("Canvas App Template"); // set title
	setByLine("by Sam Scott, Sheridan College, 2013"); // set name
	
	setCanvasSize(700,500); // canvas height and width in pixels
	
	setButton1("Button 1"); // ("" if not using)
	setButton2("Button 2"); // ("" if not using)
	
	setTimer(0); 			// set interval (in ms) for clock ticks. 0 = no clock.
	// END OF CUSTOMIZATIONS
	
	//*** Your Code Here
}

//*****************************
//KEYBOARD INPUT SECTION
//*****************************

/*
 * Called when a key is pressed. Works for all keys including shift, arrows, etc.
 * Note that the code is a KEY code, not necessarily an ASCII or UNICODE code. 
 * Therefore the char parameter might not be completely accurate.
 * 
 * @param (number) code The key code of the key pressed 
 * @param (string) char A single character string for the key pressed
 */
function keyDown(code, char) {
	//debugOut("key press, code="+code+" char="+char);

	//*** Your Code Here
}

/*
 * Very similar to keyDown, but the code is ASCII/UNICODE and it does not work
 * for keys such as shift or the arrow keys. 
 * 
 * @param (number) code The ASCII/UNICODE code of the key pressed 
 * @param (string) char A single character string for the key pressed
 */
function keyPress(code, char) {
	//debugOut("key press, code="+code+" char="+char);

	//*** Your Code Here
}

/*
 * Called when a key is released. Works for all keys including shift, arrows, etc.
 * See the notes on keyUp() for more info
 * 
 * @param (number) code The key code of the key released 
 * @param (string) char A single character string for the key released
 */
function keyUp(code, char) {
	//debugOut("key up, code="+code+" char="+char);

	//*** Your Code Here
}


//*****************************
//MOUSE INPUT SECTION
//*****************************

/*
 * Called when the mouse is clicked on the canvas.
 * 
 * @param (number) x The x location on the canvas
 * @param (number) y The y location on the canvas
 * @param (number) button The mouse button clicked (usually 0)
 */
function mouseDown(x, y, button) {
	//debugOut("mouse down, x="+x+" y="+y+" button="+button);

	//*** Your Code Here
}

/*
 * Called when the mouse button is released on the canvas.
 * 
 * @param (number) x The x location on the canvas
 * @param (number) y The y location on the canvas
 * @param (number) button The mouse button clicked (usually 0)
 */
function mouseUp(x, y, button) {
	//debugOut("mouse up, x="+x+" y="+y+" button="+button);

	//*** Your Code Here
}

/*
 * Called when the mouse is moved on the canvas.
 * 
 * @param (number) x The x location on the canvas
 * @param (number) y The y location on the canvas
 */
function mouseMove(x, y) {
	//debugOut("mouse move, x="+x+" y="+y);

	//*** Your Code Here
}
/*
 * Called when the mouse moves into the canvas area.
 * 
 * @param (number) x The x location on the canvas
 * @param (number) y The y location on the canvas
 */
function mouseOver(x, y) {
	//debugOut("mouse over, x="+x+" y="+y);

	//*** Your Code Here
}
/*
 * Called when the mouse moves off the canvas.
 * 
 * @param (number) x The x location on the canvas
 * @param (number) y The y location on the canvas
 */
function mouseOut(x, y) {
	//debugOut("mouse out, x="+x+" y="+y);

	//*** Your Code Here
}

//*****************************
//BUTTON INPUT SECTION
//*****************************

/*
 * Called when button 1 is clicked.
 * 
 * @param (number) button The mouse button clicked (usually 0)
 */
function button1Click(button) {
	//debugOut("button 1 click, button="+button);
}
/*
 * Called when button 2 is clicked.
 * 
 * @param (number) button The mouse button clicked (usually 0)
 */
function button2Click(button) {
	//debugOut("button 2 click, button="+button);
}

//****************************
//TIMER SECTION
//****************************

/*
 * This function is called every time there is a clock tick. Set it up using
 * a call to setTimer(). If you set the timer to 0 it will stop.
 */
function clockTickEvent() {
	//debugOut("tick");
}