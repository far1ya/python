
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = fibonacci(n - 1)
        fib.append(fib[-1] + fib[-2])
        return fib

n = int(input("Enter the number of terms: "))

fib_sequence = fibonacci(n)
print(f"The first {n} Fibonacci terms are: {fib_sequence}")
