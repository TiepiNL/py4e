# -problem3_6.py *- coding: utf-8 -*-

import sys

infilename = sys.argv[1]
outfilename = sys.argv[2]

infile = open(infilename)
outfile = open(outfilename,'w')
    
for line in infile:
    outfile.write("{}\n".format(len(line.strip("\n"))))

infile.close()
outfile.close()