# program to print the star pattern // 1.18

n= int(input("Enter rows: "))

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(0,i-1):
        print("*",end=" ")
    print()
