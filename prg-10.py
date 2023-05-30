# print the reverse of given integer // 1.14

n=int(input("Enter Value: "))
rev=0
r=0

while n!=0:
    r=n%10
    rev=rev*10+r
    n//=10
print(rev)
