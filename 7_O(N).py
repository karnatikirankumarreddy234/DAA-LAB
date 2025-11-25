def power_divide_linear(x, n):
    if n == 0:
        return 1
    return x * power_divide_linear(x, n - 1)

if __name__ == "__main__":
    base = 2
    exponent = 10
    print(f"Base: {base}")
    print(f"Exponent: {exponent}")
    print("Result:", power_divide_linear(base, exponent))
