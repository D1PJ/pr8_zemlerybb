import random
login = input('Login ')
password = ''
for x in range(11): #Количество символов (11)
    password = password + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦШЩЪЫЬЭЮЯ')) #Символы
print('Hello, ', login, 'your password is: ', password)
