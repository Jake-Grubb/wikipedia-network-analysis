import networkx as nx
import csv
import time

graphyboi = nx.DiGraph()
start_time = time.time()

with open('../../Documents/edges.csv', 'r') as file:
	reader = csv.reader(file)
	for row in reader:
		try:
			graphyboi.add_edge(row[0], row[1])
		except:
			print(str(row))

print("Graphy Boi Added All His Edges in " + str(time.time() - start_time) + " seconds")