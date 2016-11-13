# The program builds a list of words for selected text in “Romeo and Juliet”.

#You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

# Method 1

fn = raw_input("Enter name of file:")
fh = open('romeo.txt')
lst = list()

# For each line, split the line into a list of words using the split() method.
for line in fh:
    line = line.strip().split()
    for w in line :
       lst.append(w)

#sort out of loop
lst2 = sorted(lst)
#print lst2

# For each word on each line check to see if the word is already in the list and if not append it to the list.
l3=[]
for i in lst2 :
   if i not in l3:
      l3.append(i)

print l3