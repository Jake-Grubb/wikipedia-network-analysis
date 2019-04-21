#NOTES:
#Don't run shortest path unless it is a very small network (n < 5,000). It will take up too much RAM

import networkx as nx
import csv
import time
import matplotlib.pyplot as plt
import operator
from random import choice

graphyboi = nx.DiGraph()

#Simulate a random attack on a given graph
def randomAttack(graph, iterations):
	target = choice(list(graph.nodes()))
	i = 0
	histo = list()
	while(i < iterations):
		if(not nx.is_strongly_connected(graph)):
			graph = graph.subgraph(max(nx.strongly_connected_components(graph), key=len))
			graph = nx.DiGraph(graph)
		histo.append(nx.number_of_nodes(graph))
		target = choice(list(graph.nodes()))
		graph.remove_node(target)
		i+=1

	return histo

#Simulates an attack focused on the highest degree nodes
def degreeAttack(graph, iterations):
	target = sorted(graph.degree, key=lambda x: x[1], reverse=True)[0][0]
	i = 0
	histo = list()
	while(i < iterations):
		if(not nx.is_strongly_connected(graph)):
			graph = graph.subgraph(max(nx.strongly_connected_components(graph), key=len))
			graph = nx.DiGraph(graph)
		histo.append(nx.number_of_nodes(graph))
		target = sorted(graph.degree, key=lambda x: x[1], reverse=True)[0][0]
		graph.remove_node(target)
		i+=1

	return histo

def betweennessAttack(graph, iterations):
	target = sorted(nx.betweenness_centrality(graph).items(), key=operator.itemgetter(1), reverse=True)[0][0]
	i = 0
	histo = list()
	while(i < iterations):
		if(not nx.is_strongly_connected(graph)):
			graph = graph.subgraph(max(nx.strongly_connected_components(graph), key=len))
			graph = nx.DiGraph(graph)
		histo.append(nx.number_of_nodes(graph))
		target = sorted(nx.betweenness_centrality(graph).items(), key=operator.itemgetter(1), reverse=True)[0][0]
		graph.remove_node(target)
		i+=1

	return histo

if( __name__ == "__main__"):	
	start_time = time.time()

	#Make sure to change this file path to where ever the edge list csv is
	with open('../CN_shortening/5000n_edges.csv', 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			try:
				graphyboi.add_edge(row[0], row[1])
			except:
				print(str(row))

		print("Graphy Boi Added All His Edges in " + str(time.time() - start_time) + " seconds")

	#This section is for testing attack strategies on the network's largest component
	largest = graphyboi.subgraph(max(nx.strongly_connected_components(graphyboi), key=len))
	largestr = nx.DiGraph(largest)
	largestb = nx.DiGraph(largest)
	largestd = nx.DiGraph(largest)

	iterations = 30
	histo_r = randomAttack(largestr, iterations)
	histo_b = betweennessAttack(largestb, iterations)
	histo_d = degreeAttack(largestd, iterations)
	print(histo_r)
	print(histo_b)
	print(histo_d)