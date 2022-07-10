from datetime import datetime


def add_path(path):
    def create_log_on_place(func):
        def wrapper(*args, **kwargs):
            with open(f'{path}{func.__name__}_log.txt', 'w') as log:
                res = func(*args, **kwargs)
                info = [f'{datetime.today()}, {func.__name__}, {args}, {kwargs}, {res}']
                log.writelines(info)
            return res
        return wrapper
    return create_log_on_place


def create_log(func):
    def wrapper(*args, **kwargs):
        with open(f'{func.__name__}_log.txt', 'w') as log:
            res = func(*args, **kwargs)
            info = [f'{datetime.today()}, {func.__name__}, {args}, {kwargs}, {res}']
            log.writelines(info)
        return res
    return wrapper


@add_path('D:/')
def hello(x):
    return f'Hello {x}'


print(hello('Vasya'))
