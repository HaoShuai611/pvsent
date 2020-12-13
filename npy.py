import numpy as np
import os
import tqdm
from plyfile import PlyData


for i in range(1229):

    test = np.load("/home/sh/Public/clean-pvnet-master/data/custom/pose1/pose%d.npy"%(i))
    test = np.delete(test,3,axis = 0)
    np.save("/home/sh/Public/clean-pvnet-master/data/custom/pose/pose%d.npy"%(i), test)
    print(test)
