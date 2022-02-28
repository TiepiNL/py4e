/*

Officer: 2628175
CaseNum: 303-2-54532425-2628175

Case 303 - The Case of the Crooked Attorney
Stage 3 - The Gates Bank

I’ve made an appointment for you at the Gates Bank to retrieve your safe deposit box from the vault.
Actually you will break into Torvalds’ one.

Crack the safe by doing the following:

	When the mouse button is pressed:
	- Make Secure_Locker_Key_0 equal to the value of mouseY
	- Use the 'max' function to prevent Secure_Locker_Key_0 from falling below 1

	When the mouse button is pressed:
	- Decrement Secure_Locker_Key_1 by 2
	- Use the 'max' function to prevent Secure_Locker_Key_1 from falling below 6

	Whilst the mouse is being dragged:
	- Make Secure_Locker_Key_2 equal to the value of mouseX
	- Use the 'max' function to prevent Secure_Locker_Key_2 from falling below 2

	Whilst the mouse is being dragged:
	- Decrement Secure_Locker_Key_3 by 3
	- Use the 'max' function to prevent Secure_Locker_Key_3 from falling below 4

	When the mouse button is pressed:
	- Make Secure_Locker_Key_4 equal to the value of mouseY
	- Use the 'min' function to prevent Secure_Locker_Key_4 from going above 80



This time you'll need to create the relevant event handlers yourself.

There are many possible ways of investigating this case, but you
should use ONLY the following commands:

	- The assignment operator aka. the equals sign !
	- mouseX, mouseY
	- Incrementing +=
	- Decrementing -=
	- min, max
	- constrain

*/

//declare the variables

var Secure_Locker_Key_0;
var Secure_Locker_Key_1;
var Secure_Locker_Key_2;
var Secure_Locker_Key_3;
var Secure_Locker_Key_4;


function preload()
{
	//IMAGES WILL BE LOADED HERE

}

function setup()
{
	createCanvas(512,512);

	//initialise the variables
	Secure_Locker_Key_0 = 0;
	Secure_Locker_Key_1 = 0;
	Secure_Locker_Key_2 = 0;
	Secure_Locker_Key_3 = 0;
	Secure_Locker_Key_4 = 0;

}

///////////////////EVENT HANDLERS///////////////////

//Create event handlers here to open the safe ...
function mousePressed() {
	console.log("mousePressed");
	Secure_Locker_Key_0 = mouseY;
	Secure_Locker_Key_0 = max(Secure_Locker_Key_0, 1);
	Secure_Locker_Key_1 -= 2;
	Secure_Locker_Key_1 = max(Secure_Locker_Key_1, 6);
	Secure_Locker_Key_4 = mouseY;
	Secure_Locker_Key_4 = min(Secure_Locker_Key_4, 80);
}

function mouseDragged() {
	console.log("mouseDragged", mouseX, mouseY);
	Secure_Locker_Key_2 = mouseX;
	Secure_Locker_Key_2 = max(Secure_Locker_Key_2, 2);
	Secure_Locker_Key_3 -= 3;
	Secure_Locker_Key_3 = max(Secure_Locker_Key_3, 4);
}


///////////////DO NOT CHANGE CODE BELOW THIS POINT///////////////////

function draw()
{

	//Draw the safe door
	background(70);
	noStroke();
	fill(29,110,6);
	rect(26,26,width-52,width-52);

	//Draw the combination dials
	push();
	translate(120,170);
	drawDial(140,Secure_Locker_Key_0, 14);
	pop();

	push();
	translate(120,380);
	drawDial(140,Secure_Locker_Key_1, 26);
	pop();

	push();
	translate(280,170);
	drawDial(140,Secure_Locker_Key_2, 13);
	pop();

	push();
	translate(280,380);
	drawDial(140,Secure_Locker_Key_3, 22);
	pop();

	//Draw the lever
	push();
	translate(width - 125,256);
	drawLever(Secure_Locker_Key_4);
	pop();


}

function drawDial(diameter,num,maxNum)
{
	//the combination lock

	var r = diameter * 0.5;
	var p = r * 0.6;

	stroke(0);
	fill(255,255,200);
	ellipse(0,0,diameter,diameter);
	fill(100);
	noStroke();
	ellipse(0,0,diameter*0.66,diameter*0.66);
	fill(150,0,0);
	triangle(
		-p * 0.4,-r-p,
		p * 0.4,-r-p,
		0,-r-p/5
	);

	noStroke();

	push();
	var inc = 360/maxNum;

	rotate(radians(-num * inc));
	for(var i = 0; i < maxNum; i++)
	{
		push();
		rotate(radians(i * inc));
		stroke(0);
		line(0,-r*0.66,0,-(r-10));
		noStroke();
		fill(0);
		text(i,0,-(r-10));
		pop();
	}

	pop();
}

function drawLever(rot)
{
	push();
	rotate(radians(-rot))
	stroke(0);
	fill(100);
	rect(-10,0,20,100);
	ellipse(0,0,50,50);
	ellipse(0,100,35,35);
	pop();
}
