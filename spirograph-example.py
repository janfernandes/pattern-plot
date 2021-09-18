import matplotlib.pyplot as plt
from numpy import pi, exp, real, imag, linspace


def spiro(t, r1, r2, r3):
    """
    Create Spirograph curves made by one circle of radius r2 rolling
    around the inside (or outside) of another of radius r1.  The pen
    is a distance r3 from the center of the first circle.
    """
    return r3 * exp(1j * t * (r1 + r2) / r2) + (r1 + r2) * exp(1j * t)


def circle(t, r):
    return r * exp(1j * t)


r1 = 1.0
r2 = 52.0 / 96.0
r3 = 42.0 / 96.0

ncycle = 13  # LCM(r1,r2)/r2

t = linspace(0, ncycle * 2 * pi, 1000)
plt.plot(real(spiro(t, r1, r2, r3)), imag(spiro(t, r1, r2, r3)))
plt.plot(real(circle(t, r1)), imag(circle(t, r1)))

fig = plt.gcf()
fig.gca().set_aspect('equal')
plt.show()
fig.savefig("triplot.png", bbox_inches='tight')
