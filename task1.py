#Fluky Numbers
#Nathan Wagstaff
#Assn 8 cs1400
import random
import time

startTime = time.time()
numLoops = 0
fluky = 0

for j in range(1, 10000 + 1):
    num = j
    sum1 = 0
    if fluky == 7:
        break
#each factor of the number, not including itself.
    for i in range(1, num):
        numLoops += 1
    #determine if i is a factor of num
        if num % i == 0:
        #means i is a factor
            random.seed(i)
            randNum = random.randint(1, num)
            sum1 += randNum

    if num == sum1:
    #means we found a fluky
        print("Fluky Number: ", num)
        fluky = fluky + 1


endTime = time.time()
totalTime = endTime - startTime
print("Total Time:   ", format(totalTime, "2.2f"))
print("Total Loops:  ", numLoops)