from scipy.linalg import expm, sinm, cosm
from matplotlib import pyplot
import networkx as nx
import pandas as pd
import numpy as np
import random as rand

def pp(mat):
    print(pd.DataFrame(mat))
    print()

def empty_mat(size):
    mat = []
    for y in range(size):
        row = []
        for x in range(size):
            row.append(0)
        mat.append(row)
    return mat

def gen_mat(size):
    graph = nx.erdos_renyi_graph(size, .25, seed=123, directed=False)

    adj = nx.adjacency_matrix(graph)
    adj = adj.tocoo()

    mat = empty_mat(size)
    
    for i,j,v in zip(adj.row, adj.col, adj.data):
        mat[i][j] = 1

    return mat

def gen_mats(cnt, size=0):
    mats = []
    if (size == 0):
        for i in range(cnt):
            mats.append(gen_mat(rand.randint(2, 10)))
    else:
        for i in range(cnt):
            mats.append(gen_mat(size))
    return mats

def plot_expms(mats):
    for mat in mats:
        plot_expm(mat)

def plot_expm(mat):
    np_mat = np.array(mat)
    identity = np.identity(len(np_mat))

    time = 0.0

    data = []
    for i in range(len(mat)):
        row = []
        for j in range(len(mat)):
            row.append([])
        data.append(row)

    times = []
    while time < 3*np.pi:
        postop = np.cos(time)*identity + 1j*np.sin(time)*np_mat
        for y in range(len(mat)):
            for x in range(len(mat)):
                data[y][x].append(abs(postop[y][x]))
        times.append(time)
        time += 0.01

    entry_num = 0
    for row in data:
        for entry in row:
            pyplot.plot(times, entry, label = str(entry_num))
            entry_num += 1

    pyplot.show()

if __name__ == '__main__':
    plot_expm(gen_mat(5))

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
