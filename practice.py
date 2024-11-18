#cube-calculator

a = float(input("Enter Your Number:"))
cube=a*a*a
print ("The Cube ",cube)

#ends-here


# Calculator code

num1=float(input("Enter Your First Number:"))

num2=float(input("Enter Your Second Number:"))

print("Select The Action You Want To Perform :-")
print("Addiction - press 1")
print("Subtraction - press 2")
print("Division - press 3")
print("Multiplication - press 4")

opert= int(input("Enter Your Operation No:"))

if opert==1:
    add=num1+num2
    print ("Addition :",add)

elif opert==2:
    sub=num1-num2
    print("Subtraction :",sub)

elif opert==3:
    did=num1/num2
    print("Division :",did)

elif opert==4:
    mul=num1*num2
    print("Multiplication :",mul)   

else:
    print("Invalid Number , Can't Perform Any Opration :)")

