import matplotlib.pyplot as plt

a = int(input("Enter upper bound: "))
distributionDic = {}
for i in range(a):
    distributionDic[i + 1] = 0

for number in distributionDic:
    print(number)
    start = 1

    while (start < number):
        if number % start == 0 and start != number:
            distributionDic[start] +=1
        start +=1

for key in range(a):
    key = key + 1
    if distributionDic[key] == 0:
        distributionDic.pop(key)
plt.bar(distributionDic.keys(), distributionDic.values())
plt.show()