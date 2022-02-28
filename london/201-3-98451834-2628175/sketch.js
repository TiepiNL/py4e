/*
201 - The case of Judge Hopper
Stage 4 - The warehouse

Officer: 2628175
CaseNum: 201-3-98451834-2628175

As you enter the ALGOL warehouse you are struck by the most horrendous stench - it’s not the fish. Lying amongst piles of fish carcasses you find the body of Judge Hopper. Gathering yourself together, you tie a handkerchief around your nose and mouth and quickly set about recording the evidence.

Draw around the Judge’s body ...


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

    // write the code to draw around the Judge's body below
    beginShape();
    vertex(270, 335);
    vertex(269, 323);
    vertex(281, 308);
    vertex(322, 274);
    vertex(345, 278);
    vertex(368, 296);
    vertex(394, 260);
    vertex(413, 207);
    vertex(422, 154);
    vertex(436, 123);
    vertex(461, 125);
    vertex(468, 114);
    vertex(467, 105);
    vertex(477, 95);
    vertex(479, 83);
    vertex(487, 71);
    vertex(516, 62);
    vertex(522, 69);
    vertex(499, 111);
    vertex(493, 131);
    vertex(503, 135);
    vertex(513, 119);
    vertex(513, 107);
    vertex(526, 86);
    vertex(539, 93);
    vertex(577, 83);
    vertex(584, 91);
    vertex(566, 110);
    vertex(548, 117);
    vertex(535, 125);
    vertex(532, 134);
    vertex(571, 128);
    vertex(572, 146);
    vertex(521, 251);
    vertex(509, 278);
    vertex(484, 308);
    vertex(481, 321);
    vertex(467, 335);
    vertex(459, 366);
    vertex(533, 390);
    vertex(581, 413);
    vertex(598, 433);
    vertex(603, 450);
    vertex(590, 459);
    vertex(580, 456);
    vertex(563, 432);
    vertex(514, 416);
    vertex(481, 409);
    vertex(476, 421);
    vertex(436, 443);
    vertex(381, 429);
    vertex(359, 409);
    vertex(339, 358);
    vertex(349, 347);
    vertex(343, 322);
    vertex(324, 299);
    vertex(296, 318);
    vertex(293, 336);
    vertex(275, 338);
    vertex(270, 335);
    endShape();

}
