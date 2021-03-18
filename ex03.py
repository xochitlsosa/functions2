def multiply(numbers):  
    total = 1
    for a in numbers:
        total *= a  
    return total  
print(multiply((6, 5, 7, 9, -2)))