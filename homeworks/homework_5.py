# import datetime
# def checktime(func):
#     def wrapper(*args, **kwargs):
#         check_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         print(f"Функция '{func.__name__}' вызвана в {check_time}")
#         return func(*args, **kwargs)
#     return wrapper
# from datetime import datetime as dt
# time_now = dt.now()
# print(time_now.year) # текущий год
# print(time_now.month) # текущий месяц
# print(time_now.day) # текущее число
# print(time_now.hour) # текущий час
# print(time_now.minute) # текущая минута
# print(time_now.second) # текущая секунда
# @checktime
# def hello_world():
#     print("hello world")
# hello_world()
# # функция была вызвана в 20:39:10 15/07/2025
# # hello_world
# from time import sleep
# def checktime_before_after(func):
#     def wrapper(*args, **kwargs):
#         print(f"checktime_before_after:функция была вызвана в:{time_now}")
#         result = func(*args, **kwargs)
#         print(f"checktime_before_after:функция закончила роботу в:{datetime.datetime.now()}")
#         return result
#     return wrapper
# @checktime_before_after
# def hello_world():
#     print("hello world")
#     sleep(1)  # чтобы функция выполнялась 1 секунду
# hello_world()
# функция была вызвана в 20:39:10 15/07/2025
# hello_world
# функция была закончена в 20:40:11 15/07/2025


