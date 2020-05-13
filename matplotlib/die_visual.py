from die import Die
import pygal

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(10000):
    results.append(die_1.roll() + die_2.roll())

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
x_labels = []
for value in range(2, max_result+1):
    x_labels.append(value)
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果可视化
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = x_labels
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6+D6', frequencies)
hist.render_to_file('die_visual.svg')
