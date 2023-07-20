import numpy as np
import sys
from scipy.sparse import load_npz

data = load_npz("n_is_5.npz")
np.save("random.labels.npy", data)
data = data.toarray()
# print(data)

np.set_printoptions(threshold=np.inf)
sys.stdout=open("random.edges.csv", "w")
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i][j] == 1:
            print(str(i) + "," + str(j))
sys.stdout.close()

