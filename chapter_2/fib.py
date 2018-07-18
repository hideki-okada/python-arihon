import time

def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))

if __name__ == "__main__":
    start = time.time()
    print ("fib(30) =",fib(30))
    stop = time.time()
    print (stop-start)
