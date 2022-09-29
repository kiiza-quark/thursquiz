

# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program: Hello world! 
# Then, the output should be: UPPER CASE 1 LOWER CASE 9

import string
sent = "Hello world!"
def count_lower_upper(sentence):
    lowers = 0
    capitals = 0
    for letter in sentence:
        if letter in string.ascii_uppercase:
            capitals += 1
            
        elif letter in string.ascii_lowercase:
            lowers += 1
            
        else:
            continue
        
    return f"LOWER {lowers} CAPITALS {capitals}"
        
print(count_lower_upper(sent))