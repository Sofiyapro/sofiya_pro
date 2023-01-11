"""Игра угадай число.
Компьютер сам загадывает и угадывает число"""
import numpy as np

def random_predict(number:int=1) -> int:
    """ Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101)
        if number==predict_number:
            break
    return(count)

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

if __name__ == '__main__' :
    score_game(random_predict)