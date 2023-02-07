import numpy as np
import math
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

# Dataset


h_1 = [
        2.74,
        2.65,
        2.69,
        2.61,
        2.55,
        2.5,
        2.46,
        2.41,
        2.36,
        2.22,
        2.19,
        2.1,
        2.06,
        1.97,
        1.91,
        1.85,
        1.74,
        1.61,
        1.51,
        1.4,
        1.29,
        1.14,
        1.03,
        0.82,
        1.09,
        1.33,
        1.5,
        1.69,
        1.89,
        2.04,
        2.22,
        2.32,
        2.46,
        2.56,
        2.67
        
]
h_2 = [
        4.6,
        4.64,
        4.61,
        4.71,
        4.78,
        4.82,
        4.84,
        4.96,
        5,
        5.05,
        5.1,
        5.21,
        5.3,
        5.4,
        5.42,
        5.58,
        5.67,
        5.74,
        5.91,
        6.01,
        6.1,
        6.19,
        6.35,
        6.48,
        6.3,
        6.1,
        5.82,
        5.65,
        5.46,
        5.3,
        5.13,
        5.01,
        4.9,
        4.72,
        4.66
]
temp1 = np.array([i for i in range(273+17, 273+41)])
temp2 = np.array([i for i in range(273+38, 273+17, -2)])
temp = np.concatenate ((temp1, temp2))
# print(temp)
h = []
for i in range(0, len(h_1)):
    h.append(1400 * float(abs(h_1[i] - h_2[i])))


# print(h)


x = np.array(h)





for elem in temp:
        print(elem)

# Plotting the Graph
plt.plot(x, temp, 'bo')
plt.title("Зависимость P от T")
plt.xlabel("P (Па)")
plt.ylabel("T (К)")


linear_model=np.polyfit(x,temp,1)
linear_model_fn=np.poly1d(linear_model)
x_s=np.arange(0,8000)
plt.plot(x_s,linear_model_fn(x_s),color="green")

plt.savefig("function_graph.png")

plt.clf()


ln_h = []
for elem in h:
        ln_h.append(math.log(elem))

rev_t = []

for elem in temp:
        rev_t.append(1/(elem) * 1000)

# Plotting the Graph
plt.plot(rev_t, ln_h, 'bo')
plt.title("Зависимость ln(P) от 1/T")
plt.xlabel("1/T * 10^-3")
plt.ylabel("ln (P)")


linear_model=np.polyfit(rev_t,ln_h,1)
linear_model_fn=np.poly1d(linear_model)
x_s=np.arange(2.9,4)
plt.plot(x_s,linear_model_fn(x_s),color="green")

plt.savefig("ln_graph.png")


