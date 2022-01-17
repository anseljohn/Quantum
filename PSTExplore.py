from scipy.linalg import expm, eig
from matplotlib import pyplot
import networkx as nx
import pandas as pd
import numpy as np
import random as rand

'''
Print out a pretty matrix
'''
def pp(mat):
    print(pd.DataFrame(mat))
    print()

'''
Return an empty matrix of specified size
'''
def empty_mat(size):
    mat = []
    for y in range(size):
        row = []
        for x in range(size):
            row.append([])
        mat.append(row)
    return mat

def zero_mat(size):
    mat = []
    for y in range(size):
        row = []
        for x in range(size):
            row.append(0)
        mat.append(row)
    return mat

'''
Return a random adjacency matrix
'''
def gen_mat(size):
    graph = nx.erdos_renyi_graph(size, .25, directed=True)

    adj = nx.adjacency_matrix(graph)
    return adj.todense()

'''
Get multiple random adjacency matrices
'''
def gen_mats(cnt, size=0):
    mats = []
    if (size == 0):
        for i in range(cnt):
            mats.append(gen_mat(rand.randint(2, 10)))
    else:
        for i in range(cnt):
            mats.append(gen_mat(size))
    return mats

'''
Plot multiple adjacency matrices when passed through
the matrix expontential
'''
def plot_expms(mats):
    for mat in mats:
        plot_expm(expm_entries(mat))

'''
Create an NxN matrix showing how close values got to one
i.e. If an entry in the returned matrix is 0, that means it reached 0
'''
def closest_to_one(mat):
    closest = [] # NxN matrix with each entry being how close it got to 1
    for row in mat:
        clos_row = []
        for entry in row:
            min_val = 1-entry[0]
            for data in entry:
                if 1-data < min_val:
                    min_val = 1-data
            clos_row.append(min_val)

        closest.append(clos_row)
    
    return closest

def expm_entries(mat):
    time = 0.0
    times = []
    series = empty_mat(len(mat))
    
    while time < 3*np.pi:
        u = np.abs(expm(-1j*mat*time))
        for y in range(len(mat)):
            for x in range(len(mat)):
                series[y][x].append(u[y][x])

        times.append(time)
        time += 0.01

    return [times, series]

def plot_expm(coupled, legend):
    times = coupled[0]
    series = coupled[1]

    entry_num = 0
    for y in range(len(mat)):
        for x in range(len(mat)):
            if (x != y):
                pyplot.plot(times, series[y][x], label=str(entry_num))
                entry_num += 1
    if legend:
        pyplot.legend(loc='upper left')
    pyplot.show()

if __name__ == '__main__':
    mat = gen_mat(5)                            # Generate a random matrix
    mat = np.matrix([[0, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]])
    mat = np.matrix([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,1,1],[0,1,0,0,0],[0,1,1,0,0]])
    print(eig(mat))
    pp(mat)                                     # Print the adjacency matrix
    series = expm_entries(mat)                  # Generate the expm series
    pp(closest_to_one(series[1]))               # Show how close each entry got to one
    plot_expm(series, True)                     # Plot the exponential values over time
