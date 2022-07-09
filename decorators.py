from datetime import datetime


def Create_log(func):
    def wrapper(*args, **kwargs):
        with open(f'{func.__name__}_log.txt', 'w') as log:
            res = func(*args, **kwargs)
            info = [f'{datetime.today()}, {func.__name__}, {args}, {kwargs}, {res}']
            log.writelines(info)
        return res
    return wrapper


@Create_log
def hello(x):
    return f'Hello {x}'


print(hello('Vasya'))