/*
201 - The case of Judge Hopper
Stage 3 - The dressing room

Officer: 2628175
CaseNum: 201-2-87998661-2628175

No sooner do you enter the lobby of the Cobol Theatre than the sound of gunshots leads you running towards the backstage area. You head towards a swinging door, the star dressing room. Sure enough you find a series of bullet holes peppered across the mirror. You are about to turn round and resume your chase when you notice a familiar pattern in the holes. Frantically you grab some lipstick from the dresser and draw on the mirror.

Use the vertex function to complete the pattern.


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

    // write the code to join the bullet holes below
    //vertex(x, y)
    //x Number: x-coordinate of the vertex
    //y Number: y-coordinate of the vertex


    beginShape();
    vertex(340, 178);
    vertex(275, 111);
    vertex(363, 91);
    vertex(508, 156);
    vertex(490, 211);
    vertex(439, 162);
    endShape();

}
