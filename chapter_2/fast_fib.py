import time

MAX_N = 100000
memo = [0 for i in range(MAX_N+1)]
def fib(n):
    if n <= 1:
        return n
    if memo[n] != 0:
        return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    print ("memo["+str(n)+"] =",memo[n])
    return memo[n]

if __name__ == "__main__":
    start = time.time()
    print ("fib(30) =",fib(30))
    stop = time.time()
    print (stop-start)
