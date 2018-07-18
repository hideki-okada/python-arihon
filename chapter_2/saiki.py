def saiki(n):
    if n == 0:
        return 1
    else:
        return n * saiki(n-1)

if __name__ == "__main__":
    print ("saiki(5) =",saiki(5))
