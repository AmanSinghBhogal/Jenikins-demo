# This is version 2 for the app
print"\nHello World \n")

for c in range(2):
    for i in range(5):
        for j in range(5):
            if((j==0 or j==4) or (i==0 or i==4)):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()