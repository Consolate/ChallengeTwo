def recursion(numbers):
    sum = 0

    for i in numbers:
            if (y(i)== y([])):

                    sum= sum + recursion(i)
                    
            else: 
                    sum = sum + i
                    return sum

print(sum([1,2,3,4,3,5,8,5,6,7]))