# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()
# print('matrix')
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

######################
# Python program to print the pattern using 'a'
#
# # Top half (rows 1 to 4)
for i in range(1, 5):
    for j in range(1, 5):
        if j <= i:
            print("a", end=" ")
        else:
            print(" ", end=" ")
    print()
# Bottom half (rows 5 to 7)
for i in range(1, 4):
    for j in range(1, 5):
        if j <= 4 - i:
            print("a", end=" ")
        else:
            print(" ", end=" ")
    print()
#
#or
# for i in range (1,8):
#     for j in range (1,5):
#         if i<=4 and j<=i:
#             print("A",end=" ")
#         elif i>=5 and j<=8-i:
#             print("A",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# a
# a a
# a a a
# a a a a
# a a a
# a a
# a
#############################################################
# for i in range(1,6):
#     for j in range(1,6):
#         if i<=3 and j>=4-i and j<=2+i:
#             print(j,end=" ")
#         elif i>=4 and j>=i-2 and j<=8-i:
#             print(j, end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# or

# for i in range(1, 4):
#         for j in range(1, 6):
#             if j >= 4 - i and j <= 2 + i:
#                 print(j, end=" ")
#             else:
#                 print(" ", end=" ")
#         print()
# for i in range(1, 3):
#         for j in range(1, 6):
#             if j >= i+1 and j <= 5 - i:
#                  print(j, end=" ")
#             else:
#                 print(" ", end=" ")
#         print()

#     3
#   2 3 4
# 1 2 3 4 5
#   2 3 4
#     3
##########################################################