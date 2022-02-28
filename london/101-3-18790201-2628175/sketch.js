/*

Officer: 2628175
CaseNum: 101-3-18790201-2628175

Case 101 - The Case of Lina Lovelace
Stage 4 - The Plaza Hotel

Okay this place is more Lina’s style. Now’s our chance to find out the root of all
of this. Lets see who is Lina meeting.

Identify Lina by drawing a magenta filled rectangle with a yellow outline.
She’s the woman in the red dress of course.

Identify the man with the monocle smoking the cigar blue filled
rectangle with a red outline around him.

Identify the man reading the newspaper by drawing a yellow filled rectangle
with a cyan outline around him.

Identify the woman with the dog by drawing a cyan filled rectangle with a
blue outline around her. Make sure you include the dog too.

The rectangles should cover the targets as accurately as possible without
including anything else.

There are many possible ways of investigating this case, but you
should use ONLY the following commands:

  rect()
  fill() Use only 255 or 0 for r,g,b values. Set alpha to 100 for some opacity.
	stroke() Use only 255 or 0 for r,g,b values.

*/

var img;

function preload()
{
	img = loadImage('img.jpg');
}

function setup()
{
	createCanvas(img.width,img.height);
	strokeWeight(2);
}

function draw()
{
	image(img,0,0);

	//Write your code below here ...

	//Lina: magenta filled rectangle with a yellow outline.
	fill(255, 0, 255, 100);
	stroke(255, 255, 0);
	rect(322, 237, 536-322, 677-237);

    //Monocle smoking man: blue filled rectangle with a red outline.
	fill(0, 0, 255, 100);
	stroke(255, 0, 0);
	rect(13, 349, 136-13, 514-349);

    //Nnewspaper man: yellow filled rectangle with a cyan outline.
	fill(255, 255, 0, 100);
	stroke(0, 255, 255);
	rect(1123, 308, 1288-1123, 627-308);

    //Woman with the dog: cyan filled rectangle with a blue outline.
	fill(0, 255, 255, 100);
	stroke(0, 0, 255);
	rect(725, 230, 857-725, 508-230);

}
