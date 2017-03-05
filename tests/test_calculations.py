from pyjones.polarizations import LinearHorizontal as LH
from pyjones.opticalelements import QuarterWavePlate, PolarizerVertical
import numpy as np
import matplotlib.pyplot as plt

def test_QWP():
    angles = np.linspace(0, 360, 20)
    expected_intensities = [0.0, 0.18862862821480014, 0.46986843780162207, 0.41932039290643552,
                            0.11326296046939333, 0.013545689574841311, 0.27064483636808295,
                            0.49659032585068064, 0.35042385616324229, 0.052714872650901683,
                            0.052714872650901523, 0.35042385616324179, 0.49659032585068064,
                            0.27064483636808351, 0.013545689574841466, 0.11326296046939295,
                            0.41932039290643497, 0.46986843780162302, 0.18862862821480045,
                            1.1998078261294861e-31]
    intensities = [(PolarizerVertical() * QuarterWavePlate(angle) * LH()).intensity for angle
                   in angles]
    assert intensities == expected_intensities
