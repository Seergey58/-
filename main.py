print('hellow world')
k = open('moy.txt', 'r')  #открываем файл и читаем его
ko = k.read()  # сохраняе то, что прочитали и называем его ko
print(ko)  # выводим данные из файла
k.close()  # закрываем файл (зачем не знаю так как ничего не меняет, но выглядит логично)
parts = ko.split(',')  # разбиваем значения из по запятым, что питон не считал пробелы и запятые)
koz = [int(f) for f in parts]  # функция "int" преобразует строку цифр в объекты целых чисел и получаем список, который называем "koz"
A = len(koz)  # длина списка или количество элементов
for j in range(A - 1):  # кол-во прогонов
    for r in range(A - 1):  # выбираем какой-то элемент из (А - 1) и далее сравниваем его
        if koz[r] > koz[r + 1]:  # если элемент справа меньше, то меняем их местами
            koz[r], koz[r + 1] = koz[r + 1], koz[r]
print(koz)
