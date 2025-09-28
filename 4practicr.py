#swap two variab;es

a=12
b=23

temp=a
print ("temp:",temp)

# a swap done
a=b
print("a:",a)
b= temp
print("b:",b)
 #print("value of a after conversion is :",a)
 #print("value of a after swapis :",b)

print ("or method")

k=23
n=32

k , n=n , k
print("k:",k)
print("n:",n)

#########################################
#float to int

a=12.33
b=int(a)
print("convert into int:",b)

##########
#take inputs

n2=input("n:")
age=int(input("age:"))
email=input("e:")
ph_no=int(input("ph_no:"))

print("Student id Info")
print("Name:",n2)
print("age:",age)
print("email:",email)
print("ph_no:",ph_no)
######################

#take input as int and convert to float

zz=int(input("zz:"))
print(type(zz))

xx=float(zz)
print("input after convertion to float:",xx)
print(type(xx))