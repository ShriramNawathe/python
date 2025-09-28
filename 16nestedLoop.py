# for i in range (1,4):
#     for j in range (1,11):
#
#         # print("Set",i,"rep",j)
#         # or
#          print(j,end=" ")
#
#     print()

# row clmn
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# row
a=int(input("A:"))
for i in range(1,a):
    # print("i","=",i)
    for j in range(1,i+1):

        print(j,end=" ")
    print()
