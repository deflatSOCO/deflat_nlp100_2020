import os
import sys
import re
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

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


def nlp_75():

    EPOCH_SIZE = 100

    X_train = from_numpy(np.load(os.path.join(result_dir_path, "train_X.npy")).astype(np.float32))
    y_train = from_numpy(np.load(os.path.join(result_dir_path, "train_y.npy")).astype(np.int64))
    X_valid = from_numpy(np.load(os.path.join(result_dir_path, "valid_X.npy")).astype(np.float32))
    y_valid = from_numpy(np.load(os.path.join(result_dir_path, "valid_y.npy")).astype(np.int64))
    X_test = from_numpy(np.load(os.path.join(result_dir_path, "test_X.npy")).astype(np.float32))
    y_test = from_numpy(np.load(os.path.join(result_dir_path, "test_y.npy")).astype(np.int64))

    model = Net()
    loss_func = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

    train_loss_list = []
    valid_loss_list = []
    train_acc_list = []
    valid_acc_list = []

    for epoch in tqdm(range(EPOCH_SIZE),desc="epoch"):
        optimizer.zero_grad()
        train_output = model(X_train)
        train_loss = loss_func(train_output, y_train)
        valid_output = model(X_valid)
        valid_loss = loss_func(valid_output, y_valid)

        train_loss_list.append(train_loss.item())
        valid_loss_list.append(valid_loss.item())

        _, y_pred = torch.max(train_output.data, 1)
        train_acc_list.append(
            sum(y_train==y_pred).item() / y_train.size()[0]
        )
        _, y_pred = torch.max(valid_output.data, 1)
        valid_acc_list.append(
            sum(y_valid==y_pred).item() / y_valid.size()[0]
        )
        train_loss.backward()
        optimizer.step()
    
    graph_x = list(range(1,EPOCH_SIZE+1))

    fig, ax = plt.subplots()
    ax.plot(graph_x, train_loss_list, color="blue", label="train loss")
    ax.plot(graph_x, valid_loss_list, color="green", label="valid loss")
    ax.legend()
    plt.savefig(os.path.join(result_dir_path, "loss.png"))

    plt.clf
    fig, ax = plt.subplots()
    ax.plot(graph_x, train_acc_list, color="blue", label="train accuracy")
    ax.plot(graph_x, valid_acc_list, color="green", label="valid accuracy")
    ax.legend()
    plt.savefig(os.path.join(result_dir_path, "accuracy.png"))

if __name__ == "__main__":
    nlp_75()