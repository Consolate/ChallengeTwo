def fizzbuzz(mylist,yourList):
    mylist = [int(n) for n in input("Enter:").split(",")]
    yourList = [int(n) for n in input("Enter:").split(",")] 

    myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,17, 18, 19, 20, 21]

    yourList = [22, 23, 24, 25, 26, 27, 28, 29, 30, 31,32, 33, 34, 35, 36, 37, 38, 39, 40]
         
    totallength = len(myList) + len(yourList)

    if totallength % 3==0:

        return "fizz"

    elif totallength % 5==0:

        return "buzz"

    elif totallength % 3 == 0 and totallength % 5 == 0:
        return "fizzbuzz"
        
    else:
        return totallength
    
        print(fizzbuzz(myList,yourList))