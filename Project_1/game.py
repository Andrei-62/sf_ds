import numpy as np


def game_core(number: int=1) -> int:
    """Функции на вход подается целое число от 1 до 100
       на выходе число попыток угадать 

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    
    def predict_num(number: int, num_1: int, num_2: int) -> int:
        """ Генерим рандомное число в заданных пределах, 
            если 

        Args:
            num_1 (int): Нижний предел
            num_2 (int): Верхний предел

        Returns:
            int: Число попыток
        """
        count = 1
        predict = np.random.randint(num_1, num_2)

        while number != predict:
            count += 1
            if number > predict:
                predict += 1
            elif number < predict:
                predict -= 1
                
        return count
    
        
    if number <= 25:
        return predict_num(number, 1, 26)
    elif number <= 50:
        return predict_num(number, 26, 51)
    elif number <= 75:
        return predict_num(number, 51, 76)
    else:
        return predict_num(number, 76, 101)
            
    
def score_game(game_core) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
    
if __name__ == '__main__':
    score_game(game_core)      
                             