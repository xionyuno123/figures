import os
import optparse
import sys
import subprocess
import signal
import time

import numpy as np
import matplotlib.pyplot as plt
import xlrd

column = {
	1.0: 2,
	0.9: 3,
	0.8: 4,
	0.7: 5,
	0.6: 6,
	0.5: 7,
	0.4: 8,
	0.3: 9,
	0.2: 10,
	0.1: 11,
	0: 12,
}

types = {
	"AC": 's-.',
	"Random": 'o--',
	"DBH": 'D--',
	"HDRF": '^:',
	"LDG": 'H--',
	"FENNEL": '>--'
}

fontsize = 20

def read_table(file_name, p):
	edges = list()
	nodes = list()

	data = xlrd.open_workbook(file_name)
	table = data.sheets()[0]
	for alpha in column:
		edges.append(int(table.cell_value(p+1, column[alpha]-1)))
		nodes.append(float(table.cell_value(p+19, column[alpha])))

	print("edges=", edges)
	print("nodes=", nodes)
	return edges, nodes

def draw_edges(edges, p):
	plt.style.use('ggplot')
	fig,ax1 = plt.subplots()
	plt.title("Fat-Tree, k=8, P="+str(p), fontsize=fontsize)
	partition_numbers = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]
	ax1.plot(partition_numbers, edges, 's-.', markersize=8)
	plt.xticks(partition_numbers, partition_numbers)
	ax1.invert_xaxis()

	ax1.set_ylabel('Edge Cut', fontsize=fontsize, style='normal', color='black')
	ax1.set_xlabel('α', fontsize=fontsize, style="normal", color='black')

	legend = ax1.legend(loc='lower right', shadow=False)

	for tl in ax1.get_xticklabels():
		tl.set_fontsize(16)
		tl.set_fontstyle('normal')
	for tl in ax1.get_yticklabels():
		tl.set_fontsize(16)
		tl.set_fontstyle('normal')

	#plt.savefig("k="+str(k)+"-edge.svg", bbox_inches='tight', pad_inches=0)
	plt.show()

def draw_nodes(edges, p):
	plt.style.use('ggplot')
	fig,ax1 = plt.subplots()
	plt.title("Fat-Tree, k=8, P="+str(p), fontsize=fontsize)
	partition_numbers = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]
	ax1.plot(partition_numbers, edges, 's-.', markersize=8)
	plt.xticks(partition_numbers, partition_numbers)
	ax1.invert_xaxis()

	ax1.set_ylabel('Balance Measure', fontsize=fontsize, style='normal', color='black')
	ax1.set_xlabel('α', fontsize=fontsize, style="normal", color='black')

	legend = ax1.legend(loc='lower right', shadow=False)

	for tl in ax1.get_xticklabels():
		tl.set_fontsize(16)
		tl.set_fontstyle('normal')
	for tl in ax1.get_yticklabels():
		tl.set_fontsize(16)
		tl.set_fontstyle('normal')

	#plt.savefig("k="+str(k)+"-edge.svg", bbox_inches='tight', pad_inches=0)
	
	plt.show()


def main():
	edges3, nodes3 = read_table("C:/Users/Administrator/Desktop/fne-paper/figures-source/test/k=8.xlsx", 3)
	edges5, nodes5 = read_table("C:/Users/Administrator/Desktop/fne-paper/figures-source/test/k=8.xlsx", 5)
	edges7, nodes7 = read_table("C:/Users/Administrator/Desktop/fne-paper/figures-source/test/k=8.xlsx", 7)
	edges9, nodes9 = read_table("C:/Users/Administrator/Desktop/fne-paper/figures-source/test/k=8.xlsx", 9)


	# 根据需要画node还是edge类型调用
	draw_edges(edges7, 7)
	#draw_nodes(nodes10, 15)


if __name__ == "__main__" :
	main()