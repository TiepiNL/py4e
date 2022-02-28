/*
201 - The case of Judge Hopper:
Stage 1 - Department of Justice

Officer: 2628175
CaseNum: 201-0-17604801-2628175

Judge Hopper has gone missing and we’ve been booked to investigate. This is the big time kid. Now I need you to head over to Hopper’s office at the Department of Justice and gather clues.

Draw a separate ellipse around 4 pieces of evidence:
Letter opener,
Death threat letters,
telephone,
and the AGOL leaflet

Each ellipse should cover the entire object whilst keeping as close to the edges as possible. You will need to use different values for the width and height arguments.


*/

var img;

function preload()
{
    img = loadImage('scene.png');
}

function setup()
{
    createCanvas(img.width,img.height);
}

function draw()
{

    image(img,0,0);
    stroke(255, 0, 0);
    strokeWeight(3);
    noFill();

    // write the code to draw around the evidence below
    //ellipse(x, y, w, [h])
    //x Number: x-coordinate of the center of ellipse.
    //y Number: y-coordinate of the center of ellipse.
    //w Number: width of the ellipse.
    //h Number: height of the ellipse. (Optional)
    

    // Letter opener
    ellipse(570, 241, 50, 135);

    // Death threat letters
    ellipse(252, 231, 120, 120);

    // Telephone
    ellipse(569, 359, 200, 120);

    // AGOL leaflet
    ellipse(419, 297, 105, 125);

}
