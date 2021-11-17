import matplotlib.pyplot as plt
import numpy as np


def plot_t():
    x = np.arange(0, 3 * np.pi, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    # plt.show()

    y_sin = np.sin(x)
    y_cos = np.cos(x)
    plt.plot(x, y_sin)
    plt.plot(x, y_cos)
    plt.xlabel('x axis label')
    plt.ylabel('y axis label')
    plt.title('Sine and Cosine')
    plt.legend(['Sine', 'Cosine'])
    # plt.show()

    plt.subplot(2,1,1)
    plt.plot(x, y_sin)
    plt.title('Sine')
    plt.subplot(2, 1, 2)
    plt.plot(x, y_cos)
    plt.title('Cosine')
    plt.show()


plot_t()
