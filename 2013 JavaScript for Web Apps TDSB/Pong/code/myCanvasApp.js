/**
 * Beginnings of a pong game, made with the canvas app template
 * 
 * @author Sam Scott, Sheridan College, 2013
 */

//***  GLOBAL VARIABLES

// player positions & speed
var player1x = 20;
var player2x = 670;
var player1y = 230;
var player2y = 230;
var playerSpeed = 5;

// ball position and speed
var ballX = 300;
var ballY = 250;
var ballSpeedX = 0;
var ballSpeedY = 0;

// player current direction
var p1Up = false;
var p1Down = false;
var p2Up = false;
var p2Down = false;

// player scores
var p1Score = 0;
var p2Score = 0;

// sounds
var ping = new Audio("sounds/ping.wav");
var pong = new Audio("sounds/pong.wav");
var bust = new Audio("sounds/bust.wav");

// image
var paddle = new Image();
paddle.src = "images/paddle.png";

/*
 * Customize the look of the canvas app
 */
function init() {
	// CUSTOMIZE YOUR APP
	setTitle("It's Pong!!!!! (sort of)"); // set title
	setByLine("by Sam Scott, Sheridan College, 2013"); // set name

	setCanvasSize(700,500); // canvas height and width in pixels

	setButton1("Start"); // ("" if not using)
	setButton2("Help"); // ("" if not using)

	setTimer(20); 
	// END OF CUSTOMIZATIONS
	
}

//*****************************
//KEYBOARD INPUT SECTION
//*****************************

/*
 * Changes the direction of the appropriate player
 * 
 * @param (number) code The key code of the key pressed 
 * @param (string) char A single character string for the key pressed
 */
function keyDown(code, char) {
	//debugOut("key press, code="+code+" char="+char);

	if (code == 65) {
		p1Up = true;
		p1Down = false;
	} else if (code == 90) {
		p1Down = true;
		p1Up = false;
	} else if (code == 38) {
		p2Up = true;
		p2Down = false;
	} else if (code == 40) {
		p2Down = true;
		p2Up = false;
	}
}

/*
 * Unused
 */
function keyPress(code, char) {}

/*
 * Stops player movement when a key is lifted
 * 
 * @param (number) code The key code of the key released 
 * @param (string) char A single character string for the key released
 */
function keyUp(code, char) {
	//debugOut("key up, code="+code+" char="+char);

	if (code == 65) 
		p1Up = false;
	else if (code == 90)
		p1Down = false;
	else if (code == 38)
		p2Up = false;
	else if (code == 40)
		p2Down = false;
	
}


//*****************************
//MOUSE INPUT SECTION -- UNUSED
//*****************************
function mouseDown(x, y, button) {}
function mouseUp(x, y, button) {}
function mouseMove(x, y) {}
function mouseOver(x, y) {}
function mouseOut(x, y) {}

//*****************************
//BUTTON INPUT SECTION
//*****************************

/*
 * Start the game
 * 
 * @param (number) button The mouse button clicked (usually 0)
 */
function button1Click(button) {
	//debugOut("button 1 click, button="+button);
	ballSpeedX = -7;
	ballSpeedY = 7;
	setButton1("");
}
/*
 * Show the help
 * 
 * @param (number) button The mouse button clicked (usually 0)
 */
function button2Click(button) {
	//debugOut("button 2 click, button="+button);
	alert("Player 1: A and Z keys\nPlayer 2: arrow keys");
}

//****************************
//TIMER SECTION
//****************************

/*
 * Main game method. Moves, checks collisions, and draws screen
 */
function clockTickEvent() {
	//debugOut("tick");

	// move ball
	ballX = ballX + ballSpeedX;
	ballY = ballY + ballSpeedY;

	// move paddles
	if (p1Up) 
		player1y = player1y - playerSpeed;
	else if (p1Down)
		player1y = player1y + playerSpeed;
	if (p2Up) 
		player2y = player2y - playerSpeed;
	else if (p2Down)
		player2y = player2y + playerSpeed;

	// bounce ball & score
	if (ballX < 0 || ballX > 699) {
		if (ballX < 0)
			p2Score++;
		else
			p1Score++;
		ballSpeedX = ballSpeedX * -1;
		ballX = ballX + ballSpeedX;
		bust.play();
	} else
		if (ballX < player1x+10 && ballX > player1x && ballSpeedX < 0 && ballY > player1y && ballY < player1y+40) {
			ballSpeedX = ballSpeedX * -1;
			ballX = ballX + ballSpeedX;
			ping.play();
		}
		else
			if (ballX > player2x+10 && ballX < player2x+20 && ballSpeedX > 0 && ballY > player2y && ballY < player2y+40) {
				ballSpeedX = ballSpeedX * -1;
				ballX = ballX + ballSpeedX;
				ping.play();
			}
	if (ballY < 0 || ballY > 499) {
		ballSpeedY = ballSpeedY * -1;
		ballY = ballY + ballSpeedY;
		pong.play();
	}

	// draw screen
	canvas.fillStyle = "black";
	canvas.fillRect(0,0,700,500);
	canvas.drawImage(paddle,player1x,player1y);
	canvas.drawImage(paddle,player2x,player2y);
	canvas.fillStyle="green";
	canvas.fillArc(ballX, ballY, 5, 0, 360);
	canvas.font = "24px monospace bold";
	canvas.fillStyle = "white";
	canvas.fillText(p1Score,20,30);
	canvas.fillText(p2Score,660,30);
	
}