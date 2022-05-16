import numpy as np
import matplotlib.pyplot as mpl


def plot_sine_curve() -> None:
    """
    The function compute the x and y coordinates for points on a sine curve and plot the points using matplotlib.
    :return: None
    """
    x = np.arange(-3, 3, 1)
    mpl.plot(x, np.sin(x))
    mpl.show()


if __name__ == "__main__":
    plot_sine_curve()
