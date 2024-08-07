from Input_value import *
from Result_func import *


def exe():
    input_limit()
    limit = input_limit()
    list_exception = input_exception(limit)
    summ_func(limit, list_exception)


exe()
