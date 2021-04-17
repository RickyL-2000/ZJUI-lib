##################################################################################################################
##      ECE449 assignment 2, task 3: LeNet in PyTorch.                                                          ##
##--------------------------------------------------------------------------------------------------------------##
##      Script template created for the course ECE449 at Zhejiang University / University of                    ##
##      Illinois at Urbana-Champaign Institute (ZJU-UIUC Institute) in Fall 2020 semester.                      ##
##      Licensing Information:  You are free to use or extend this project if:                                  ##
##          (1) You don't distribute or publish coding solutions for ECE449 Assignments in this project online. ##
##          (2) You retain this notice.                                                                         ##
##          (3) You provide clear attribution to ZJU-UIUC Institute.                                            ##
##--------------------------------------------------------------------------------------------------------------##
##          Written by Jinghua Wang (jinghuawang@intl.zju.edu.cn), last edit: 2020-11-04                        ##
##################################################################################################################

import torch
from torch import nn
import torchvision
from torchvision import transforms
from torch.utils import data

##################################################################################################################
#                                             NN implementations                                                 #

class Reshape(torch.nn.Module):
    def forward(self, x):
        return x.view(-1, 1, 28, 28)

def get_lenet():
    # get a lenet model using torch.nn
    net = torch.nn.Sequential(
        Reshape(),
        ####################################################
        #        YOUR IMPLEMENTATION HERE         [5pts]   #
        ####################################################
        #     add lines below in your implementation       #
        ####################################################
        
    )
    return net

##################################################################################################################

##################################################################################################################
#                      You may write other helper functions and/or classes here, if you need                     #

def try_gpu(i=0):
    #Return gpu(i) if detected, otherwise return cpu() for device
    if torch.cuda.device_count() >= i + 1:
        return torch.device(f'cuda:{i}')
    return torch.device('cpu')

class Accumulator:
    # Class for accumulating sums over n variables.
    def __init__(self, n):
        self.data = [0.0] * n
    def add(self, *args):
        self.data = [a + float(b) for a, b in zip(self.data, args)]
    def reset(self):
        self.data = [0.0] * len(self.data)
    def __getitem__(self, idx):
        return self.data[idx]

def accuracy(y_hat, y):
    # Compute the number of correct predictions."""
    if len(y_hat.shape) > 1 and y_hat.shape[1] > 1:
        y_hat = y_hat.argmax(axis=1)        
    cmp = y_hat.type(y.dtype) == y
    return float((cmp.type(y.dtype)).sum())

def evaluate_accuracy_try_gpu(net, data_iter, device=None):
    # Evaluate the accuracy for a model on a dataset from data_iter.
    # If GPU exists then use GPU, otherwise use CPU.
    # returns None if net has not been constructed properly(too shallow).
    if len(net) <= 2:
        return None
    net.eval()  # Set the model to evaluation mode to disable gradient update
    if not device:
        device = next(iter(net.parameters())).device
    # metric contains: (1) No. of correct predictions, (2) no. of predictions
    metric = Accumulator(2)
    for X, y in data_iter:
        X, y = X.to(device), y.to(device)
        metric.add(accuracy(net(X), y), y.numel())
    return metric[0] / metric[1]

##################################################################################################################

##################################################################################################################
#                 The training function (and its helper functions and/or classes, if you need)                   #

def train_cnn(net, train_iter, test_iter, num_epochs, lr, device=try_gpu()):
    # From task 1 and task 2, you should get a pretty clear idea what we need to do for model training.
    # Now, its your time to implement the whole train function, you will use this function in task 3 and 4.
    # Good Luck!
    ####################################################
    #        YOUR IMPLEMENTATION HERE         [15pts]  #
    ####################################################
    return 

##################################################################################################################

##################################################################################################################
#                                          Other utility functions                                               #

def load_data_fashion_mnist(batch_size, resize=None):
    # Load the Fashion-MNIST dataset from hard drive into memory.
    # Download the Fashion-MNIST dataset if needed.
    trans = [transforms.ToTensor()]
    if resize:
        trans.insert(0, transforms.Resize(resize))
    trans = transforms.Compose(trans)
    fashion_mnist_train = torchvision.datasets.FashionMNIST(
        root="./data", train=True, transform=trans, download=True)
    fashion_mnist_test = torchvision.datasets.FashionMNIST(
        root="./data", train=False, transform=trans, download=True)
    return (data.DataLoader(fashion_mnist_train, batch_size, shuffle=True, num_workers=4),
            data.DataLoader(fashion_mnist_test, batch_size, shuffle=False, num_workers=4))

def get_correct_lenet_shape_str():
    return """Reshape output shape: 	 torch.Size([1, 1, 28, 28])
Conv2d output shape: 	 torch.Size([1, 6, 28, 28])
Sigmoid output shape: 	 torch.Size([1, 6, 28, 28])
AvgPool2d output shape: 	 torch.Size([1, 6, 14, 14])
Conv2d output shape: 	 torch.Size([1, 16, 10, 10])
Sigmoid output shape: 	 torch.Size([1, 16, 10, 10])
AvgPool2d output shape: 	 torch.Size([1, 16, 5, 5])
Flatten output shape: 	 torch.Size([1, 400])
Linear output shape: 	 torch.Size([1, 120])
Sigmoid output shape: 	 torch.Size([1, 120])
Linear output shape: 	 torch.Size([1, 84])
Sigmoid output shape: 	 torch.Size([1, 84])
Linear output shape: 	 torch.Size([1, 10])"""

##################################################################################################################