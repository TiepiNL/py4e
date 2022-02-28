

function setup() 
{
    //setup the canvas
    createCanvas(512,512);
    
}

function draw()
{
    
    //Draw the various shapes
    background(255);
    
    rect(50,50,100,100);

    ellipse(250,100,100,100);
    
    //overlapping shapes
    ellipse(100,250,100,100);
    rect(50,200,75,75);
    
    ellipse(250,250,100,100);
    rect(225,225,75,75);
    
}


