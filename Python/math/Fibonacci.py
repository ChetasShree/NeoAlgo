"""
Function to print first n Fibonacci Numbers
n takes the input of first n numbers to be printed
"""


def fibonaccinumber(n):
    """
    >>fibonaccinumber(6)
    1 1 2 3 5 8

    >>fibonaccinumber(10)
    1 1 2 3 5 8 13 21 34 55

    """
    
    if n<0:
        print("Incorrect input")    

    elif n==0:
        return 0
    
    elif n==1:
        return 1

    else:
        n1 , n2 =1,1
        count = 1
        while count < n: 
            print(n1 , end = ' ')       
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1            
        return n1

    

n = int(input(">>"))
print(fibonaccinumber(n))
