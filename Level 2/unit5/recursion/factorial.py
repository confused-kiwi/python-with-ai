def factorial(num):
    num = int(num)
    if num == 0 or num == 1:
        print(f"{num} = ", end="")
        return 1
    
    else:
        print(f"{num}*", end="")
        return num * factorial(num-1)

print(factorial(10))