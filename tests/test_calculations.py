from pyjones.polarizations import LinearHorizontal as LH
from pyjones.opticalelements import QuarterWavePlate, HalfWavePlate, PolarizerVertical, Polarizer
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

def test_HWP():
    angles = np.linspace(0, 360, 20)
    expected_intensities = [0.0, 0.37725725642960045, 0.93973687560324448, 0.83864078581287071,
                            0.22652592093878668, 0.027091379149682623, 0.54128967273616557,
                            0.99318065170136116, 0.70084771232648502, 0.10542974530180337,
                            0.10542974530180307, 0.7008477123264838, 0.99318065170136138,
                            0.54128967273616713, 0.027091379149682925, 0.22652592093878596,
                            0.83864078581287005, 0.9397368756032457, 0.37725725642960095,
                            2.3996156522589722e-31]
    intensities = [(PolarizerVertical() * HalfWavePlate(angle) * LH()).intensity for angle
                   in angles]
    assert intensities == expected_intensities

def test_basic_calculation():
    assert (PolarizerVertical()*Polarizer(45)*LH()).intensity == 0.25

#test_basic_calculation()