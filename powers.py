def powers(base=int(input("Enter the base:")),exp=(int(input("Enter the exponential:")))):

    if (exp==1):

        return(base)

    if(exp!=1):

        return(base*powers(base,exp-1))

print("Result:",powers())
