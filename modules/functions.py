def select_level():
    while True:
        tmp = input("Введите номер уровня (1-4): ")
        if tmp.isdigit():
            tmp = int(tmp)
            if 1 <= tmp <= 4:
                return tmp
            else:
                print("Введи число от 1 до 4")
        else:
            print("Введите корректное число")
  
            
def calculate_level():
    min_num = validate_is_number("Введите минимальное число: ")
    max_num = validate_is_number("Введите максимальное число: ")
    health = validate_is_number("Введите количество очков жизни: ")
    return {
        "min": min_num,
        "max": max_num,
        "health": health
    }


def validate_is_number(text):
    while True:
        tmp = input(text)
        if tmp.isdigit():
            return int(tmp)
        else:
            print("Введите число")