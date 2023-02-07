import numpy as np
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt

# Dataset


h_1 = [
        2.74,
        2.65,
        2.69
        
]
h_2 = [
        4.6,
        4.64,
        4.61
]
h = []
for i in range(0, len(h_1)):
    h.append(abs(h_1[i] - h_2[i]))

print(h)

temp = [
        17,
        18,
        19
]

for row in f:
        row = row.split(' ')
        x_1.append(int(row[0]))
        y_1.append(float(row[1]))

x = np.array(h)
y = np.array(temp)

X_Y_Spline = make_interp_spline(x, y)

# Returns evenly spaced numbers
# over a specified interval.
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)

# Plotting the Graph
plt.plot(X_, Y_)
plt.title("This is god damn it graphic, look at it fella!")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("function_graph.png")
