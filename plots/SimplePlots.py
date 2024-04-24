import numpy as np
import matplotlib.pyplot as plt

with plt.xkcd():
    v = np.arange(365, 0, -1)

    fig, ax = plt.subplots()
    fig.set_facecolor('whitesmoke')
    fig.set_edgecolor('black')
    ax.set_xlabel('Day of the year')
    ax.set_ylabel('Days until New Year\'s Eve')

    plt.xlim(0, 365)
    plt.ylim(1, 365)

    plt.plot(v)
    plt.show()
    