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
        self.fc1 = nn.Linear(300,100)
        self.act1 = nn.PReLU()
        self.bn1 = nn.BatchNorm1d(100)
        self.fc2 = nn.Linear(100,30)
        self.act2 = nn.PReLU()
        self.bn2 = nn.BatchNorm1d(30)
        self.fc3 = nn.Linear(30,4)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.act1(x)
        x = self.bn1(x)
        x = self.fc2(x)
        x = self.act2(x)
        x = self.bn2(x)
        x = self.fc3(x)
        return x


def nlp_79():

    EPOCH_SIZE = 100
    CHECKPOINT_SPAN = 1000
    BATCH_SIZE = 8
    checkpoint_dir = os.path.join(result_dir_path, "79_checkpoint")
    if not os.path.isdir(checkpoint_dir):
        os.makedirs(checkpoint_dir)

    X_train = from_numpy(np.load(os.path.join(result_dir_path, "train_X.npy")).astype(np.float32))
    y_train = from_numpy(np.load(os.path.join(result_dir_path, "train_y.npy")).astype(np.int64))
    X_valid = from_numpy(np.load(os.path.join(result_dir_path, "valid_X.npy")).astype(np.float32))
    y_valid = from_numpy(np.load(os.path.join(result_dir_path, "valid_y.npy")).astype(np.int64))

    X_valid = Variable(X_valid).cuda()
    y_valid = Variable(y_valid).cuda()

    model = Net().cuda()
    loss_func = nn.CrossEntropyLoss()
    optimizer =optim.SGD(model.parameters(),lr=0.01)
    
    train = torch.utils.data.TensorDataset(X_train, y_train)
    train_loader = torch.utils.data.DataLoader(train, batch_size=BATCH_SIZE, shuffle=True)
    train_loss_list = []
    valid_loss_list = []
    train_acc_list = []
    valid_acc_list = []

    for epoch in tqdm(range(EPOCH_SIZE),desc="epoch"):

        loss_total = 0.0
        train_all_cnt = 0
        train_corr_cnt = 0
        for data in train_loader:
            X, y = data
            X, y = Variable(X).cuda(), Variable(y).cuda()
            optimizer.zero_grad()
            train_output = model(X)
            train_loss = loss_func(train_output, y)
            loss_total += train_loss.item()

            _, y_pred = torch.max(train_output.data, 1)
            train_corr_cnt += sum(y==y_pred).item()
            train_all_cnt += y.size()[0]

            train_loss.backward()
            optimizer.step()

        train_loss_list.append(loss_total / len(train_loader))
        train_acc_list.append(
            train_corr_cnt / train_all_cnt
        )

        valid_output = model(X_valid)
        valid_loss = loss_func(valid_output, y_valid)
        valid_loss_list.append(valid_loss.item())
        _, y_pred = torch.max(valid_output.data, 1)
        valid_acc_list.append(
            sum(y_valid==y_pred).item() / y_valid.size()[0]
        )

        if (epoch+1) % CHECKPOINT_SPAN == 0:
            torch.save({
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict()
            },os.path.join(checkpoint_dir,"checkpoint_{}.tar".format(epoch)))
        
    graph_x = list(range(1,EPOCH_SIZE+1))

    fig, ax = plt.subplots()
    ax.plot(graph_x, train_loss_list, color="blue", label="train loss")
    ax.plot(graph_x, valid_loss_list, color="green", label="valid loss")
    ax.legend()
    plt.savefig(os.path.join(checkpoint_dir, "loss_batch{}.png".format(BATCH_SIZE)))

    plt.clf()
    fig, ax = plt.subplots()
    ax.plot(graph_x, train_acc_list, color="blue", label="train accuracy")
    ax.plot(graph_x, valid_acc_list, color="green", label="valid accuracy")
    ax.legend()
    plt.savefig(os.path.join(checkpoint_dir, "accuracy{}.png".format(BATCH_SIZE)))

if __name__ == "__main__":
    nlp_79()