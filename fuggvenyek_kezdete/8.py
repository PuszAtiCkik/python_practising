def factorial(num):
    eredemeny = 1
    for x in range(1,num + 1):
        eredemeny *= x
    
    return eredemeny
print(factorial(5))