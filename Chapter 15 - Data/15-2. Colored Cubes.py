# Apply a colormap to your cubes plot

import matplotlib.pyplot as plt

x = range(1, 1000)
y = [n**3 for n in x]

fig, ax = plt.subplots()

ax.set_title(" Cubic numbers", fontsize=20)
ax.set_xlabel("numbers", fontsize=12)
ax.set_ylabel("cubes", fontsize=12)

ax.axis([0, 1100, 0, 1_000_000_000])
ax.scatter(x, y, c=y, cmap=plt.cm.Blues)
ax.ticklabel_format(style='plain')
plt.show()
