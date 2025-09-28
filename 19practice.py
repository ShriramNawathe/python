b=0
for i in range(1,51):
    if i%2==0:
        b=b+i
    # print(b)
print("Eve:",b)

K=0
for i in range(1,51):
    if i%2!=0:
      K=K+i
print("Odd:",K)

##########################
h=0
for i in range(0,51,2):
    h=h+i
print("short hand Sum:",h)


###################

for i in range(1,21):
    k=i**2
    print(i,"**2=",k)

# square of 1st 20no
#################
# sum of 10odd no.
# sum=0
# for i in range(1,20):
#     if i%2!=0:
#         print(i)
#         sum+=i
# print(sum)


sum=0
i=0
while i<=20:
    if i%2!=0:
        sum=sum+i
    i=i+1
print(sum)

#############
# no divisible by 8  and 12

for i in range(1,100):
    if i%8==0 and i%12==0:
        print(i)



# while true billing name amt quan total


while True:
    print("Welcome to Instamart")
    name=input("Enter your name: ")
    total=0

    while True:
        print("Select product and enter amount and no. of quantity")
        amt=float(input("Enter the amount of specific produt: "))
        qnt=float(input("Enter the quantity of specific prod: "))
        total=total+(amt*qnt)

        repeat=input("Do you want more product? (yes/no): ")
        if repeat=="no" or repeat=="No":
            break
    print("-"*50)
    print("Name: ",name)
    print("Total of your product: ",total)
    print("-"*50)

    rep1=input("Do you wise to go for next person? (yes/no): ")
    if rep1=="no" or rep1=="No":
        break