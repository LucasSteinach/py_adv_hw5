from decorators import dec_logger_rel, dec_logger_abs
import os

@dec_logger_rel
def hello():
    print('Hello world!')


@dec_logger_abs(os.getcwd())
def bye_bye(name):
    print(f'Bye bye, {name}!')


if __name__ == '__main__':
    # hello()
    bye_bye('Gustav')
