# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

s = int(input('Введите общее количество журавликов '))
if s % 6 == 0:
    print(f'Петя сделал {s//6} журавликов')
    print(f'Катя сделала {s//3*2} журавликов')
    print(f'Сережа сделал {s//6} журавликов')
else:
    print('Пересчитайте общее количество журавликов')

