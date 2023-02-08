import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:

    rw = RandomWalk(50_000)
    rw.fill_walk()
    fig, ax = plt.subplots(figsize=(15, 9))

    plt.style.use('classic')
    point_numbers = range(rw.num_points)

    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=1)
    ax.scatter(0, 0,
               c='green', edgecolors='none', s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1],
               c='red', edgecolors='none',  s=50)
    ax.set_aspect('equal')

    # Hide axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk?(y/n)")
    if keep_running == 'n':
        break
