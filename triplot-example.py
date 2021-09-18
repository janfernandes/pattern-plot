import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

fig, (ax1, ax2) = plt.subplots(ncols=2)
ax1.set_aspect('equal')
ax2.set_aspect('equal')

##setting up basic shape
phi = np.linspace(0, 2 * np.pi, 20)
r = 1 + 2 * np.sin(phi) ** 2
x = np.cos(phi) * r
y = np.sin(phi) * r
ax1.plot(x, y, 'ro-', lw=3, ms=6, zorder=1, label='edge')
ax2.plot(x, y, 'ro-', lw=3, ms=6, zorder=1)

# ##original triangulation
triang1 = tri.Triangulation(x, y)
ax1.triplot(triang1, 'ko--', lw=1, ms=4, zorder=2, label='all')

# ##masking
# outline = sPolygon(zip(x, y))
# mask = [
#     not outline.contains(sPolygon(zip(x[tri], y[tri])))
#     for tri in triang1.get_masked_triangles()
# ]
# triang1.set_mask(mask)
# ax1.triplot(triang1, 'b-', lw=1, zorder=3, label='inner')
#
# ##adding more points
# x_extra = np.random.rand(30) * (x.max() - x.min()) + x.min()
# y_extra = np.random.rand(30) * (y.max() - y.min()) + y.min()
#
# x = np.concatenate([x, x_extra])
# y = np.concatenate([y, y_extra])
#
# triang2 = tri.Triangulation(x, y)
# ax2.triplot(triang2, 'ko--', lw=1, ms=4, zorder=2)
#
# ##masking
# mask = [
#     not outline.contains(sPolygon(zip(x[tri], y[tri])))
#     for tri in triang2.get_masked_triangles()
# ]
# triang2.set_mask(mask)
# ax2.triplot(triang2, 'b-', lw=1, zorder=3)

fig.legend()
plt.show()