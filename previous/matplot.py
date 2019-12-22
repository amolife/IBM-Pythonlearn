import matplotlib.pyplot as plt
from numpy.random import randn
import numpy as np


def f1():
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)
    ax1.hist(randn(100), bins=20, color='k', alpha=0.3)
    print(randn(100))
    ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30))
    plt.show()


def f2():
    fig, axes = plt.subplots(3, 2, sharex=True, sharey=True)
    print(axes[2, 1])
    print(axes[1, 0])
    for i in range(3):
        for j in range(2):
            axes[i, j].hist(randn(500), bins=50, color='k', alpha=0.5)

    plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9,
                        top=0.9, wspace=0.05, hspace=0.05)

    plt.show()


def f3():
    fig = plt.figure()
    plt.plot(randn(30).cumsum(), 'ro--',label='defaultt') # line1
    plt.plot(randn(30).cumsum(), color='g', linestyle='dashed', marker='o') # line2
    data = randn(50).cumsum()
    plt.plot(data, color='b', drawstyle='steps-post', label='steps-ppost') # line3
    plt.legend(loc='best') # best location
    ax = fig.add_subplot(1,1,1)
    ax.set_title('no chinese accepted..waiting....')
    ax.set_xlabel('WTF....')
    ax.set_ylabel('W....')
    plt.show()



f3()
