import pyjones
from pyjones.polarizations import LinearHorizontal
from pyjones.opticalelements import HalfWavePlate, QuarterWavePlate
import numpy as np

fig1, ps = pyjones.polarizations.get_Poincare_sphere()
fig2, ps2 = pyjones.polarizations.get_Poincare_sphere()


# plot QWP
for angle in np.linspace(0, 360, 50):
    pol = QuarterWavePlate(angle) * LinearHorizontal()
    pol.plot(ps, color='r')

# plot HWP
for angle in np.linspace(0, 360, 50):
    pol = HalfWavePlate(angle) * LinearHorizontal()
    pol.plot(ps2, color='b')

pyjones.polarizations.show_plots()




