from datetime import datetime

# В одной папке лежит файл events с событиями
# После запуска файла создается фаил log куда выводится результат
# TO-DO что делать, если следующая минута не наступает, а в текущей был Not OK

current_minute = None
current_time = None
new_minute = None
counter = 0
answer = ""
# Открытие файла с использованием менеджера контекста
with open('events.txt', 'r', encoding='utf-8') as file:
    # Итерация по каждой строке файла
    for line in file:
        for x in line:
            if x == "N":
                # установка времени
                if current_minute == None:
                    current_minute = line[1:20]
                    current_minute = datetime.strptime(current_minute, '%Y-%m-%d %H:%M:%S')
                    current_time = current_minute
                    current_minute = current_minute.strftime("%M")
                    counter += 1
                    print(line)
                else:
                    new_minute = line[1:20]
                    new_minute = datetime.strptime(new_minute, '%Y-%m-%d %H:%M:%S')
                    new_minute = new_minute.strftime("%M")
                    if new_minute == current_minute:
                        counter += 1
                        print(line)
                    else:
                        current_time = line[1:20]
                        # Выгружаем NotOK за прошлую минуту  
                        answer = "[" + current_time + "]" + " " + str(counter) + "\n"
                        # Открытие файла для записи (создаёт новый файл или дописывает в существующий)
                        with open('log.txt', 'a', encoding='utf-8') as file:
                            file.write(answer)
                        current_minute = new_minute
                        counter = 1

