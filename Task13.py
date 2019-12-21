N = int(input("Number: "))
a = 0

while a <= N:
    a = a + 1
    b = a ** 2
    if b <= N:
        print(b)
    else:
        break

