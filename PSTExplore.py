from scipy.linalg import expm, sinm, cosm
from matplotlib import pyplot
import pandas as pd
import numpy as np

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

