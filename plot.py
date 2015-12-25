from pprint import pprint
from bokeh.models import HoverTool
from collections import defaultdict
from bokeh.plotting import figure, output_file, show

steps = set()
results = defaultdict(list)
colors = ['red', 'blue', 'green', 'purple', 'orange', 'black']

lang_map = {'py': 'Python', 'rb': 'Ruby'}

for i, line in enumerate(file('results.csv').readlines()):

    if i == 0:
        continue

    parts = line.split(",")
    short_lang = parts[0].strip().replace('fib', '').replace('.', '').replace('-', '')
    lang = lang_map.get(short_lang, short_lang).capitalize()
    real_t = float(parts[3].strip())
    results[lang].append(real_t)
    step = int(parts[1].strip())
    steps.add(step)

ordered_steps = sorted(list(steps))
output_file("benchmark.html", title="Fibonacci Bench")
p = figure(title="Fibonacci Bench", x_axis_label='N', y_axis_label='Seconds', width=1400, height=700)

for lang, series in results.items():
    p.line(ordered_steps, results[lang], legend="%s" % lang, line_width=3, line_color=colors.pop())

p.legend.orientation = 'top_left'
show(p)
