data = "jaaatinnn"
list2 = {}

count = 0
for i in range(len(data)):
    list2.update({data[i]: count})

for i in data:
    if(i in list2):
        list2[i] += 1

print(list2)
