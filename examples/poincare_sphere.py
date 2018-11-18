from pyjones.polarizations import *
from pyjones.opticalelements import HalfWavePlate, QuarterWavePlate
import numpy as np

# plot QWP
for angle in np.linspace(0, 360, 50):
    pol = QuarterWavePlate(angle) * LinearHorizontal()
    pol.plot(color='r')

# plot HWP
for angle in np.linspace(0, 360, 50):
    pol = HalfWavePlate(angle) * LinearHorizontal()
    pol.plot(color='b')

JonesVector.show()




