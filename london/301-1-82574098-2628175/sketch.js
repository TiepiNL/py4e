/*
The case of the Python Syndicate
Stage 2


Officer: 2628175
CaseNum: 301-1-82574098-2628175

- Word on the street is that there is a new gang in town - The Python Syndicate.
It seems my bones were correct on this one. I need you to organise the gang
around the suspected leader Lina lovelace

- The variables for Lina lovelace have been declared and
initialised.
- Modify the x and y parameters of each image command using these two variables
so the images maintain their correct positions their correct positions on the board.
- To do this you will need to combine add and subtract operators with variables
Lina lovelace for for each parameter.
- Do not create any new variables
- Do not add any additional commands


*/

var photoBoard;
var countessHamiltonImg;
var cecilKarpinskiImg;
var bonesKarpinskiImg;
var linaLovelaceImg;
var pawelKarpinskiImg;
var annaKarpinskiImg;


var linaLovelaceXCoord = 115;
var linaLovelaceYCoord = 309;


function preload()
{
	photoBoard = loadImage('photoBoard.png');
	countessHamiltonImg = loadImage("countessHamilton.png");
	cecilKarpinskiImg = loadImage("karpinskiBros1.png");
	bonesKarpinskiImg = loadImage("karpinskiDog.png");
	linaLovelaceImg = loadImage("lina.png");
	pawelKarpinskiImg = loadImage("karpinskiBros2.png");
	annaKarpinskiImg = loadImage("karpinskiWoman.png");

}

function setup()
{
	createCanvas(photoBoard.width, photoBoard.height);
}

function draw()
{
	image(photoBoard, 0, 0);

	//And update these image commands with your x and y coordinates.
	image(linaLovelaceImg, linaLovelaceXCoord, linaLovelaceYCoord);
	image(countessHamiltonImg, linaLovelaceXCoord, linaLovelaceYCoord - 269);
	image(cecilKarpinskiImg, linaLovelaceXCoord + 293, linaLovelaceYCoord - 269);
	image(bonesKarpinskiImg, linaLovelaceXCoord + 586, linaLovelaceYCoord - 269);
	image(pawelKarpinskiImg, linaLovelaceXCoord + 293, linaLovelaceYCoord);
	image(annaKarpinskiImg, linaLovelaceXCoord + 586, linaLovelaceYCoord);

}