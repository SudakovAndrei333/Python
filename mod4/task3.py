def recursive(a, b):
    return a if b == 0 else recursive(b, a % b)


a, b = map(int, input("Введите два целых чисела через пробел: ").split())
print(recursive(a, b))