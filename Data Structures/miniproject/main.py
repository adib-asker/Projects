import sys
sys.setrecursionlimit(100000) #increase recursion limit otherwise the DFS() crashes due to error RuntimeError: maximum recursion depth exceeded

clock = 1 #global counter for pre and post visit procedure
nb_cc = 0

#Task 2 function
def InitGraph(filename, is_directed):
  """
  Input: filename with edges of the graph
  Output: a dictionary which represents graph as adjacency list, where dict.key is the vertex , dict.value is a list of outgoing vertices. 
  """
  graph = {}

  with open(filename, "r") as f:
    for line in f:  #read the file line by line
      if (line[0] != '#'): #skip the comment lines
        
        #determine the delimiter between 2 nodes
        if (',' in line):
          delimiter = ','
        elif(';' in line):
          delimiter = ';'
        elif('\t'): 
          delimiter = '\t'
        else:
          delimiter = ''
        edge = line.rstrip().split(delimiter)  #split line, the result is the list [u,v]

        if len(edge) == 1: #one node in line case
          graph[edge[0]] = []
          continue

        #add the edge u-->v into adjacency list
        if edge[0] not in graph:
          graph[edge[0]] = [edge[1]]
        else:
          graph[edge[0]].append(edge[1])
        
        #add also edge v --> u for undirected graph 
        if not is_directed:
          if edge[1] not in graph:
            graph[edge[1]] = [edge[0]]
          else:
            graph[edge[1]].append(edge[0])
  return graph
          
def GetUndirectedGraph(G):
  """
  Input   Directed graph G
  Output  Undirected graph G_undir obtained from G
  """
  G_undir = {}
  
  for node, childs in G.items():
    if node in G_undir:
      G_undir[node] = G_undir[node] + childs
    else:
      G_undir[node] = childs
      
    for v in childs:
      if v in G_undir:
        G_undir[v].append(node)
      else:
        G_undir[v] = [node]
  
  return G_undir

def CC_nodes_number(graph_stats):
  """
  Input:  Graph statistics dictionary
  Output: List with the number of nodes in each connected components
  """
  global nb_cc
  #init all components' id with 0
  nb_cc_arr = [0 for cc_id in range(nb_cc)]
  
  for node in graph_stats:
    cc_id = graph_stats[node][0]
    nb_cc_arr[cc_id] += 1
  
  return nb_cc_arr


def Explore(G, v, visited, cc, graph_stat):
  visited.add(v)

  graph_stat[v] = [cc]
  
  #previsit procedure
  global clock
  graph_stat[v].append(clock)
  clock += 1

  try:
    adj = G[v]
  except KeyError:
    #there is no outgoing edges from vertex v
    adj = []

  for node in adj: #for each child of the parent node node v
    if node not in visited:
      Explore(G, node, visited, cc, graph_stat)
  
  #postvisited(v)
  graph_stat[v].append(clock)
  clock += 1

def DFS(G):
  """
  Depth first search implementation
  Input:   graph G as am adjacency list
  Output:  The graph statistic dictionary graph_stat, where dict.key is a node of the graph and dict.value is list [pos1, pos2, pos3], where
            pos1 -  node's connected component id
            pos2 -  previsit time
            pos3 -  postvisit time

  """
  graph_stat = {}   #dictionary to store graph's statistic
  cc = -1           #connected componets counter
  global nb_cc
  visited = set()   #stores visited nodes
  
  for node in G:
    if node not in visited:
      cc += 1
      Explore(G, node, visited, cc, graph_stat)
  
  nb_cc = cc + 1
  
  return graph_stat
  
def FindSmallerComponents(G, is_directed, min_node_numb):
  """
  Task4:
  Search all connected components of the graph which are fake.
  Node's connected component is said to be fake if the total number
  of nodes with the same id(same connected component number) is  less then the min_node_numb argument difined by user.
  """
  fake_node = []
  
  if is_directed:
    #need to make an undirected graph from directed one before finding the connected components
    G_undir = GetUndirectedGraph(G)
    graph_data = DFS(G_undir)
  else:
    graph_data = DFS(G)

  cc_stat = CC_nodes_number(graph_data)

  fake_cc_id = set() #set of conected components ids

  for i in range(len(cc_stat)):
    if cc_stat[i] <= min_node_numb:
      fake_cc_id.add(i)
  
  for node in graph_data:
    cc_id = graph_data[node][0]
    if cc_id in fake_cc_id:
      fake_node.append(node)
  
  return(fake_node)

def GetReversedGraph(G):
  """
  Input:  Directed graph G as dictionary data structure
  Output: Revervsed graph G_reverse as dict
  """ 

  G_reverse = {}

  for parent, childs in G.items():
    for child in childs:
      if child in G_reverse:
        G_reverse[child].append(parent)
      else:
        G_reverse[child] = [parent]
  
  return G_reverse

def FindStronglyConectedComponents(G):
  """
  Fucntion finds all connected components of the directed graph G.
    Input:  Directed graph G
    Output: List of strongly connected components of the graph G
  """

  G_graph_data = DFS(G) #Step 1
  G_R = GetReversedGraph(G)  #Step 2
  
  G_R_sorted = {}
  #sort graph nodes in decreasing order of post numbers 
  for key, val in sorted(G_graph_data.items(), key = lambda item: (item[1][2], item[0]), reverse = True):
    try:
      G_R_sorted[key] = G_R[key]
    except KeyError:
      continue

  G_R_graph_data = DFS(G_R_sorted)#Step 3

  strongly_cc = {}
  for node in G_R_graph_data:
    node_cc = G_R_graph_data[node][0]
    if node_cc in strongly_cc:
      strongly_cc[node_cc].append(node)
    else:
      strongly_cc[node_cc] = [node]
  
  return(list(strongly_cc.values()))
  

#Test
test = "test1_undirected"
test2 = "test2_directed"
filename1 = "directed/soc-Epinions1.txt"  #initial directed graph file
filename2 = "undirected/deezer_clean_data/HR_edges.csv"
is_graph_directed = True
G = {} # graph G(V,E)                            
G = InitGraph(filename1, True)
#DFS(G)
print("Fake nodes:\n",FindSmallerComponents(G, True, 1000))

scc_list = FindStronglyConectedComponents(G)
print("Strongly connected components:\n")
for scc in scc_list:
  if(len(scc)> 1):
    print(scc)
#test1 = {'A':['B','E'], 'B':['A'], 'E':['J', 'I'], 'J':['E','I'], 'I':['E','J'], 'F':[]}
#DFS(test1)
