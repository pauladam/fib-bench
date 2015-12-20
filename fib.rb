#!/usr/bin/ruby

def fib n
    if n == 0 || n == 1
        return n
    else
        return fib(n - 2) + fib(n - 1)
    end
end

n = ARGV.shift.to_i
puts "%s, %s" % [n, fib(n)]
