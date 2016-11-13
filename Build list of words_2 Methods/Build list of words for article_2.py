# The program builds a list of words for selected text in “Romeo and Juliet”.

#You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

# Method 2

fname = raw_input("Enter file name: ")
fh = open(fname)
lst=list()

#sort here
for line in fh:
    line=line.strip().split()
    for words in line:
        lst.append(words)
        lst.sort()

l2=[]
for i in lst:
    if i not in l2:
	l2.append(i)

print l2