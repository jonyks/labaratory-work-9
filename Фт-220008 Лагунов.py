import logging
logging.basicConfig(filename="sample.log", level=logging.INFO)
from random import randint
try:     #Для проверки чилового значения n
    n=int(input("Введите размер мешочка "))
except:
    print('Размером мешочка служит число')
    logging.error("An error has happened!")
    quit()
v=list(range(1,n+1))
for i in range(n):# Для перебора всех бочонков
    c=randint(1,n-i)
    print('Выпал бочонок под номером ',v[c-1] )
    logging.info(f'Удаление {v[c-1]} бочонка')
    v.pop(c-1)
    input('Введите enter чтобы продолжить')


