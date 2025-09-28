# # sum of no. up to 50
# sum=0
# for i in range(1,51):
#     if(i%2!=0):
#         sum=sum+i
# print(sum)

# square of 1st 20num

# n=1
# while n<=20:
#     k=n**2
#     print(n,k)
#     n+=1

#
# for i in range(1,21):
#     k=i**2
#     print(k)

# sum of 1st 10odd num
# sum=0
# n=1
# while n<=20:
#     if n%2!=0:
#         sum=sum+n
#     n+=1
#
# print(n,sum)

# sum=0
# for i in range(1,21):
#     if i%2==0:
#         sum+=i
# print("Even:",sum)


#    if i%2!=0:
#         sum+=i
# print("Odd:",sum)


while True:
    print("Welcome to instamart")
    Name=input("whats your name:")
    Total=0

    while True:
        print("Give selected product amt and quntity")
        amt=int(input("amt:"))
        quantity=int(input("quantity:"))
        total=amt*quantity

        rep=input("do you want more product ?(yes/no): ")
        if rep=="no" or rep=="No":
            break
    print("-"*50)
    print("Nmae:",Name)
    print("Total:",total)
    print("-"*50)

    rep1=input("Did you finish and want buy again?(yes/no): ")
    if rep1=="no" or rep1=="No":

        print("Visit again")
        break


