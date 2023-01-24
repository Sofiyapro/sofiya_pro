"""Игра угадай число."""
import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    min = 1 # мнимальное возможное значение
    max = 100 # максимальное возможное значение
    predict_number = np.random.randint(1, 101)
    while True:
        count+=1
        if number>predict_number:
            min = predict_number
            predict_number = max - (max - min)//2
        elif number<predict_number:
            max = predict_number
            predict_number = min + (max - min)//2
        else: 
            break
    
    # Ваш код заканчивается здесь

    return count

def score_game(random_predict) -> int:
    """За какое количество в среднем угадывает наш подход

    Args:
        random_predict (_type_): Функция угадвыния

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 100, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))    
    print(f'Ваш алгоритм угадыыает число в среднем за:{score} попыток')
    return(score)