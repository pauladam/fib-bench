use std::env;

fn fib(n: u32) -> u32 {
    if n == 0 {
        n
    } else if n == 1 {
        n
    } else {
        fib(n - 1) + fib(n - 2)
    }
}

fn main() {
    // Get command line arg 1
    let args: Vec<_> = env::args().collect();
    let n: u32 = args[1].parse().unwrap();
    println!("{}, {}", args[1], fib(n).to_string());
}
