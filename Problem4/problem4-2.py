def factorial(num, total=1):
    if num == 1 :
        return total
    else :
        return factorial(num-1, num * total)
    
result = factorial(4,1)
print(result)
