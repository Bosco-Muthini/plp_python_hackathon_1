def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence[:n]

def main():
    n = int(input("Enter the value of n: "))
    if n <= 0:
        print("Please enter a positive integer.")
        return
    fibonacci_sequence = generate_fibonacci_sequence(n)
    print("Fibonacci sequence up to term", n, ":", fibonacci_sequence)

if __name__ == "__main__":
    main()
