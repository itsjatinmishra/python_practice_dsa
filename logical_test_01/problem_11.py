values = [60,100,120]

weight = [10,20,30]

capacity = 50

newValues = set()
newWeight = set()

for i in range(len(values)):
    for j in range(len(values)):
        if(i == j):
            continue
        else:
            newValues.add(values[i] + values[j])
            newWeight.add(weight[i] +  weight[j])

# print(newValues, newWeight)

newVal = list(newValues)
newWei = list(newWeight)

maxWeight = 0

for i in range(len(newWei)):
    if newWei[i] <= capacity:
        if (newVal[i] > maxWeight):
            maxWeight = newVal[i]

print(maxWeight)