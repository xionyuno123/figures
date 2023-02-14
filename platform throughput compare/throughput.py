#!/usr/bin/env python2.7
import os
import optparse
import sys
import subprocess
import signal
import time
import random

import numpy as np
import matplotlib.pyplot as plt

def draw_on_chain_cost(cost):
	plt.style.use('ggplot')
	fig,ax1 = plt.subplots()
	fig = plt.figure(1)
	plt.title("Fat-Tree, K=6", fontsize=20)

	x = np.arange(len(cost))
	width = 0.6

	ax1.bar(x, cost, width, color=list(plt.rcParams['axes.prop_cycle'])[1]['color'])

	labels= ["Mocknet", "Mininet", "ContainerNet", "DistriNet"]
	plt.xticks(x, labels, rotation=-10)

	ax1.set_ylabel('Bi-section Throughput '+r'(Gb/s)', fontsize=20, style='normal')
	# ax1.set_xlabel('# of participants', fontsize=15, style="normal", color='black')

	for tl in ax1.get_xticklabels():
		tl.set_fontsize(16)
		tl.set_fontstyle('normal')
	for tl in ax1.get_yticklabels():
		tl.set_fontsize(16)
		tl.set_fontstyle('normal')


	plt.savefig("throughput k=6.pdf", bbox_inches='tight', pad_inches=0)
	plt.show()

def main():
	# left to right: deployment, init, join, stopReg, stopMission
	on_chain_cost = [71.1, 1.58, 1.1, 3.4]
	draw_on_chain_cost(on_chain_cost)

if __name__ == "__main__" :
	main()