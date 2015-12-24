#!/usr/bin/python

import sys

def fib(n):

    if n == 0 or n == 1:
        return n

    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":

    n = int(sys.argv[1])
    print "%d, %d" % (n, fib(n))
