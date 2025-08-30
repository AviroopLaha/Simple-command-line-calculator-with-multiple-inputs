def calculator():
    expression=input("enter your exxpression")
    try:
        result=eval(expression)
        print("results:",result)
    except ZeroDivisionError:
        print("invalid input")
    except:
        print("wrong expression")
while True:
    calculator()
    choise=input("do you want to continue yes/no??")
    if choise!="yes":
            print("bye")
            break
