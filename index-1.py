import matplotlib.pyplot as plt
import numpy as np
from pyjones.polarizations import LinearHorizontal
from pyjones.opticalelements import Polarizer
angles = np.linspace(0, 360, 1000)
intensities = [(Polarizer(angle)*LinearHorizontal()).intensity for angle in angles]
plt.plot(angles, intensities)
plt.show()