n=int(input("Enter the no of terms:"))

def fib(n):
    if(n<=1):
        return n
    else:
        return(fib(n-1)+fib(n-2))
    

if n==1:
    print("1")
elif(n==2):
    print("1,2")
else:
    for i in range(n):
        print(fib(i))
