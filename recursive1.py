def sumdown(n):
    if n == 0:
        return 0
    return n + sumdown(n-1)

inum = int(input("enter a number"))
print(f"sum of {inum} down to 1 is : {sumdown(inum)}")

