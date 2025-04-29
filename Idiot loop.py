#Example 1
n = 1

while n < 5:
    print("Hello Elijah")
    n = n+1
    
#Example 2
    n = 1

while n < 5:
    print("Hello Elijah")
    n = n+1
    if n == 3:
        break
    
#Example 3
n = 1

while n < 5:
    if n == 2:
        n = n+1
        continue
    print("Hello Elijah")
    n = n+1

#Example 4
z = 0

while z < 3:
    if z == 0:
        print("z is",z)
        z += 1
    elif z == 1:
        print("z is",z)
        z += 1
    else:
        print("z is",z)
        z += 1

#Example 5
myList = []
i = 0

while len(myList) < 4 :
    myList.append(i)
    i += 1
  
print(myList)

#Example 6
n = 10

while n <= 100:
    print(n ,end = ",")
    n = n+10

#Example 7
    myTuple = (10,20,30,40,50,60)
i = 0

while i < len(myTuple):
    print(myTuple[i])
    i += 1

#Example 8
    myList = [23,45,12,10,25]
i = 0 
sum = 0

while i < len(myList):
    sum += myList[i]
    i += 1

print(sum)

#Example 9
fruitsList = ["Mango","Apple","Orange","Guava"]

while fruitsList:
    print(fruitsList.pop())

print(fruitsList)

#example 10
i = 0 
word = "Hello"

#print all letters except e and o

while i < len(word):
    if word[i] == "e" or word[i] =="o":
        i += 1
        continue

    print("Returned letter",word[i])
    i += 1

#Example 11
    n = int(input("Enter a number: "))

while n != 0:
    n = int(input("Enter zero to quit: "))

#Example 12
    num = int(input("Enter a number: "))
b = 0
p = 1
n = num

while n>0:
    rem = n%2
    b += rem * p
    p = p*10
    n = n//2

print("Binary value: ",b)

#Example 13
p = 5
sum = 0
count = 0

while p > 0:
    count += 1
    f = int(input("Enter the number "))
    sum += f
    p -= 1
  
average = sum/count
print("Average of given Numbers:",average)

#Example 14
n = 1

while n <= 5:
    squareNum = n**2
    print(n,squareNum)
    n += 1