def power_naive(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result

if __name__ == "__main__":
    base = 2
    exponent = 10
    print(f"Base: {base}")
    print(f"Exponent: {exponent}")
    print("Result:", power_naive(base, exponent))
