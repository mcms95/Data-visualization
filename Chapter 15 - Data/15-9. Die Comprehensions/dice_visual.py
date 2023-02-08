import plotly.express as px
from dice import Dice

dice1 = Dice()
dice2 = Dice()


results = list(dice1.roll() + dice2.roll() for roll in range(10_000))

max_result = dice1.num_sides * dice2.num_sides
poss_results = range(1, max_result+1)
frequencies = list(results.count(value) for value in poss_results)

title = "Rolling"
labels = {'x': 'Possible results', 'y': 'frequencies'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

fig.show()
