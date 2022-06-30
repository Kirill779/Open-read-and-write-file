list_file = ['1.txt','2.txt','3.txt'] #создаем список исходных файлов
data_file = {} #словарь для хранения исходных данных из файлов
num_str = []   #вспомогательный список для сортировки
for file_name in list_file:     # считываем данные файлов
    with open(file_name, encoding='utf8') as file:
        len_file = 0    # определяем количество строк в файле
        dict_file = {}  # внутренний словарь для данных конкретного файла
        for line in file:  # считываем данные непосредственно из файла
            len_file += 1
            dict_file[len_file] = line.strip()   # записываем данные файла в спомогательный словарь
            data_file[file_name] = dict_file,len_file  # записываем данные в основной словарь
    num_str.append(len_file)    # записываем длинну строк в список

with open('Result.txt', 'w', encoding='utf8') as file_result: #
    number = 2
    for i in sorted(num_str):     # сортируем список по количеству строк в файле
        for k,n in data_file.items():    # выбираем данные для записи
            if i == n[1]:
                str_nn = 1
                file_result.write(f'{k} \n')    # записываем данные, имя файла
                file_result.write(f'{str(number)} \n')  #требование задачи
                number -= 1
                for s in n[0].values():
                    file_result.write(f'Строка номер {str_nn},файла номер {k[:1]} \n')   # требования задачи
                    str_nn += 1
    file_result.write('\n')
    for i in sorted(num_str):     # повторяем цикл для окончательной записи данных
        for k, n in data_file.items():
            if i == n[1]:
                str_nn = 1
                for s in n[0].values():
                    file_result.write(f'{s} \n')   # окончательные данные результирующего файла
                    str_nn += 1
