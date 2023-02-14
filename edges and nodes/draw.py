import os
import optparse
import sys
import subprocess
import signal
import time

import numpy as np
import matplotlib.pyplot as plt
import xlrd

method_colomns = {
	"AC": 6,
	#"Random": 12,
	"DBH": 13,
	"HDRF": 14,
	"LDG": 15,
	"FENNEL": 16
}

types = {
	"AC": 's-.',
	#"Random": 'o--',
	"DBH": 'D--',
	"HDRF": '^:',
	"LDG": 'H--',
	"FENNEL": '>--'
}


def read_table(file_name, partition_numbers):
	edges = {}
	nodes = {}

	for method in method_colomns:
		edges[method] = list()
		nodes[method] = list()

	data = xlrd.open_workbook(file_name)
	table = data.sheets()[0]
	for p in range(partition_numbers):
		for method in method_colomns:
			edges[method].append(int(table.cell_value(p+3, method_colomns[method])))
			nodes[method].append(float(table.cell_value(p+22, method_colomns[method])))

	return edges, nodes

def draw_edges(edges, k):
	plt.style.use('ggplot')
	fig,ax1 = plt.subplots()
	fig = plt.figure(1)
	#plt.title("Fat-Tree, k="+str(k), fontsize=20)
	plt.title("Full-Tree, n=4, depth=4", fontsize=20)

	partition_numbers = []
	for i in range(len(edges["AC"])):
		partition_numbers.append(i+2)

	print(partition_numbers)

	for method in method_colomns:
		if method == "AC":
			ax1.plot(partition_numbers, edges[method], types[method], label=method, markersize=12)
		else:
			ax1.plot(partition_numbers, edges[method], types[method], label=method, markersize=8)
		#plt.xticks(partition_numbers, edges[method])

	ax1.set_ylabel('Edge Cut', fontsize=20, style='normal', color='black')
	ax1.set_xlabel('Partition Number', fontsize=20, style="normal", color='black')

	legend = ax1.legend(loc='center right', shadow=False, ncol=3)

	for tl in ax1.get_xticklabels():
		tl.set_fontsize(16)
		tl.set_fontstyle('normal')
	for tl in ax1.get_yticklabels():
		tl.set_fontsize(16)
		tl.set_fontstyle('normal')

	#plt.savefig("k="+str(k)+"-edge.svg", bbox_inches='tight', pad_inches=0)
	plt.show()

def draw_nodes(nodes, k):
	plt.style.use('ggplot')
	fig,ax1 = plt.subplots()
	fig = plt.figure(1)
	#plt.title("Fat-Tree, k="+str(k), fontsize=20)
	plt.title("Full-Tree, n=4, depth=4", fontsize=20)

	partition_numbers = []
	for i in range(len(nodes["AC"])):
		partition_numbers.append(i+2)

	print(partition_numbers)

	for method in method_colomns:
		if method == "AC":
			ax1.plot(partition_numbers, nodes[method], types[method], label=method, markersize=12)
		else:
			ax1.plot(partition_numbers, nodes[method], types[method], label=method, markersize=8)
		#plt.xticks(partition_numbers, edges[method])

	ax1.set_ylabel('Balance Measure', fontsize=20, style='normal', color='black')
	ax1.set_xlabel('Partition Number', fontsize=20, style="normal", color='black')

	legend = ax1.legend(loc='upper left', shadow=False, ncol=3)

	for tl in ax1.get_xticklabels():
		tl.set_fontsize(16)
		tl.set_fontstyle('normal')
	for tl in ax1.get_yticklabels():
		tl.set_fontsize(16)
		tl.set_fontstyle('normal')

	#plt.savefig("k="+str(k)+"-node.svg", bbox_inches='tight', pad_inches=0)
	plt.show()

def main():
	# lengths = {
	# 	4: 5, 6: 8, 8: 10, 10: 15
	# }
	# for k in [4, 6, 8, 10]:
	# 	edges, nodes = read_table("k="+str(k)+".xlsx", lengths[k])
	# 	draw_edges(edges, k)
	# 	draw_nodes(nodes, k)
	edges4, nodes4 = read_table("C:/Users/Administrator/Desktop/fne-paper/figures-source/edges and nodes/k=4.xlsx", 5)
	edges6, nodes6 = read_table("C:/Users/Administrator/Desktop/fne-paper/figures-source/edges and nodes/k=6.xlsx", 8)
	edges8, nodes8 = read_table("C:/Users/Administrator/Desktop/fne-paper/figures-source/edges and nodes/k=8.xlsx", 10)
	edges10, nodes10 = read_table("C:/Users/Administrator/Desktop/fne-paper/figures-source/edges and nodes/k=10.xlsx", 15)
	edges_fulltree, nodes_fulltree = read_table("C:/Users/Administrator/Desktop/fne-paper/figures-source/edges and nodes/fulltree.xlsx", 15)

	# 根据需要画node还是edge类型调用
	draw_edges(edges_fulltree, 10)


if __name__ == "__main__" :
	main()