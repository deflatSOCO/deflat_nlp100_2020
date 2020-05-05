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

def nlp_73():

    X_train = np.load(os.path.join(result_dir_path, "train_X.npy")).astype(np.float32)
    y_train = np.load(os.path.join(result_dir_path, "train_y.npy")).astype(np.int64)
    X_train = torch.from_numpy(X_train)
    y_train = torch.from_numpy(y_train)

    model = Net()
    loss_func = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

    for epoch in tqdm(range(100),desc="epoch"):
        optimizer.zero_grad()
        output = model(X_train)
        loss = loss_func(output, y_train)
        loss.backward()
        optimizer.step()
    print(model.state_dict()['fc.weight'])

if __name__ == "__main__":
    nlp_73()