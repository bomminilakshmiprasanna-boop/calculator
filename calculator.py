def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiple(a,b):
    return a*b
def divide(a,b):
    if b == 0 :
        return "cannot divide by zero"
while True:
    print("calculator")
    print("1.addition")
    print("2.subtraction")
    print("3.multiple")
    print("4.divide")
    print("5.exit")
    choice = input("enter your choice (1-5:)")
    if choice == 5:
        print("thank you for using the maniteched calculator")
        break
    if choice in ["1","2","3","4"]:
        try :
            n1=float(input('enter first number:'))
            n2=float(input('enter second number:'))
            if choice == "1":
                print("result=",add(n1,n2))
            elif choice == "2":
                print("result=",substract(n1,n2))
            elif choice == "3":
                print("result=",multiple(n1,n2))
            elif choice == "4":
                print("result=",divide(n1,n2))
        except ValueError:
                print("please enter a valid numbers!")
    else :
        print("invalid choice please try again")