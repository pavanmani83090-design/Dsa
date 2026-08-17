def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def pfib(n, i):
    if i == n:
        return
    else:
        print(fib(i))
        pfib(n, i + 1)


n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Wrong input")
else:
    pfib(n, 0)
