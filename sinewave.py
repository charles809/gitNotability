# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import matplotlib.pyplot as plt


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Visual Studio Code')

    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)

    colors = np.random.rand(N)

    area = np.pi * (15 * np.random.rand(N)) ** 2  # 0 to 15 point radii
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)

    plt.show()

    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C, S = np.cos(X), np.sin(X)
    plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
    plt.plot(X, S, color="red", linewidth=2.5, linestyle="-")
    plt.xlim(X.min()*1.1, X.max()*1.1)
    plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

    plt.ylim(C.min() * 1.1, C.max() * 1.1)
    plt.yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])

    plt.show()
