def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    elif length == 1:
        fib_sequence = [0]
    elif length == 2:
        fib_sequence = [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < length:
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
    print(fib_sequence)

# Example usage:
print_fibonacci(9)