from scipy.linalg import expm, sinm, cosm
from matplotlib import pyplot
import networkx as nx
import pandas as pd
import numpy as np
import random as rand

def pp(mat):
    print(pd.DataFrame(mat))

def gen_mat(size):
    graph = nx.gnp_random_graph(size, .1)

    adj = nx.adjacency_matrix(graph)
    adj = adj.tocoo()
    
    newadj = [[0]*size]*size
    pp(newadj)
    for i,j,v in zip(adj.row, adj.col,adj.data):
        print(newadj[j][i])
        newadj[j][i] = 1
        print(i,j,v)
        pp(newadj)

def gen_mats(cnt, size=0):
    mats = []
    if (size == 0):
        for i in range(cnt):
            mats.append(gen_mat(rand.randint(2, 10)))
    else:
        for i in range(cnt):
            mats.append(gen_mat(size))
    return mats

gen_mat(10)

'''
test = np.mat('[0 1;1 0]')
test = np.array([
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0]
])
testI = np.identity(len(test))

time = 0.0

data = []
while time < 3*np.pi:
  postop = np.cos(time)*testI + 1j*np.sin(time)*test
  data.append([1, abs(postop[0][0])])
  time += 0.01

df = pd.DataFrame(data, columns = ['One', 'Value'])
df.plot()
pyplot.xlim([0, np.pi*4])
pyplot.show()
'''
