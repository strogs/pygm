import os
import numpy
from modules.functions import select_level, calculate_level, validate_is_number

min_num = 1
max_num = 100
min_user_num = int()
max_user_num = int()
selected_level = int()
secret_number = int()
win_points = 1000
health = 10
# print(secret_number)
health_icon = "❤️"

os.system('cls' if os.name == 'nt' else 'clear')

print('==============================================')
print('================ Угадай число ================'.upper())
print('==============================================')

print("Выберите уровень сложности:")
print("1) Легкий    | Числа от 1 до 100  | 10 жизни")
print("2) Средний   | Числа от 1 до 100  | 7 жизней")
print("3) Сложный   | Числа от 1 до 100  | 4 жизней")
print("4) Кастомный | Числа от ? до ?    | ? жизней")
    
selected_level = select_level()

match(selected_level):
    case 1:
        health = 10
        print('\n==============================================')
        print('Выбран \033[1mЛегкий\033[0m уровень сложности')
        print('==============================================')
    case 2:
        health = 5
        print('\n==============================================')
        print('Выбран \033[1mСредний\033[0m уровень сложности')
        print('==============================================')
    case 3:
        health = 4
        print('\n==============================================')
        print('Выбран \033[1mСложный\033[0m уровень сложности')
        print('==============================================')
    case 4:
        print('\n==============================================')
        print('Выбран \033[1mКастомный\033[0m уровень сложности')
        print('==============================================')
        builded = calculate_level()
        min_num = builded["min"]
        max_num = builded["max"]
        health = builded["health"]        
        print('==============================================')

secret_number = numpy.random.randint(min_num, max_num)

print('\nОтлично! Я загадал число от {} до {}'.format(min_num, max_num))
print('Попробуй отгадать за {} {}'.format(health, health_icon))
print('Давай приступим!')


while True:
    if health <= 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n==============================================')
        print('=========== 💀 G A M E   O V E R 💀 ==========')
        print('==============================================')
        print("У вас не осталось жизней 💔.")
        print('Загаданное число: \033[1m{}\033[0m'.format(secret_number))
        print('==============================================')
        break
    else:
        print("\nЗдоровье: " + health_icon * health)
        print("Очки     : {}".format(win_points))
        
    user_num = validate_is_number("Введите чило: ")

    if (secret_number != user_num):
        if min_user_num and max_user_num:            
            if user_num > min_user_num and user_num < secret_number:
                min_user_num = user_num
            if user_num < max_user_num and user_num > secret_number:
                max_user_num = user_num
            if secret_number - min_user_num <= 10 or max_user_num - secret_number <= 10:
                win_points += 3
            print("\033[1mЗагаданное число больше {} и меньше {}\033[0m".format(min_user_num, max_user_num))
        else:
            if secret_number > user_num:
                min_user_num = user_num
                print("\033[1mЗагаданное число больше {}\033[0m".format(user_num))
            else:
                max_user_num = user_num
                print("\033[1mЗагаданное число меньше {}\033[0m".format(user_num))    
        health -= 1
        win_points -= 10
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('==============================================')
        print('================ 🎉 \033[1mПОБЕДА!\033[0m 🎉 ===============')
        print('==============================================')
        print('🎲 Загаданное число: \033[1m{}\033[0m'.format(secret_number))
        print('==============================================')
        print('{} Оставшиеся жизни: {} (+{} очков)'.format(health_icon, health_icon * health, health * 10))
        print('🏆 Оставшиеся очки: {}'.format(win_points))
        print('==============================================')
        win_points += 10 * health
        print('💎 Всего очков: {}'.format(win_points))
        break



        