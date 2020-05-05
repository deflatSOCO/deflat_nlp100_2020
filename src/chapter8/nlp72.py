import os
import sys
import re
import pandas as pd
import numpy as np

import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torch.utils.data


from typing import List, Tuple


THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter8")

def nlp_72():

    X_train = np.load(os.path.join(result_dir_path, "train_X.npy")).astype(np.float32)
    y_train = np.load(os.path.join(result_dir_path, "train_y.npy")).astype(np.int64)
    X_train = torch.from_numpy(X_train)
    y_train = torch.from_numpy(y_train)
    net = nn.Sequential(
        nn.Linear(300,4,bias=False),
        nn.Softmax(1)
    )
    loss = nn.CrossEntropyLoss()
    print("y1:")
    y_pred = net.forward(X_train[0:1,:])
    print(loss(y_pred, y_train[0:1]))
    print("Y")
    y_pred = net.forward(X_train[0:4,:])
    print(loss(y_pred, y_train[0:4]))

if __name__ == "__main__":
    nlp_72()