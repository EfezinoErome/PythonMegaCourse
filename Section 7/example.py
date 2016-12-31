"""
This script creates an empty file.
"""
import datetime
import time

filename = "sample1.txt"
filename = datetime.datetime.now().strftime("%Y-%m-%d"+".txt")

#create empty file

def create_file():
    """This function creates an empty file"""
    with open(filename, "w") as file:
        file.write("")
create_file()

lst = []
for i in range(5):
    lst.append(datetime.datetime.now())
    time.sleep(2)

for i in lst:
    print(i)
