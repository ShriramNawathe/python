for i in range(1, 4):
        for j in range(1, 6):
            if j >= 4 - i and j <= 2 + i:
                print(j, end=" ")
            else:
                print(" ", end=" ")
        print()
for i in range(1, 3):
        for j in range(1, 6):
            if j >= i+1 and j <= 5 - i:
                 print(j, end=" ")
            else:
                print(" ", end=" ")
        print()