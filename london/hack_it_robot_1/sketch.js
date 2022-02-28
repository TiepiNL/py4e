function setup()
{
	//create a canvas for the robot
	createCanvas(500, 500);
}

function draw()
{
	strokeWeight(6);

	//robots head
	fill(200);
	rect(100, 100, 300, 300, 20);


	//robots antenna
	fill(250, 250, 0);
	ellipse(150, 70, 60, 60);

	fill(200, 0, 200);
	rect(110, 80, 80, 30);

	//robots antenna
	fill(250, 250, 0);
	ellipse(250, 70, 60, 60);

	fill(200, 0, 200);
	rect(210, 80, 80, 30);

	//robots antenna
	fill(250, 250, 0);
	ellipse(350, 70, 60, 60);

	fill(200, 0, 200);
	rect(310, 80, 80, 30);

	//robots eyes
	fill(255, 255, 255);
	ellipse(175, 200, 160, 160);
	ellipse(325, 200, 160, 160);
	stroke(0, 0, 255);
	strokeWeight(50);
	point(175, 200);
	point(325, 200);
	stroke(0);
	strokeWeight();

	//robots nose
	fill(255, 215, 0);
	triangle(250, 220, 200, 300, 300, 300);

	//robots ears
	rect(80, 250, 30, 100);
	rect(390, 250, 30, 100);

	//robots mouth
	strokeWeight(20);
	stroke(255, 0, 0);
	noFill();
	beginShape();
	vertex(175, 340);
	vertex(200, 370);
	vertex(225, 340);
	vertex(250, 370);
	vertex(275, 340);
	vertex(300, 370);
	vertex(325, 340);
	endShape();
	strokeWeight();
	stroke(0);
}