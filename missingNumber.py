def missing_number(original_list=[1,2,3,4,6,7,10], num_list=[10,11,12,14,17]):
    original_list = [x for x in range(num_list[0], num_list[-1] + 1)]
    num_list = set(num_list)
    return (list(num_list ^ set(original_list)))
    print(missing_number([1,2,3,4,6,7,10]))
print(missing_number([10,11,12,14,17]))   
        