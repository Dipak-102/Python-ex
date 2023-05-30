# print the list of the only even number // 1.15

lst1=[10, 20, 30, 40, 50, 70, 60, 90, 80, 100]
lst2=[]
a=0

for i in lst1:
    if a % 2 == 0:
        print(i,end=" ")
    a+=1
