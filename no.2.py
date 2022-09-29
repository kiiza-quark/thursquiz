

# The snail climbs up 7 feet each day and slips back 2 feet each night. 
# How many days will it take the snail to get out of a well with the given depth?. 
# Using python, write a function to solve this problem. Sample Input: 31 Sample Output: 6

def days(depth):
    count = 0
    n = 0
    while count <= depth:
        count += 5
        n += 1
        
    return n

print(days(31))
        