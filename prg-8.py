# w.a.p to display prime numbers in range // 1.11

lower=int(input("Enter the Range: "))
upper=int(input("Enter the Range: "))
print("Prime number between",lower,"And",upper,"Are: ")
for i in range(lower,upper+1):
    if i > 1:
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            print(i)

        

