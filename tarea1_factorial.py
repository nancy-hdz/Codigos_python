def factorial(n):
    if n<0:
        print("no es posible calcular el factorial")
    elif (n ==1 or n ==0) :
        return 1
    else:
        return factorial(n-1)*n
print(factorial(6))

