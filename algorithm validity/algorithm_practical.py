import os
import optparse
import sys
import subprocess
import signal
import time

import numpy as np
import matplotlib.pyplot as plt

data_6 = {
	"AC": [71.1, 96.9],
	"DBH": [35.7, 81],
	"HDRF": [45.3, 83.2],
	"LDG": [32.2, 68.5],
	"FENNEL": [62.6, 96.6]
}

data_4 = {
	"AC": [42.1, 54.4],
	"DBH": [41.8, 60.6],
	"HDRF": [40.9, 53.3],
	"LDG": [42.2, 50],
	"FENNEL": [41.9, 53.5]
}


colors = {
	"AC": '#F1D77E',
	"DBH": '#B1CE46',
	"HDRF": '#9394E7',
	"LDG": '#5F97D2',
	"FENNEL": '#D76364'
}

hatchs = {
	"AC": '\\\\\\',
	"DBH": 'xxx',
	"HDRF": '...',
	"LDG": '///',
	"FENNEL": '+++'
}

bar_width = 0.06
blank = 0.01
throughput_x = {}
bandwidth_x = {}
throughput_start = 0
bandwidth_start = 0.6
count = 0
x_label = []
for method in data_4:
	throughput_x[method] = throughput_start + count*bar_width + blank
	count += 1
	if count == 2:
		x_label.append(throughput_start + count*bar_width + blank)

count = 0
for method in data_4:
	bandwidth_x[method] = bandwidth_start + count*bar_width + blank
	count += 1
	if count == 2:
		x_label.append(bandwidth_start + count*bar_width + blank)



labels = ["Throughput", "Physical Bandwidth Consumption"]

def main():
	plt.style.use('ggplot')
	fig,ax1 = plt.subplots()
	fig = plt.figure(1)
	plt.title("K = 4", size=20)
	plt.xticks(x_label, labels)
	plots = []

	for method in colors:
		bar1 = plt.bar(
		throughput_x[method], height=data_4[method][0], 
		width=bar_width, 
		color=[colors[method]], 
		label=method,
		hatch=hatchs[method]
	)
		plots.append(bar1)
		bar2 = plt.bar(
		bandwidth_x[method], height=data_4[method][1],
		width=bar_width, 
		color=[colors[method]], 
		label=method,
		hatch=hatchs[method]
	)
	
	for tl in ax1.get_xticklabels():
		tl.set_fontsize(12)
		tl.set_fontstyle('normal')
	ax1.legend(handles=plots, loc='upper left', shadow=False, ncol=3)
	ax1.set_ylabel('Speed (Gb/s)', fontsize=20, style='normal', color='black')


	plt.show()


if __name__ == "__main__" :
	main()