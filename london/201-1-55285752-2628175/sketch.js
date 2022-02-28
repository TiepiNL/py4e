/*
201 - The case of Judge Hopper
Stage 2 - Hopper’s House

Officer: 2628175
CaseNum: 201-1-55285752-2628175

On entering the house you’re immediately confronted by a trail of blood spatters leading up to the master bedroom. It’s clear that Judge Hopper was abducted from here. What’s more, the clues splayed across the bed sheets indicate a private life a little more exciting than a district judge would admit in public. Somehow these clues connect, you just need to join them together.

Use the triangle function to join the blood spatters on the clues and make the connection.

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

    // write the code to connect the blood splatter below
    //triangle(x1, y1, x2, y2, x3, y3)
    //x1 Number: x-coordinate of the first point
    //y1 Number: y-coordinate of the first point
    //x2 Number: x-coordinate of the second point
    //y2 Number: y-coordinate of the second point
    //x3 Number: x-coordinate of the third point
    //y3 Number: y-coordinate of the third point
    triangle(144, 372, 983, 329, 850, 506);

}
