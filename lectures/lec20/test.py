def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("fibo(10)", number=100, setup="from __main__ import fibo"))
