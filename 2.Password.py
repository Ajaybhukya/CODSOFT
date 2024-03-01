no1=int(input("Enter the first number:"))
no2=int(input("Enter the second number:"))
print("MENU")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("Read  your choice:"))
if choice==1:
    print("Addition of two numbers:",no1+no2)
elif choice==2:
    print("Substraction of two numbers:",no1-no2)
elif choice==3:
    print("Multipilication of two numbers:",no1*no2)
elif choice==4:
    print("Division of two numbers:",no1/no2)
else:
    print("Invalid choice")