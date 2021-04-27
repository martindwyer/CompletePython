def solve(arr_one, arr_two):
    the_list = arr_one
    for n in arr_two:
        the_list.append(n)
    the_list.sort()
    return the_list


print(solve([1,2,3,4],[-3,-2,-1]))

