print("mirrored rightangle trianglr pattern")
n=int(input("Enter the number of rows :"))
for i in range(n):
    for j in range(i+1):
        print("* ",end="")
    print()
for i in range(n):
    for j in range(i-1):
        print("* ",end="")
    print()