
import plotly.figure_factory as ff 
import csv
import pandas as pd
import statistics 
import plotly.graph_objects as go


df = pd.read_csv("G:/Whitehatjr/Bell Curve/Data.csv")
data = df["Math_score"].tolist()

# code to show the plot of raw data
fig = ff.create_distplot([data], ["Math.score"], show_hist=False)


mean = statistics.mean(data)
stdev = statistics.stdev(data)

print(mean, stdev)

fstdv_start, fstdev_end = mean-stdev, mean+stdev
Sstdv_start, Sstdev_end = mean-2*stdev, mean+2*stdev
tstdv_start, tstdev_end = mean-3*stdev, mean+3*stdev
fig.add_trace(go.scatter( x = [mean, mean], y = [0, 0.17], name = 'mean'))
fig.add_trace(go.scatter( x = [fstdv_start, fstdev_end], y = [0, 0.17], name = 'mean'))
fig.add_trace(go.scatter( x = [Sstdv_start, Sstdev_end], y = [0, 0.17], name = 'mean'))
fig.add_trace(go.scatter( x = [tstdv_start, tstdev_end], y = [0, 0.17], name = 'mean'))
fig.add_trace(go.scatter( x = [fstdev_end, fstdv_start], y = [0, 0.17], name = 'mean'))
fig.add_trace(go.scatter( x = [Sstdev_end, Sstdv_start], y = [0, 0.17], name = 'mean'))
fig.add_trace(go.scatter( x = [tstdev_end, tstdv_start], y = [0, 0.17], name = 'mean'))
fig.show()
'''df = pd.read_csv("G:/Whitehatjr/Bell Curve/Data3.csv")
data = df["Math_score"].tolist()

# code to show the plot of raw data
fig = ff.create_distplot([data], ["Math.score"], show_hist=False)
fig.show()

sample_1 = statistics.mean(data)
sample_2 = statistics.stdev(data)

print(sample_1, sample_2)'''





