
numlarge = int(input("Enter the largest number: "))
numsmall = int(input("Enter the smallest number: "))
while numlarge % numsmall != 0:
    numlarge += 1
print("LCM IS:", numlarge)
