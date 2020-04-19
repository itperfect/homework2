# 2. Написать декоратор log, который будет выводить на экран все аргументы, которые передаются вызываемой функции.
# @log
# def my_sum(*args):
# return sum(*args)

# my_sum(1,2,3,1) - выведет "Функция была вызвана с - 1, 2, 3, 1"
# my_sum(22, 1) - выведет "Функция была вызвана с - 22, 1"


def log(func):

    def wrapper(*args):
        args_in_string = ", ".join(map(str, args))
        print(f'Функция была вызвана с - {args_in_string}')

    return wrapper


@log
def my_sum(*args):
    pass


if __name__ == "__main__":
    my_sum(1,2,3,1)
    my_sum(22,1)
