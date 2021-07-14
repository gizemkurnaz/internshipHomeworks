#1
sum = 0
for i in range(1000):
  if (i%3 == 0) | (i%5 == 0):
          sum = sum + i
print(sum)


#2
firstNum, secondNum = 0, 1
total = 0
while True:
    firstNum, secondNum = secondNum, firstNum + secondNum
    if secondNum >= 4000000:
        break
    if secondNum % 2 == 0:
        total += secondNum
print(total)

#3
import math
number = 60
for i in range(int(math.sqrt(number)),1,-1):
    print(i)
    if (number % i ==0):
        is_prime = False
        for x in range(int(math.sqrt(i)),1,-1):
            if(i % x ==0):
               is_prime = True
        if(is_prime!=True):
            print(i)
            break


