from datetime import datetime
list = []
def logger(func):
    def wrapper(*args, **kwargs):
        current_datetime = datetime.now()
        function_name = func.__name__ 
        try:
            result = func(*args, **kwargs)
            data = f'{current_datetime}, {function_name},{args},{result},success '
        except Exception as Error:
            data = f'{current_datetime}, {function_name},{args},{result},failed: {Error} '
        list.append(data)
        print(list)
        return data
    return wrapper

@logger
def data_time(get):
    return 'bla bloca'

data_time('some func')

data_time('na na na')


def get_logs():
    with open ('text.txt', 'a', newline='') as file:
        for functions in list:
            file.write(functions + '\n')
            yield functions
log = get_logs()
print(next(log))
print(next(log))
