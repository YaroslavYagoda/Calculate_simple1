while True:
    print ('Консольный калькулятор (для выхода вместо первого числа введите exit)')
    a = input('Введите первое число: ')
    if a.lower() == 'exit':
        print('До свидания!')
        exit()
    a = a.replace(',','.',-1)
    b = input('Введите второе число: ')
    b = b.replace(',','.',-1)
    c = input('введите опперанд ("+","-","*","/"): ')
    try:
        print(eval(a + c + b))
    except SyntaxError:
        print('Ошибка: Введите корректный операнд или число!')
    except ZeroDivisionError:
        print('Ошибка: На ноль делить нельзя!')
    except NameError:
        print('Ошибка: Введите число!')
