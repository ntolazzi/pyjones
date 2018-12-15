The following code snippet shows a classic example of the surprising effects of
light polarization

.. ipython::

    In [1]: from pyjones.polarizations import LinearHorizontal

    In [2]: from pyjones.opticalelements import Polarizer, PolarizerVertical

    In [3]: input_polarization = LinearHorizontal()

    In [4]: output_polarization = PolarizerVertical()*input_polarization

    In [5]: print("Output: %s, Intensity: %.2f" %(output_polarization, output_polarization.intensity))

That means the light is perfectly blocked. We now put in one more polarizer:

.. ipython::

    In [6]: output_polarization = PolarizerVertical()*Polarizer(45)*input_polarization

    In [7]: print("Output: %s, Intensity: %.2f" %(output_polarization, output_polarization.intensity))

That means if we put in one more polarizer in the middle suddenly there is light again.

You can also use **PyJones** to visualize for example
`Malus' law <https://en.wikipedia.org/wiki/Polarizer#Malus.27_law_and_other_properties>`_ that states the the
transmitted intensity of a linear polarized beam trough a polarizer is given by

.. math::
    I \propto \cos^2(\theta)

where :math:`\theta` is the angle between the input polarization and the polarizer.


.. ipython::
    @savefig

    In [1]: import matplotlib.pyplot as plt

    In [2]: import numpy as np

    In [3]: from pyjones.polarizations import LinearHorizontal

    In [4]: from pyjones.opticalelements import Polarizer

    In [5]: angles = np.linspace(0, 360, 1000)

    In [6]: intensities = [(Polarizer(angle)*LinearHorizontal()).intensity for angle in angles]

    In [7]: plt.figure()

    @savefig plot_simple.png width=4in
    In [8]: plt.plot(angles, intensities);


It is also possible to plot the polarization of a Jones vector on
the  `Poincare sphere <https://en.wikipedia.org/wiki/Polarization_(waves)#Poincar%C3%A9_sphere>`_:

.. ipython::
    @savefig

    In [9]: import pyjones

    In [10]: from pyjones.polarizations import LinearHorizontal

    In [11]: from pyjones.opticalelements import HalfWavePlate, QuarterWavePlate

    In [12]: import numpy as np

    In [13]: ps = pyjones.polarizations.get_Poincare_sphere()

    @savefig plot_poincare.png width=8in
    In [109]: for angle in np.linspace(0, 360, 50):
       .....:     pol = QuarterWavePlate(angle) * LinearHorizontal()
       .....:     pol.plot(ps, color='r')

