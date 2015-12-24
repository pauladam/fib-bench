import os
from strutils import parseInt

proc fib(n: int): int =

    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)

try:
    let n = parseInt(paramStr(1).string)
    echo(n, ", ", fib(n))
except:
    discard
