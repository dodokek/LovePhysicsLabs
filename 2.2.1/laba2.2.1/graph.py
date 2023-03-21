import numpy as np
import math
import matplotlib.pyplot as plt


with open('dedus/29.7.csv') as f:
    lines = [line.rstrip('\n') for line in f]

time = []
voltage = []

for line in lines:
    tmp1, tmp2 = line.split(",")
    time.append(float(tmp1))
    voltage.append(math.log(float(tmp2)/13.5))


# print(time, end="\n")
# print(voltage, end ="\n")

x = np.array(time)
y = np.array(voltage)

plt.plot(x, y, 'b')


with open('dedus/88.csv') as f:
    lines = [line.rstrip('\n') for line in f]

time = []
voltage = []

for line in lines:
    tmp1, tmp2 = line.split(",")
    time.append(float(tmp1))
    voltage.append(math.log(float(tmp2)/15))


# print(time, end="\n")
# print(voltage, end ="\n")

x = np.array(time)
y = np.array(voltage)

plt.plot(x, y, 'b', color="red")


with open('dedus/128.csv') as f:
    lines = [line.rstrip('\n') for line in f]

time = []
voltage = []

for line in lines:
    tmp1, tmp2 = line.split(",")
    time.append(float(tmp1))
    voltage.append(math.log(float(tmp2)/12.7))


# print(time, end="\n")
# print(voltage, end ="\n")

x = np.array(time)
y = np.array(voltage)

plt.plot(x, y, 'b', color="green")
plt.title("Зависимость логарифма напряжения от времени")
plt.xlabel("Время(с)")
plt.ylabel("ln(V\V0)")

plt.savefig("function_graph.png")