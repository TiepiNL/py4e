

function setup() 
{
    createCanvas(512,512);
    
}

function draw()
{
    background(150,150,255);
    
    //sun
    noStroke();
    fill(255,150,0);
    ellipse(430,150,100,100);
    
    //tree
    stroke(0);
    fill(180,80,0);
    ellipse(256,360,40,100);
    fill(0,150,0);
    ellipse(256,300,120,120);
    
    //cloud
    noStroke();
    fill(255);
    ellipse(100,50,50,50);
    ellipse(130,50,30,30);
    ellipse(150,50,20,20);
    
    //ground
    fill(200,130,0);
    rect(0,400,width,112);
    

}


