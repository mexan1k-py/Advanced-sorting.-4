# Task 1
# Вывод бинарного представления числа
n = int(input())

def binnarchis(n):
    if n < 2:
        print(n, end=' ')
    else:
        binnarchis(n // 2)
        print(n % 2, end=' ')

result = binnarchis(n)
print(result)

##############################################################
# Task 2
# Умножение при помощи рекурсии
n1 = int(input())
n2 = int(input())

def mul(n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    if n2 == 1:
        return n1
    if n1 == 1:
        return n2
    return n1 + mul(n1, n2 - 1)

def mul2(n1, n2):
    result = mul(n1, abs(n2))
    return result

result = mul2(n1, n2)
print(result)
##############################################################
# Task 3
#  Возведение в степень при помощи рекурсии
n1 = int(input())
n2 = int(input())

def step(n1, n2):
    if n1 == 0:
        return 1
    if n2 == 1:
        return n1
    if n2 != 1:
        return n1 * step(n1, n2 - 1)

result = step(n1, n2)
print(result)
