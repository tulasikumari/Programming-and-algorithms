#  program to print a specified list after removing the 4th elements.
list=[1,4,5,7,9,44,66]
for i in list:
    if i==list[4]:
        continue
    print(i,end=" ")