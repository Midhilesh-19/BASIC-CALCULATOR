def add (x,y):
    return x+y

def subs (x,y):
    return x-y

def multiply (x,y):
    return x*y

def divide (x,y):
    return x/y

def power (x,y):
    return pow(x,y)


print("select operation")
print("1.add")
print("2.subs")
print("3.multiply")
print("4.divide")
print("5.power")

choice = input("Enter choice(1/2/3/4/5):")

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=",subs(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=",multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=",divide(num1,num2))

elif choice == '5':
    print(num1,"^",num2,"=",power(num1,num2))

else:
    print("Invalid input") 