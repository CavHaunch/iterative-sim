import numpy as np 
import matplotlib.pyplot as plt

def plot(data):
    plt.figure(1)
    plt.plot(np.arange(len(data))/60,data)
    plt.title('Vacuum pressure control simulation output')
    plt.xlabel('time /minutes')
    plt.ylabel('vacuum pressure /mbar')
    plt.show()