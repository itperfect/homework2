# 1. Написать функцию, которая будет принимать на вход натуральное число n, и возращать сумму его цифр.
# Реализовать используя рекурсию (без циклов, без строк, без контейнерных типов данных).
# Пример: get_sum_of_components(123) -> 6 (1+2+3)

def get_sum_of_components(summ = 0):
    if summ < 1:
        return 0
    else:
        num = summ / 10
        ost = round(num%1, 1) * 10

        num = int(num)
        ost = int(ost)

        return ost + get_sum_of_components(num)


res = get_sum_of_components(135 + 531)
print(res)
