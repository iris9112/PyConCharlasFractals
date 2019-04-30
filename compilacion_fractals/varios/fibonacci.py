def fibonacci(n):
    #if n <= 1:
    #    return n
    # cada numero es la suma de los dos anteriores    
    total = fibonacci(n-1) + fibonacci(n-2)
    return total

#print('Ingresa un número')
#num1 = int(input()) 
#print('El fibonacci de {} es {}'.format(num1, fibonacci(num1)))

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987

fibonacci(3)