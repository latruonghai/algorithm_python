import time


def sort_algo(sort_func):
    def wrapper_function(*args, **kwargs):
        start_time = time.process_time()
        sort_func(*args, **kwargs)
        print("Sort function {} run in {} second".format(
            sort_func.__name__, time.process_time() - start_time))
        # print("Sorted Arr is: ", args[0])
    return wrapper_function
