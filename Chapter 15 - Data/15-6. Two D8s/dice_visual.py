import plotly.express as px
from dice import Dice

dice1 = Dice(8)
dice2 = Dice(8)

results = []
for roll in range(10_000):
    result = dice1.roll() + dice2.roll()
    results.append(result)

frequencies = []
max_result = dice1.num_sides + dice2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

fig = px.bar(x=poss_results, y=frequencies)

fig.show()
