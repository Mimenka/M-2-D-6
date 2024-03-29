# 1.
# def get_upper(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper

# @get_upper
# def get_text():
#     return 'hello world!'
# print(get_text())

# 2.
# def cypher_number(func):
#     def wrapper():
#         phone_number = func()
#         cypher_num = ''
#         for i, p in enumerate(phone_number):
#             if i in (0,1,2):
#                 cypher_num += p
#             elif i in (10, 11):
#                 cypher_num += p
#             else:
#                 cypher_num += '#'
        
#         return cypher_num
#     return wrapper


# @cypher_number
# def get_number():
#     return '996700123456'

# print(get_number())

# 3.
# def greeting(func):
#     def wrapper():
#         print('Привет, сейчас я буду показывать номер телефона')
#         result = func()
#         return result
#     return wrapper

# @greeting
# def get_number():
#     return '996700123456'

# print(get_number())

# 4.
# def double_salary(func):
#     def wrapper():
#         result = func()
#         return result * 2
#     return wrapper


# @double_salary
# def get_salary():
#     salary = 50000
#     return salary

# print(get_salary())

# 5.
# def print_notification(func):
#     def wrapper():
#         result = func()
#         print('Функция выполнилась')
#         print(f'Вам начислили зарплату на сумму {result}')
#         return result
#     return wrapper

# @print_notification
# def get_salary():
#     salary = 50000
#     return salary
# print(get_salary())

# 6.
import time 

def timer_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f'Функция отпрвки сообщений пользователям заняло \n \
              {end_time - start_time} секунд')
    return wrapper

@timer_decorator
def send_massage_to_users():
    users = range(1,1001)

    for user in users:
        print(f'Отправка сообщения пользвателю {user}')

send_massage_to_users()

