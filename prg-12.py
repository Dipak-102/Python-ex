# program to calculate the series of sum // 1.17

n=int(input("Enter the Term: "))
b=0
sum=0
for i in range(1,n+1):
        b=(b*10)+n-3
        sum+=b
        print(b,end=" ")
print()
        
print("sum is: ",sum)    
