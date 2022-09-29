# Write a function that takes a list of numbers and returns the largest number in the list.

lst = [23,44,33]

def max(lst):
    max_num = lst[0]
    if len(lst) == 1:
        return lst[0]
    else:
        for num in lst:
            if num > max_num:
                max_num = num
                
    return max_num

print(max(lst))