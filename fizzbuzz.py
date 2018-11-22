def fizzbuzz(mylist = n for n in input("Enter:"), yourList = n for n in input("Enter:")):
         
    totallength = len(myList) + len(yourList)

    if totallength % 3==0:

        return "fizz"

    elif totallength % 5==0:

        return "buzz"

    elif totallength % 3 == 0 and totallength % 5 == 0:
        return "fizzbuzz"
        
    else:
        return totallength
    
print(fizzbuzz())
