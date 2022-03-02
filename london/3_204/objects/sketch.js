//declare variables
var groundPos_y;

//variables for the tree
var treePos_x;
var treeTrunkHeight;
var treeTrunkWidth;
var treeRadius;


function setup() 
{
    createCanvas(512,512);
    
    //initialise variables
    treePos_x = 256;
    treeTrunkHeight = 100;
    treeRadius = 120;
    treeTrunkWidth = 40;
    
    groundPos_y = 400;
    
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
    //trunk
    fill(180,80,0);
    ellipse(
        treePos_x,
        groundPos_y - treeTrunkHeight/2 + 10,
        treeTrunkWidth,
        treeTrunkHeight);
    //leaves
    fill(0,150,0);
    ellipse(
        treePos_x,
        groundPos_y - treeTrunkHeight,
        treeRadius,
        treeRadius);
    
    //cloud
    noStroke();
    fill(255);
    ellipse(100,50,50,50);
    ellipse(130,50,30,30);
    ellipse(150,50,20,20);
    
    //ground
    fill(200,130,0);
    rect(0,groundPos_y,width,112);
    

}


