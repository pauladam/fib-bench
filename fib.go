package main

import (
	"fmt"
	"os"
	"strconv"
)

func fib(n int) int {
	if n == 0 || n == 1 {
		return n
	} else {
		return fib(n-2) + fib(n-1)
	}

}

func main() {
	n, _ := strconv.Atoi(os.Args[1])
	fmt.Printf("%d, %d\n", n, fib(n))
}
