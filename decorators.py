import datetime

import os

# creates log in current directory
def dec_logger_rel(old_func):
    def new_func(*args, **kwargs):
        with open('log.txt', 'a') as file:
            file.write(str(datetime.datetime.now()) + '\nName of function:' + str(old_func.__name__) + '\nArguments:' +
                       str(*args, **kwargs) + '\n\n')
        return old_func(*args, **kwargs)
    return new_func

# creates log in given directory
def dec_logger_abs(path):
    PATH = path

    def decorator(old_func):
        def new_func(*args, **kwargs):
            with open(PATH +'/log.txt', 'a') as file:
                file.write(
                    str(datetime.datetime.now()) + '\nName of function:' + str(old_func.__name__) + '\nArguments:' +
                    str(*args, **kwargs) + '\n\n')
            return old_func(*args, **kwargs)
        return new_func
    return decorator
