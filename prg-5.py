# w.a.p to count total number of digits using while loop
# 1.6

n=int(input("Enter number: "))
count=0



while n!=0:
    n//=10
    count+=1

print(count)
