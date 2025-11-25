unlock = int(input("Enter unlock pin: "))
current = int(input("Enter current pin: "))

rotation = 0
while unlock > 0:
    r_term = unlock % 10
    l_term = current % 10
    rotation += min(abs(r_term - l_term), 10 - abs(r_term - l_term))
    unlock //= 10
    current //= 10

print("Minimum rotations:", rotation)
