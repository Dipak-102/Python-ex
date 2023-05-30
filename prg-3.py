# write a program to print multiplication table of given number
# 1.4


n=int(input("Enter Number: "))
no=n
for i in range(11):
    no=n * i
    if no == 0:
        print()
    else:
        print(no)
