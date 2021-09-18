import matplotlib.pyplot as plt
import numpy as np
from matplotlib.tri import Triangulation

n_angles = 4
n_radii = 3
min_radius = 12
radii = np.linspace(min_radius, 30, n_radii)
angles = np.linspace(0, 42 * np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles
x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()
triang = Triangulation(x, y)
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1)) < min_radius)

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
ax.autoscale_view('tight')

# plt.plot(x, y, 'o', color='y')
# plt.axhspan(ymin=26, ymax=60, color='green', alpha=0.1)
#
# plt.plot(x, y, 'o', color='y')
# plt.axhspan(ymin=-32, ymax=26, color='red', alpha=0.1)
#
# x = linspace(3, -3, 30)
# y = -x**2 + 34
# # ax.plot(x, y)
# ax.fill_between(x, y, color='red', alpha=0.1)

# change lw to show connection
ax.triplot(triang, 'ko--', lw=0, color="0.8", markeredgecolor="tab:red", markerfacecolor="tab:red", linestyle=':')

np.random.seed(98765)
x = np.arange(-40, 40)
y = np.random.randint(30, 60, 80)

ax.scatter(x, y, marker='s', color='green', alpha=0.5)

plt.plot(0, 30, 'P', markersize=8, markerfacecolor='blue',
         markeredgecolor='blue', markeredgewidth=2.0)

# plt.text(-5, 28, '.', fontsize=92)
plt.axis('off')
plt.show()
fig.savefig("try2.png", bbox_inches='tight')
