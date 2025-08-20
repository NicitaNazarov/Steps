import datetime as DT

STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}  # Словарь для хранения полученных данных.

def check_correct_data(data):

    for item in data:

        if len(data[0]) != 2 or data == None:
            print ('Ошибка длинны пакета')
            return False
        
        else:
            return True
        
    # Если длина пакета отлична от 2
    # или один из элементов пакета имеет пустое значение -
    # функция вернет False, иначе - True.


def check_correct_time (time):

    """Проверка корректности параметра времени."""
    if time != None:
        return True
    else:
        print ('Ошибка. Пакет времени пустой')
        return False
    
    # Если словарь для хранения не пустой
    # и значение времени, полученное в аргументе,
    # меньше или равно самому большому значению ключа в словаре,
    # функция вернет False.
    # Иначе - True 

def get_step_day(steps):

    """Получить количество пройденных шагов за этот день."""

    steps = sum(storage_data.values())
    return steps

    # Посчитайте все шаги, записанные в словарь storage_data,
    # прибавьте к ним значение из последнего пакета
    # и верните  эту сумму.

def get_distance(steps):

    """Получить дистанцию пройденного пути в км."""
    distance = steps * 0.65 / 1000
    return distance

def get_spent_calories (steps):
    """Получить значения потраченных калорий."""
    
    spent_calories = steps * 0.04 
    return spent_calories
    # В уроке «Последовательности» вы написали формулу расчета калорий.

def achive (distance):
    if distance >= 6.5:
        message = 'Отличный результат! Цель достигнута.' 
    elif distance >= 3.9:
        message = 'Неплохо! День был продуктивный'
    elif distance >= 2:
        message = 'Завтра наверстаем'
    else:
        message = 'Лежать тоже полезно. Главное — участие, а не победа!'
    return message

def show_message (time, steps_per_day, distance, calories, achive):
    
    print (f'Время : {time} .')
    print (f'Количество шагов за сегодня: {steps_per_day} .')
    print (f'Дистанция за сегодня составила: {distance} км .')
    print (f'Вы сожгли {calories:.2f} ккал .')
    print (achive)

def watch_on (input_list):
    for i in input_list:
        steps, time = i
        
        if check_correct_time(time) == True and check_correct_data (input_list ) == True:
            time = DT.datetime.strptime(f'{time}', '%H:%M:%S').time()
            storage_data [f'{time}'] = steps
            steps_per_day = get_step_day (steps)
            distance = get_distance (steps)
            calories = get_spent_calories (steps)
            message = achive (distance)
        else:
            print ("Ошибка")

    show_message (time, steps_per_day, distance, calories, message)

watch_on ([(100, '9:22:12'), 
              (200, '9:23:12'),
              (30000, '9:24:12')])
