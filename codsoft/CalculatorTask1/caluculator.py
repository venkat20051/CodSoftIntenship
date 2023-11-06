rem="yes"
while(True):
        if(rem=="yes"):
            num1=int(input("enter first value :"))
            num2=int(input("enter second value : "))
            print("1 or + for Addition")
            print("2 or - for subraction")
            print("3 or * for multiplication")
            print("4 or / for division")
            print("5 or % for mod")
            print("6 or ** for power")
            s=input("enter the operator")
            if(s=='1' or s=="+"):
                add=num1+num2
                print(add)
            elif(s=='2'or s=='-'):
                sub=num1-num2
                print(sub)
            elif(s=='3' or s=="*"):
                mul=num1*num2
                print(mul)
            elif(s=='4' or s=='/'):
                div=num1/num2
                print(div)
            elif(s=='5' or s=='%'):
                mod=num1%num2
                print(mod)
            elif(s=='6' or s=='**'):
                pow=num1**num2
                print(pow)
        else:
             print("Exiting...")
             break
        print("if you want to continue your caluculation enter yes or no")
        rem=input()
