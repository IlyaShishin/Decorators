from datetime import datetime, date, time


def logger(log_path):
    def decorator(function):
        def new_function(*args, **kwargs):
            name = f'Вызвана функция: {function.__name__}'
            params = f'С параметрами: {args}, {kwargs}'
            result = function(*args, **kwargs)
            with open(log_path, 'a', encoding='utf-8') as f:
                f.write(f'{datetime.now()}\n {name}\n {params}\n Полученный результат: {result}\n')
            return f'Информация записана в файл'
        return new_function
    return decorator


@logger(r'C:\Users\Илья\PycharmProjects\Decorators\Log_result.txt')
def calculate(a, b):
    result = a + b
    return result


print(calculate(2, 3))


