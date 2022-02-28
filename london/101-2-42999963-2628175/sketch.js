/*

Officer: 2628175
CaseNum: 101-2-42999963-2628175

Case 101 - The Case of Lina Lovelace
Stage 3 - The Docks

You’ve followed Lina down to the docks. She sure frequents some classy places.
Okay let’s see who she’s meeting down there.

Identify Lina by drawing a yellow filled rectangle around her.
She’s the woman in the red dress of course.

Identify the heavy-set man in the fishing overalls by drawing a blue filled
rectangle around him.

Identify the man in the striped top by drawing a green filled rectangle around
him.

The rectangles should cover the targets as accurately as possible without
including anything else.

There are many possible ways of investigating this case, but you
should use ONLY the following commands:

  rect()
  fill() Use only 255 or 0 for r,g,b values. Set alpha to 100 for some opacity.

*/

var img;

function preload()
{
	img = loadImage('img.jpg');
}

function setup()
{
	createCanvas(img.width,img.height);
	noStroke();
}

function draw()
{
	image(img,0,0);

	//Write your code below here ...

	//Lina: yellow filled rectangle
	fill(255,255,0,100);
	rect(1515,216,1699-1515,591-216);
	

	//Heavy-set man: blue filled rectangle
	fill(0,0,255,100);
	rect(1089,238,1402-1089,576-238);	

	//Striped top man: green filled rectangle
	fill(0,255,0,100);
	rect(745,505,952-745,1074-505);

}
