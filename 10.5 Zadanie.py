import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:  # Открываем файл для чтения
        while True:
            line = file.readline()  # Считываем строку
            if not line:  # Если строка пустая, выходим из цикла
                break
            all_data.append(line.strip())  # Добавляем строку в список (удаляем пробелы)
    return all_data

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time_linear = time.time()  # Сохраняем время начала
    for filename in filenames:
        data = read_info(filename)
    end_time_linear = time.time()  # Сохраняем время окончания
    print(f'Время выполнения (линейный): {end_time_linear - start_time_linear:.3f} секунд')

    # Многопроцессный подход
    start_time_multiprocessing = time.time()  # Сохраняем время начала
    with Pool() as pool:
        results = pool.map(read_info, filenames)
    end_time_multiprocessing = time.time()  # Сохраняем время окончания
    print(f'Время выполнения (многопроцессный): {end_time_multiprocessing - start_time_multiprocessing:.3f} секунд')