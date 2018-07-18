def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 2)


n = factorial(2)

a = {1, 2, 3}
b = {4, 4, 5}

print(a.symmetric_difference(b))
print(a.difference(b))
print(a.intersection(b))
print(a.union(b))


a = {2, 3}

n = a < b

print(n)


print(5 / 4)

print(5 // 4)

print(5 % 4)

a = 5
b = 7

print(a < b)
print(a > 2 and b < 5)
print(a < 2 and b > 5)
print(a < 2 or b < 5)
print(a < 2 or b > 5)
print(not a == 7)
print('rt' < 'a')


def f(x):
    return (x * (x + 2)) / 2


# print(f(3))


def User():
    x = 0

    while x < 1:
        name = input("what is your name: ")
        option = int(input("pick a num 1 or 2:  "))

        if option == 1:
            print("Hello " + name)
        elif option == 2:
            print("Goodbye " + name)
        x = x + 1


n = [2, 3, 5, 6, 20]

maxVal = max(n)


for i in range(0, len(n), 1):
    if maxVal < n[i]:
        maxVal = n[i]


print(maxVal)


lists = [3, 5, 6, 8, 3]


