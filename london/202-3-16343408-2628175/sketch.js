/*

Officer: 2628175
CaseNum: 202-3-16343408-2628175

Case 202 - The case of Bob and Daisy - stage 4

Here’s the final letter from Daisy (aka. Woz). Decode it to uncover the
final details about Woz and Job’s dastardly plan.

Discover the hidden code by commenting out all text commands except
those which produce pink filled text with magenta outline in Melissa font.
Only comment out text commands - leave fill & stroke, push and pop commands uncommented.

There are many possible ways of investigating this case, but you
should use ONLY the following commands:

  // comments are all that are needed for this case.
  Do NOT add any new lines of code.

*/

var letterFont;

function preload()
{
	Ballpointprint = loadFont('Ballpointprint.ttf');
	Melissa = loadFont('Melissa.otf');
	Diggity = loadFont('Diggity.ttf');
	RonsFont = loadFont('RonsFont.ttf');
}

function setup()
{
	createCanvas(524,498);
	textSize(29);
}

function draw()
{
	background(255);

	fill(255,255,0);
	stroke(0,0,255);
	textFont(Ballpointprint);
	//text("My", 16,29);
	//text("so,", 339,87);
	stroke(0,0,0);
	textFont(RonsFont);
	//text("dar", 62,29);
	push();
	fill(255,192,203);
	textFont(Melissa);
	//text("how", 108,249);
	pop();
	textFont(Ballpointprint);
	//text("yours,", 109,340);
	//text("ps", 110,184);
	push();
	stroke(255,0,255);
	//text("Are", 16,87);
	//text("Daisy", 16,398);
	pop();
	textFont(Diggity);
	//text("long", 126,120);
	//text("of", 183,87);
	stroke(255,0,0);
	textFont(Melissa);
	//text("no", 102,120);
	fill(255,192,203);
	textFont(RonsFont);
	//text("our", 230,219);
	fill(0,255,255);
	textFont(Melissa);
	//text("we", 144,184);
	//text("take", 343,249);
	fill(255,192,203);
	textFont(Ballpointprint);
	//text("all", 104,219);
	fill(0,255,255);
	stroke(255,0,255);
	//text("and", 439,184);
	//text("sort", 17,219);
	textFont(Melissa);
	//text("me", 463,149);
	fill(255,255,0);
	textFont(Diggity);
	//text("The", 408,249);
	//text("I", 55,120);
	//text("er", 155,120);
	fill(255,192,203);
	stroke(0,0,255);
	//text("?", 293,87);
	//text("break", 373,184);
	textFont(Ballpointprint);
	//text("Perha", 49,184);
	fill(0,255,255);
	stroke(0,255,0);
	textFont(Diggity);
	//text("not", 13,249);
	fill(255,165,0);
	stroke(0,0,0);
	textFont(Melissa);
	//text("Are", 329,149);
	fill(255,192,203);
	stroke(0,255,0);
	//text("away", 267,184);
	fill(255,255,0);
	stroke(255,0,255);
	textFont(Diggity);
	//text("I'm", 458,219);
	push();
	textFont(Melissa);
	//text("?", 442,219);
	pop();
	stroke(0,0,255);
	textFont(RonsFont);
	//text("You", 14,149);
	fill(0,255,255);
	textFont(Diggity);
	//text("the", 101,282);
	push();
	fill(255,165,0);
	//text("should", 176,184);
	//text("send", 425,87);
	pop();
	textFont(Ballpointprint);
	//text("continual", 340,120);
	//text("ignore", 188,120);
	fill(255,165,0);
	textFont(Diggity);
	//text("silence.", 145,282);
	stroke(255,0,0);
	//text("sho", 121,87);
	//text("rt", 150,87);
	stroke(0,0,0);
	//text("much", 146,249);
	//text("are", 65,149);
	push();
	fill(255,192,203);
	stroke(255,0,0);
	textFont(Melissa);
	//text("cash.", 8,120);
	pop();
	textFont(Ballpointprint);
	//text("x", 92,398);
	//text("these", 266,120);
	push();
	textFont(Diggity);
	//text("can", 301,249);
	pop();
	stroke(0,255,0);
	textFont(RonsFont);
	//text("ling", 108,29);
	textFont(Melissa);
	//text("ed", 182,149);
	fill(0,255,255);
	//text("If", 315,87);
	stroke(255,0,255);
	textFont(Diggity);
	//text("a", 350,184);
	//text("so", 109,149);
	//text("sure", 55,249);
	fill(255,192,203);
	stroke(0,0,0);
	textFont(Ballpointprint);
	//text("sometimes.", 207,149);
	fill(0,255,255);
	stroke(0,255,0);
	//text("Is", 186,219);
	fill(255,255,0);
	textFont(Melissa);
	//text("avoiding", 397,149);
	//text("this", 66,219);
	//text("can", 69,120);
	stroke(0,0,255);
	textFont(Diggity);
	//text("?", 386,249);
	//text("relationship", 287,219);
	stroke(255,0,0);
	textFont(Ballpointprint);
	//text("out.", 140,219);
	//text("money", 216,87);
	fill(255,192,203);
	stroke(0,255,0);
	textFont(RonsFont);
	//text("you", 71,87);
	fill(255,255,0);
	textFont(Melissa);
	//text("s", 471,120);
	fill(0,255,255);
	stroke(255,0,0);
	textFont(Ballpointprint);
	//text("?", 17,184);
	//text("Bob,", 154,29);
	stroke(0,0,0);
	textFont(Diggity);
	//text("secrets,", 15,282);
	fill(255,192,203);
	textFont(RonsFont);
	//text("Forever", 12,340);
	//text("more", 204,249);
	stroke(0,255,0);
	//text("I", 276,249);
	stroke(255,0,255);
	textFont(Melissa);
	text("can", 392,87);
	text("you", 365,149);
	text("delay", 432,120);
	text("for", 317,184);
	text("safe", 398,219);
	text("I", 377,87);
	text("guard", 140,149);
	text("go", 242,184);



}
