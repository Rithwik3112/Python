'''import time as ti
times = ti.strftime("%H:%M:%S")
print(times)
timestamp= int(ti.strftime("%H"))
if timestamp < 12:
    print("good morning ")
else:
    print("good evening ")
x=int(input("enter a number (X):- "))

match x :
    case 0:
        print("x is zero ")
    case 1:
        print("x is 1 ")
    case 2:
        print("x is 2")

    case _ if x < 0:
        print("its negitive number ")
    case _ :
        print(" x is gretaer than 2" )

for i in range(12):
    if (i == 9):

        continue
    print(i)
'''
# do while loop
i=0
while True:
    print(i)
    i=i+1
    if(i%100 ==0):
       print(i)
       break
