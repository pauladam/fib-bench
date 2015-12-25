def fib(n : UInt64) : UInt64
    if n == 0 || n == 1
        return n
    else
        return fib(n - 2) + fib(n - 1)
    end
end

n = ARGV.shift.to_u64
puts "%s, %s" % [n, fib(n)]
