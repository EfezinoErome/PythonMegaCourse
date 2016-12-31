import glob2
import datetime
'''
#John Attempt - which is correct
file1 = "file1.txt"
file2 = "file2.txt"
file3 = "file3.txt"
file4 = "filemerge.txt"

file = open(file1,'r')
content = []
content.append(file.read())
file = open(file2,'r')
content.append(file.read())
file = open(file3, 'r')
content.append(file.read())

file = open(file4,'w')
for i in content:
    file.write(str(i)+"\n")
file.close()
'''

#Program attempt
filenames = glob2.glob("*.txt")

with open(datetime.datetime.now().strftime("%Y-%m-%d"  \
+ ".txt"), 'w') as file:
    for filename in filenames:
        with open(filename, 'r') as f:
            file.write(f.read() + "\n")
