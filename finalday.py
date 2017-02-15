'''firstlist=[1,2,3,4,5,6]
#print(firstlist[2])
firstlist.append(3)

for a in firstlist:
    print(a)
print(firstlist)
#print(firstlist.count(3))
#print(firstlist.index(3))
#print(firstlist.pop())
#firstlist.reverse()
firstlist.sort()
print(firstlist)

firsttuple=(1,2,3,4,5,6)
for a in firsttuple:
    print (a)

myTuple = (1,2,3)
print(myTuple)
myList = list(myTuple)
myList.append(4)
print(myList)

VaildInput=False
while (VaildInput==False):
    try:
        a=int(input("Enter in a number between 1-10"))
        squared=a*a
        print(a, "squared is",squared)
        VaildInput = True
    except:
        print("Invalid Input, ", end="")

file= open("test.txt", "r") #opens file with name of "test.txt"
myList = []
for line in file:
    myList.append(line)
print(myList)
b=len(myList)
for a in range (0,b):
    print (myList[a])

q="I like pie"
print(len(q))

writefile = open("test2.txt", "w") #writes a file with name of "test2.txt"
writefile.write("I like apple pie")
writefile.write("I can write to a file.\n")
writefile.write("It is sweet!")
writefile.close()'''

appendfile = open("test2.txt", "a") #appends to file "test2.txt"
appendfile.write("I forget the flowers!")
appendfile.close()
