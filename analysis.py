import networkx
import csv
import time

#Load the file ./edges.csv using csv module into a python list
start_time = time.time()
with open('../../Documents/edges.csv', 'r') as file:
	reader = csv.reader(file)
	print("Reader Made in " + str(time.time() - start_time) + " seconds")
	edgeList = list(reader)
	print("EdgeList Loaded in " + str(time.time() - start_time) + " seconds")
#Load the python list of edges into a networkx graph
graphyboi = networkx.DiGraph()
print("Graphy Boi Made in " + str(time.time() - start_time) + " seconds")
#graphyboi.add_edges_from(edgeList)
for edge in edgeList:
	try:
		graphyboi.add_edge(edge[0], edge[1])
	except:
		print(str(edge))
print("Graphy Boi Added All His Edges in " + str(time.time() - start_time) + " seconds")
