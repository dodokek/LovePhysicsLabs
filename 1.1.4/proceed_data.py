import re
import math

def count_sig(array, mid):
    sum_ = 0
    for num in array:
        sum_ += (num - mid)**2
    return (sum_/len(array))**0.5


def sig_percentage(array, sig, mid):
    one_sig = 0
    two_sig = 0
    three_sig = 0
    for num in array:
        if abs(mid - num) < sig:
            one_sig += 1
        if abs(mid - num) < 2*sig:
            two_sig += 1
        if abs(mid - num) < 3*sig:
            three_sig += 1
    print("     В пределах 1 sigma ", one_sig/len(array))
    print("     В пределах 2 sigma ", two_sig/len(array))
    print("     В пределах 3 sigma ", three_sig/len(array))



data = """ 21&15&22&16&16&25&15&21&25&23
           18&27&14&18&18&21&24&20&24&13
           20&17&21&28&18&15&15&18&13&21
           17&16&22&29&19&22&23&25&20&11
           29&22&18&25&17&22&25&24&19&26
           27&31&25&15&17&26&24&25&20&22
           23&23&20&19&20&17&15&31&24&17
           28&19&19&28&14&12&17&18&19&25
           10&20&32&14&14&18&31&25&24&22
           22&20&21&13&23&30&13&13&27&21
           18&25&22&15&17&18&22&27&20&20
           20&19&18&28&14&12&17&18&19&25
           25&20&21&19&29&22&25&14&28&16
           13&19&14&13&17&19&22&19&22&20 
           29&25&18&23&23&16&29&19&20&21
           25&19&16&26&15&14&24&21&25&26
           24&25&19&19&20&15&24&23&12&18
           23&22&17&24&24&34&21&19&18&18
           18&16&29&10&22&28&21&16&16&18
           19&24&15&27&17&14&28&24&16&23"""
# Парсим данные

data_int_20_tmp = []
data_int_20_tmp = re.split("\n", data)
data_int_20 = []

for elem in data_int_20_tmp:
    tmp = []
    tmp = elem.split("&")
    for elem_2 in tmp:
        data_int_20.append(int(elem_2))

data_int_40 = []
for i in range(0, len(data_int_20) - 1, 2):
    data_int_40.append(data_int_20[i] + data_int_20[i+1])

#Выводиm массив на 40

for i in range(0, len(data_int_40)):
    print("&" + str(data_int_40[i]), end="")
    if (i+1) % 10 == 0:
        print(" ")
print("")
#Считаем вероятности для t=40 сек
data_40 = {}
data_int_40.sort()

print("Вероятности для t = 40", data_40)

for elem in data_int_40:
    if elem in data_40.keys():
        data_40[elem] += 1
    else:
        data_40[elem] = 1

for key in data_40.keys():
    data_40[key] = str(data_40[key] / len(data_int_40)) + " Число случаев: " + str(data_40[key])
    print(key, data_40[key])





#Считаем для t=20 вероятности

data_20 = {}
data_int_20.sort()
print("Вероятности для t = 20")
for elem in data_int_20:
    if elem in data_20.keys():
        data_20[elem] += 1
    else:
        data_20[elem] = 1

for key in data_20.keys():
    data_20[key] = str(data_20[key] / len(data_int_20)) + " Число случаев: " + str(data_20[key])
    print(key, data_20[key])



#Средние значения и среднеквадратичная ошибка отдельного измерения

n20 = sum(data_int_20) / len(data_int_20)
print("Среднее n для t=20 ", n20)

n40 = sum(data_int_40) / len(data_int_40)
print("Среднее n для t=40 ", n40)

sig_20 = count_sig(data_int_20, n20)
print("Стандартная ошибка измерения t = 20 ", sig_20)

sig_40 = count_sig(data_int_40, n40)
print("Стандартная ошибка измерения t = 40 ", sig_40)

print("Данны о распределении значений t=20")
sig_percentage(data_int_20, sig_20, n20)

print("Данны о распределении значений t=40")
sig_percentage(data_int_40, sig_40, n40)

print("Стандартная ошибка отклонения n20", sig_20/len(data_int_20))
print("Стандартная ошибка отклонения n40", sig_40/len(data_int_40))

