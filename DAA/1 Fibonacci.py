
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-2)+fib(n-1)

n=int(input("Enter the end : "))

for i in range(n):
    print(fib(i))


"""
def fibo(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b

num=int(input("Enter the limit : "))
print("Iterative Fibonacci Series is :")
fibo(num)"""



def itrfibo(n):
    a,b=0,1
    for i in range(n):
        print(a,end=' ')
        a,b=b,a+b

num=int(input("Enter the Limit : "))
itrfibo(num)
