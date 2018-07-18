"""
整数a1,a2,...,anが与えられる。その中からいくつか選び、その和をちょうどkにすることができるかを判定しなさい。
制約
1<=n<=20
-10**8<=ai<=10**8
-10**8<=k<=10**8
"""

n = int(input())
a = list(map(int,input().split()))
k = int(input())

def dfs(i,sum):
    if i == n:
        return sum == k
    if dfs(i+1,sum):
        return True
    if dfs(i+1,sum+a[i]):
        return True
    return False

if __name__ == "__main__":
    if dfs(0,0):
        print ("Yes")
    else:
        print ("No")
