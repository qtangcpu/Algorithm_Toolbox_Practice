# Uses python3
def calc_fib(n):
    a0 = 0
    a1 = 1
    if n !=0:
        for i in range(2,n+1):
            a0,a1 = a1%10, (a0%10+a1%10)%10
        return a1
    else:
        return a0

n = int(input())
print(calc_fib(n))
