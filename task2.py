#Elephant simulation
#Nathan Wagstaff assn 8
#cs1400
import random
#definitions of the variables
count = 0
threeMatch = 0
zooKeeperMatch = 0
number = 100000

#simulation loop
while count != number:
    elephantOne = random.randint(1, 6)
    elephantTwo = random.randint(1, 6)
    zooKeeper = random.randint(1,6)
    count = count + 1
    #If the zookeeper sees one of the Elephant
    if elephantOne == zooKeeper or elephantTwo == zooKeeper:
        zooKeeperMatch = zooKeeperMatch + 1
    #If the zookeerer sees both of the Elephants
    if elephantOne == elephantTwo == zooKeeper:
        threeMatch = threeMatch + 1
    #breaking the loop after 100000
    if count == number:
        break

#calculate the percentages
singlePercentage = (zooKeeperMatch / number) * 100
bothPercentage = (threeMatch / number) * 100


print("The zookeeper sees both Elephants ", format(bothPercentage, "2.2f"), "% of the time.")
print("The zookeeper sees one of the Elephants ", format(singlePercentage, "2.2f"), "% of the time.")
if singlePercentage == range(31, 35) and bothPercentage == range(14, 18):
    print("The Zookeeper was correct")
else:
    print("The Custodian is correct")


