# BarabasiAlbert
# Language: Python
# Input: TXT
# Output: GML
# Tested with: PluMA 1.0, Python 3.6
# Dependency: Networkx 2.4

PluMA plugin that uses the Barabasi-Albert algorithm (Barabasi and Albert, 1999) to compute a random network of a user-specified number of nodes and edges (per node).

The node and edge count are entered into an input TXT file of tab-delineated keywords and values (the keywords are "nodes" and "edges", respectively).  Note for this case "edges" should be less than "nodes", as the algorithm iteratively attaches new nodes with a certain number of edges (this is how the parameter "edges" is used). 

Output will be the network, in the Graph Modeling Language (GML) format.
