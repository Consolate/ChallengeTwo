def powers(base,exp):

    if (exp==1):

        return(base)

    if(exp!=1):

        return(base*powers(base,exp-1))

        base=eval(int(input("Enter the base:")))

        exp=eval(int(input("Enter the exponential:")))

        print("Result:",powers(base,exp))