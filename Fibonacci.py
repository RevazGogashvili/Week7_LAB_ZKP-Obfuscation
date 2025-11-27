def generate_fibonacci(terms):

    if terms <= 0:
        return []
    elif terms == 1:
        return [0]

    sequence = [0, 1]

    while len(sequence) < terms:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)

    return sequence


result = generate_fibonacci(10)
print(f"Original Code Output: {result}")