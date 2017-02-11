'''for a in range (1,5):
    print (a)
for b in (1,3,5):
    print (b)

def main():
    b = int(input("How many numbers in your set? "))
    sum = 0
    for q in range (0,b):
        z=int(input("Enter a number"))
        print("Number %d is %d" %(q+1,z))
        print("Number", q+1, "is", z)
        sum=sum+z
    print("The average of all the numbers is %f" %(sum/b))
    print ("The average of all the numbers is", (sum/b))

main()

def main():
    setnumberlineend = int(input("How many numbers in your set? "))
    averagesum=0
    for numberlinenumber in range (0,setnumberlineend):
        randomnumber=int(input("Enter a number"))
        print("Number", numberlinenumber+1, "is", randomnumber)
        print ("Current average sum number is", averagesum)
        averagesum=averagesum+randomnumber
        print ("New average sum number is", averagesum)
    print ("The average of all the number is", (averagesum/setnumberlineend))

main()

a=True
b = 0
while a == True:
    print (b)
    b=b+2
    if b <= 5:
        a = True
    else:
        a = False'''

for rangebytwos in range (0,10,3):
    print (rangebytwos)

a=input("Do you want to continue? Y or N")
while a == 'Y':
    print
