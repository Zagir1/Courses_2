#task 7

print('Числa Фибоначчи')
a=1
b=1
print ('Введите число: ')
number = int(input())

i = 0
while i < (number-2):
    fib = a+b
    a = b
    b = fib
    i = i+1

print('Номер ряда = ',number,' ,его значение = ', fib)