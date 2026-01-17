def get_the_fastest_func(funcs, arg):
    import time
    l = {}
    for f in funcs:
        st = time.monotonic()
        f(arg)
        en = time.monotonic()
        tm = en - st
        l.setdefault(tm, f)
    return l[min(l)]

from math import factorial                   # функция из модуля math     


def factorial_recurrent(n):                  # рекурсивная функция
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)    


def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f    
funcs = [factorial, factorial_recurrent, factorial_classic]

print(get_the_fastest_func(funcs, 900))


        
