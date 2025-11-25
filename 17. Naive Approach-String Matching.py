def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            positions.append(i)
    return positions

text = "ABABABA"
pattern = "ABA"
print("Pattern found at positions:", naive_string_match(text, pattern))
