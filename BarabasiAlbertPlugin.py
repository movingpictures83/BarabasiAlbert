import networkx

class BarabasiAlbertPlugin:
	def input(self, filename):
                print("HI")
                inputfile = open(filename, 'r')
                self.parameters = dict()
                for line in inputfile:
                   contents = line.split('\t')
                   self.parameters[contents[0]] = int(contents[1])


	def run(self):
                self.G = networkx.barabasi_albert_graph(self.parameters['nodes'],
                                                       self.parameters['edges'],
                                                       seed=1234)

	def output(self, filename):
		networkx.write_gml(self.G, filename)
