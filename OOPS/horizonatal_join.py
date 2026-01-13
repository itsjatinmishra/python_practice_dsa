# lst = [
#     ["John", "Smith"],
#     ["Marie", "Keys"]
# ]

# final_list = []
# for i in range(len(lst)):
#     new_full_name = ""
#     for j in range(len(lst)):
#         new_full_name += lst[j][i] + " "
#     final_list.append(new_full_name)

# for i in final_list:
#     print(i)    

names = ("Jatin", "Other")
work = ("CEO", "Employee")

zipped = zip(names, work)

print(type(zipped))

for (a,b) in zipped:
    print(a,b)