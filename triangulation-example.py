import matplotlib.pyplot as plt
from matplotlib.tri import Triangulation
import numpy as np

# Create a Triangulation.
n_angles = 15
n_radii = 3
min_radius = 0.1
radii = np.linspace(min_radius, 0.5, n_radii)
angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=True)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles
x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()
triang = Triangulation(x, y)
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1)) < min_radius)

cm = 1 / 2.54  # centimeters in inches
plt.figure(figsize=(20 * cm, 20 * cm))
fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
ax.triplot(triang, 'ko--', lw=1, zorder=3, label='inner', color="gray")
# ax.plot(x, y, 'ro-', lw=3, ms=6, zorder=1, label='edge')
ax.triplot(triang, 'ko--', lw=1, ms=8, color="red")
plt.axis('off')

plt.show()
plt.savefig("test.png", bbox_inches='tight')















