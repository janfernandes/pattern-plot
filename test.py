import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

n_angles = 40
n_radii = 4
min_radius = 40
radii = np.linspace(min_radius, 0.1, n_radii)

angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles

x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()

triang = tri.Triangulation(x, y)

triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)

fig, ax = plt.subplots()
ax.autoscale_view('tight')
x = np.arange(100)
y = np.random.randint(45, 55, 100)

ax.scatter(x, y, color='red', alpha=0.5)

ax.set_aspect('equal')
ax.triplot(triang, 'g:', lw=1, marker='s', markersize=4, markerfacecolor='green', alpha=1)
ax.axis(False)

plt.show()
