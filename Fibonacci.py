def Fibonacci (n):
    a = 0
    b = 1
    if n == 0:
        return 0
    elif n == 1 :
        return 1
    else:
        print(a)
        print(b)
        for i in range (2 , n):  
            c = a + b
            a = b
            b = c
            print(c)
        print("Fibonacci numer is : ")
        return c
k = 20      
print(Fibonacci (k))