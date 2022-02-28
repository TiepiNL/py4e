function setup()
{
	//create a canvas for the robot
	createCanvas(1000, 700);
}

function draw()
{
	// Draw the robot antennas
	strokeWeight(8);
	//robot 1
	stroke(31, 34, 18);
	beginShape(); //left
	vertex(155, 190);
	vertex(115, 115);
	endShape();
	beginShape(); //right
	vertex(155, 190);
	vertex(195, 115);
	endShape();
	//robot 2
	stroke(86, 86, 86);
	beginShape(); //left
	vertex(455, 190);
	vertex(415, 115);
	endShape();
	beginShape(); //right
	vertex(455, 190);
	vertex(495, 115);
	endShape();
	//robot 3
	stroke(164, 198, 57);
	beginShape(); //left
	vertex(755, 190);
	vertex(715, 115);
	endShape();
	beginShape(); //right
	vertex(755, 190);
	vertex(795, 115);
	endShape();

	noStroke();

	// Draw the robot heads
	//robot 1
	fill(31, 34, 18);
	ellipse(155, 190, 130, 130);
	//robot 2
	fill(86, 86, 86);
	ellipse(455, 190, 130, 130);
	//robot 3
	fill(164, 198, 57);
	ellipse(755, 190, 130, 130);

	// Draw the robot "necks"
	fill(255);
	rect(90, 190, 130, 10); //robot 1
	rect(390, 190, 130, 10); //robot 2
	rect(690, 190, 130, 10); //robot 3

	// Draw the robot eyes
	fill(255);
	ellipse(130, 157.5, 15, 15); // robot 1 - left
	ellipse(180, 157.5, 15, 15); // robot 1 - right
	ellipse(430, 157.5, 15, 15); // robot 2 - left
	ellipse(480, 157.5, 15, 15); // robot 2 - right
	ellipse(730, 157.5, 15, 15); // robot 3 - left
	ellipse(780, 157.5, 15, 15); // robot 3 - right

	// Draw the robot bodies
	//robot 1
	fill(31, 34, 18);
	rect(90, 200, 130, 130, 0, 0, 15, 15); //body
	rect(50, 200, 30, 90, 50); //arm 1
	rect(230, 200, 30, 90, 50); //arm 2
	rect(115, 330, 30, 45, 0, 0, 50, 50); //leg 1
	rect(165, 330, 30, 45, 0, 0, 50, 50); //leg 2
	//robot 2
	fill(86, 86, 86);
	rect(390, 200, 130, 130, 0, 0, 15, 15); //body
	rect(350, 200, 30, 90, 50); //arm 1
	rect(530, 200, 30, 90, 50); //arm 2
	rect(415, 330, 30, 45, 0, 0, 50, 50); //leg 1
	rect(465, 330, 30, 45, 0, 0, 50, 50); //leg 2
	//robot 3
	fill(164, 198, 57);
	rect(690, 200, 130, 130, 0, 0, 15, 15); //body
	rect(650, 200, 30, 90, 50); //arm 1
	rect(830, 200, 30, 90, 50); //arm 2
	rect(715, 330, 30, 45, 0, 0, 50, 50); //leg 1
	rect(765, 330, 30, 45, 0, 0, 50, 50); //leg 2

}