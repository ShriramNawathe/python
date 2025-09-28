# #positive or neg num

num=int(input("Enter a number:"))

if num>=0:
    print("Positive: ",num)
else:
    print("neg: ",num)

#odd eve
num=int(input("Enter num: "))
if num%2==0:
    print("Even")
else:
    print("Odd")

# area
print("1 for square /n 2for rectangle /n 3for circle /n 4for triangle")
num=int(input("Enter num: "))

if num==1:
    sidde=float(input("Enter side: "))
    #side square
    area=sidde**2
    print("area =",area)
elif num==2:
    l=float(input("Enter length: "))
    h=float(input("Enter height: "))
    area=l*h
    print("area =",area)
elif num==3:
    r=float(input("Enter number: "))
    area=(3.14)*(r**2)
    print("area =",area)
elif num==4:
    b=int(input("Base: "))
    h=int(input("Height: "))
    area=0.5*b*h
    print("area =",area)
else:
    print("Invalid input")


##########
# 1D 2D 3d 4d
num=int(input("Enter num: "))

if num>=0 and num<9:
     print(num,"is 1D")
elif num>=10 and num<99:
    print(num,"is 2D")
elif num>=100 and num<999:
    print(num,"is 3D")
elif num>=1000 and num<9999:
    print(num,"is 4D")
else:
    print("invalid input")





 # vowels
let= input(" enter vowels: ")

# if let in "aeiou" or let in"AEIOU":
#     print("Entered letter: "+(let)+" are vowels")
#
#

if let == "a" or let == "e" or let == "i" or let == "o" or let == "u" or let == "A" or let == "E" or let == "I" or let == "O" or let == "U":
    print("Entered letter "+let+" are vowels")
else:
    print("Not Vowels")