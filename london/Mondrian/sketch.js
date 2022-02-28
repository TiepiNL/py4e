let margin = 20;
let line = 35;

function setup()
{
	//create a large square canvas
	createCanvas(1000, 1000);
}

function draw()
{
	//set a thick stroke weight for the black lines
	strokeWeight(0);

	//draw the red rectangle 
	fill(255, 0, 0);
	rect(6 * line + margin, 0 * line + margin, 12 * line, 12 * line);

	//draw the blue rectangle
	fill(0, 0, 255);
	rect(0 * line + margin, 13 * line + margin, 5 * line, 6 * line);

	//draw the yellow rectangle
	fill(255, 255, 0);
	rect(16 * line + margin, 16.5 * line + margin, 2 * line, 2.5 * line);

	//draw the black lines
	fill(0, 0, 0);

	// horizontal 1 (short)
	rect(0 * line + margin, 4.5 * line + margin, 5 * line, 1.5 * line);

	// horizontal 2 (full)
	rect(0 * line + margin, 12 * line + margin, 18 * line, 1 * line);

	// horizontal 3 (short)
	rect(16 * line + margin, 15 * line + margin, 2 * line, 1.5 * line);

	// vertical 1 (full)
	rect(5 * line + margin, 0 * line + margin, 1 * line, 19 * line);

	// vertical 2 (short)
	rect(15 * line + margin, 13 * line + margin, 1 * line, 6 * line);
}