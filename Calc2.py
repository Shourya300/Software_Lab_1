import Addition
import Subtraction
import Division
import Multiplication

print("Select Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Mulitiplication")

while True:
    choice = input("Enter your choice")
    if choice in ('1','2','3','4'):
        try:
            num1=float(input("Enter first number"))
            num2=float(input("Enter second number"))
        except ValueError:
            print("Invalid input")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", Addition.Addition(num1,num2) )
        elif choice == '2':
            print(num1, "-", num2, "=", Subtraction.Subtraction(num1,num2) )
        elif choice == '3':
            print(num1, "/", num2, "=", Division.Division(num1,num2) )
        elif choice == '4':
            print(num1, "*", num2, "=", Mulitiplication.Mulitiplication(num1,num2) )
        next = input("Another Round yes/no?")
        if next=="no":
            break
        