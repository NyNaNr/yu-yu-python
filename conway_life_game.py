#! /usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 100

x = np.arange(N * N) % N
y = np.arange(N * N) // N

# 初期状態（任意に与える）
a = np.zeros((N, N), dtype="int8")
a[N // 2, N // 2] = 1
a[N // 2 - 1, N // 2] = 1
a[N // 2 + 1, N // 2] = 1
a[N // 2, N // 2 - 1] = 1
a[N // 2 - 1, N // 2 + 1] = 1
a.shape = N * N

fig = plt.figure(figsize=(15, 15))
plt.axis([-1, N, -1, N])
line, = plt.plot(x[a != 0], y[a != 0], ".")


def update(_):
    line.set_data(x[a != 0], y[a != 0])
    b = a.copy()
    for i in range(N + 1, N * N - N - 1):
        n = (
            b[i - N - 1]
            + b[i - N]
            + b[i - N + 1]
            + b[i - 1]
            + b[i + 1]
            + b[i + N - 1]
            + b[i + N]
            + b[i + N + 1]
        )
        if n == 3:
            a[i] = 1
        elif n != 2:
            a[i] = 0


ani = FuncAnimation(fig, update, interval=10)
plt.show()
