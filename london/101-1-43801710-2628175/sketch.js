/*

Officer: 2628175
CaseNum: 101-1-43801710-2628175

Case 101 - The Case of Lina Lovelace
Stage 2 - The Smalltalk Speakeasy

Well well, things have gotten interesting already ! No sooner does Lina step foot
in Console City than she heads straight for Smalltalk’s. Now be careful kid, that
place is a den of iniquity. Find out who she’s meeting and then get out as soon as
you can.

First identify Lina by drawing a rectangle with a blue outline around her.
She’s the woman in the red dress of course.

That woman with the cigarette and the feathered hat looks very familiar. Let’s identify her too by drawing
a rectangle with a green outline around her. Make sure you include her cigarette
and feather too.

The rectangles should cover the targets as accurately as possible without
including anything else.

There are many possible ways of investigating this case, but you
should use ONLY the following commands:

  rect()
  stroke() - Use only 255 or 0 for r,g,b values.

*/

var img;

function preload()
{
	img = loadImage('img.jpg');
}

function setup()
{
	createCanvas(img.width,img.height);
	noFill();
	strokeWeight(2);
}

function draw()
{
	image(img,0,0);

	//Write your code below here ...

	// rect Lina (blue)
	stroke(0,0,255);
	rect(685,300,800-685,538-300);

	// rect woman (green)
	stroke(0,255,0)
	rect(903,338,1019-903,538-338);


}
