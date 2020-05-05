import os
import sys
import re
import pandas as pd
import numpy as np

import torch
from torch import from_numpy
from torch.autograd import Variable
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torch.utils.data

from tqdm import tqdm


from typing import List, Tuple


THISFILEDIR = os.path.dirname(os.path.abspath(__file__))
result_dir_path = os.path.join(THISFILEDIR, "..", "..", "result","chapter8")

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc = nn.Linear(300,4,bias=False)
    
    def forward(self, x):
        x = F.softmax(self.fc(x), dim=1)
        return x

def nlp_74():

    X_train = from_numpy(np.load(os.path.join(result_dir_path, "train_X.npy")).astype(np.float32))
    y_train = from_numpy(np.load(os.path.join(result_dir_path, "train_y.npy")).astype(np.int64))
    X_test = from_numpy(np.load(os.path.join(result_dir_path, "test_X.npy")).astype(np.float32))
    y_test = from_numpy(np.load(os.path.join(result_dir_path, "test_y.npy")).astype(np.int64))

    model = Net()
    loss_func = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

    for epoch in tqdm(range(100),desc="epoch"):
        optimizer.zero_grad()
        output = model(X_train)
        loss = loss_func(output, y_train)
        loss.backward()
        optimizer.step()

    print("Training data:")
    test_out = model(X_train)
    _, y_pred = torch.max(test_out.data, 1)
    print(sum(y_train==y_pred).item() / y_train.size()[0])

    print("Test data:")
    test_out = model(X_test)
    _, y_pred = torch.max(test_out.data, 1)
    print(sum(y_test==y_pred).item() / y_test.size()[0])

if __name__ == "__main__":
    nlp_74()