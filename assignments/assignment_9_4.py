# 9.4 Write a program to read through the mbox-short.txt and figure out who has
# sent the greatest number of mail messages. The program looks for 'From ' lines
# and takes the second word of those lines as the person who sent the mail. The
# program creates a Python dictionary that maps the sender's mail address to a
# count of the number of times they appear in the file. After the dictionary is
# produced, the program reads through the dictionary using a maximum loop to
# find the most prolific committer.

# Desired output:
# cwen@iupui.edu 5

fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"

fhandler = open(fname)
senders = dict()
for line in fhandler:
    if not line.startswith("From "):
        continue
    pieces = line.split()
    sender = pieces[1]
    senders[sender] = senders.get(sender, 0) + 1

bigcount = None
bigword = None
for word,count in senders.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword,bigcount)
