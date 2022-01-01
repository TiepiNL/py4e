# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line
# that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the
# line (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. Also look at the
# last line of the sample output to see how to print the count.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

# Desired output:
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
# zqian@umich.edu
# rjlowe@iupui.edu
# zqian@umich.edu
# rjlowe@iupui.edu
# cwen@iupui.edu
# cwen@iupui.edu
# gsilver@umich.edu
# gsilver@umich.edu
# zqian@umich.edu
# gsilver@umich.edu
# wagnermr@iupui.edu
# zqian@umich.edu
# antranig@caret.cam.ac.uk
# gopal.ramasammycook@gmail.com
# david.horwitz@uct.ac.za
# david.horwitz@uct.ac.za
# david.horwitz@uct.ac.za
# david.horwitz@uct.ac.za
# stephen.marquard@uct.ac.za
# louis@media.berkeley.edu
# louis@media.berkeley.edu
# ray@media.berkeley.edu
# cwen@iupui.edu
# cwen@iupui.edu
# cwen@iupui.edu
# There were 27 lines in the file with From as the first word

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fhandler = open(fname)
lst = list()
for line in fhandler:
    if not line.startswith("From "):
        continue
    pieces = line.split()
    lst.append(pieces[1])

print("\n".join(lst))
print("There were", len(lst), "lines in the file with From as the first word")
