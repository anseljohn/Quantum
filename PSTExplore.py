from scipy.linalg import expm, sinm, cosm
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
            row.append(0)
        mat.append(row)
    return mat

'''
Return a random adjacency matrix
'''
def gen_mat(size):
    graph = nx.erdos_renyi_graph(size, .25, directed=False)

    adj = nx.adjacency_matrix(graph)
    adj = adj.tocoo()

    mat = empty_mat(size)
    
    for i,j,v in zip(adj.row, adj.col, adj.data):
        mat[i][j] = 1

    return mat

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
            clos_row.append(round(min_val, 3))

        closest.append(clos_row)
    
    return closest

'''
Returns the time vector and...
the NxN matrix with each entry being a vector containing the entry's matrix
exponential values over some period of time.
'''
def expm_entries(mat):
    np_mat = np.array(mat)
    identity = np.identity(len(np_mat))

    time = 0.0
    data = []

    # Generate an NxNxtime matrix for recording each entry change
    # over time
    for i in range(len(mat)):
        row = []
        for j in range(len(mat)):
            row.append([])
        data.append(row)

    times = []  # The time vector
    while time < 3*np.pi: # Record matrix exponential just to 3pi
        postop = np.cos(time)*identity + 1j*np.sin(time)*np_mat #Calcuate matrix exponential for current time
        for y in range(len(mat)):
            for x in range(len(mat)):
                data[y][x].append(abs(postop[y][x])) 
        times.append(time)
        time += 0.01

    return [times, data]

'''
Plot a single matrix exponential over time
'''
def plot_expm(coupled):
    times = coupled[0]
    data = coupled[1]
    entry_num = 0
    for y in range(len(mat)):
        for x in range(len(mat)):
            if (x != y):
                pyplot.plot(times, data[y][x], label=str(entry_num))
                entry_num += 1

    pyplot.legend(loc='upper right')
    pyplot.show()

    pp(mat)
    pp(closest_to_one(expm_entries(mat)[1]))

if __name__ == '__main__':
    mat = gen_mat(5)                            # Generate a random matrix
    series = expm_entries(mat)                  # Get the times and matrix exponentials
    pp(mat)                                     # Print the adjacency matrix
    pp(closest_to_one(expm_entries(mat)[1]))    # Show how close each entry got to one
    plot_expm(series)                           # Plot the exponential values over time
