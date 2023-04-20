#task6

def prime_number(number: int):
    count = 0
    if number < 0:
        return 'Введите число (не отрицательное)'
    else:
        for i in range(1, number + 1):
            if number % i == 0:
                count += 1
        if count == 2:
            return 'Простое'
        return 'Составное'

if __name__ == '__main__':
    num = int(input())
    print(prime_number(num))
