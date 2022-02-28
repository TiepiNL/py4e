/*
The case of the Python Syndicate
Stage 3


Officer: 2628175
CaseNum: 301-2-56938332-2628175

Right kid let’s work out which of our ‘friends’ is connected to the syndicate.

- An object for Cecil karpinski has been declared and initialised
- Modify the x and y parameters of each image command using the x and y
properties from the Cecil karpinski object so the images remain at their correct
positions on the board.
- To do this you will need to combine add and subtract operators with the
relevant property for each parameter



*/

var photoBoard;
var pawelKarpinskiImage;
var linaLovelaceImage;
var robbieKrayImage;
var countessHamiltonImage;
var cecilKarpinskiImage;
var annaKarpinskiImage;

var cecilKarpinskiObject;




function preload()
{
	photoBoard = loadImage('photoBoard.png');
	pawelKarpinskiImage = loadImage("karpinskiBros2.png");
	linaLovelaceImage = loadImage("lina.png");
	robbieKrayImage = loadImage("krayBrothers2.png");
	countessHamiltonImage = loadImage("countessHamilton.png");
	cecilKarpinskiImage = loadImage("karpinskiBros1.png");
	annaKarpinskiImage = loadImage("karpinskiWoman.png");

}

function setup()
{
	createCanvas(photoBoard.width, photoBoard.height);
	cecilKarpinskiObject = {
		x: 408,
		y: 309,
		image: cecilKarpinskiImage
	};
}

function draw()
{
	image(photoBoard, 0, 0);

	//And update these image commands with your x and y coordinates.
	image(cecilKarpinskiObject.image, cecilKarpinskiObject.x, cecilKarpinskiObject.y);

	image(pawelKarpinskiImage, cecilKarpinskiObject.x - 293, cecilKarpinskiObject.y - 269);
	image(linaLovelaceImage, cecilKarpinskiObject.x, cecilKarpinskiObject.y - 269);
	image(robbieKrayImage, cecilKarpinskiObject.x + 293, cecilKarpinskiObject.y - 269);
	image(countessHamiltonImage, cecilKarpinskiObject.x - 293, cecilKarpinskiObject.y);
	image(annaKarpinskiImage, cecilKarpinskiObject.x + 293, cecilKarpinskiObject.y);

}