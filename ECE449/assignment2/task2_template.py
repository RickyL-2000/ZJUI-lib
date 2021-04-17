##################################################################################################################
##      ECE449 assignment 2, task 2: simple and small DNN using PyTorch.                                        ##
##--------------------------------------------------------------------------------------------------------------##
##      Script template created for the course ECE449 at Zhejiang University / University of                    ##
##      Illinois at Urbana-Champaign Institute (ZJU-UIUC Institute) in Fall 2020 semester.                      ##
##      Licensing Information:  You are free to use or extend this project if:                                  ##
##          (1) You don't distribute or publish coding solutions for ECE449 Assignments in this project online. ##
##          (2) You retain this notice.                                                                         ##
##          (3) You provide clear attribution to ZJU-UIUC Institute.                                            ##
##--------------------------------------------------------------------------------------------------------------##
##          Written by Jinghua Wang (jinghuawang@intl.zju.edu.cn), last edit: 2020-11-03                        ##
##################################################################################################################

import torch
from torch import nn
import numpy as np

##################################################################################################################
#                                             NN implementations                                                 #

def get_DNN():
    # get a simple and small DNN using torch.nn
    ####################################################
    #        YOUR IMPLEMENTATION HERE         [5pts]   #
    ####################################################
    #  Change the line below to your implementation    #
    ####################################################

    net = nn.Sequential()
    return net

def train_torch(net, dataset_X, dataset_y, num_epochs, lr, batch_size):
    # net: torch.nn.Sequential object, our simple and small DNN
    # dataset_X: dataset input features, numpy.ndarray
    # dataset_y: dataset labels, numpy.ndarray
    # nump_epochs: total number of epochs we train our NN model, int
    # lr: learning rate, float or int
    # batch_size: number of samples in each batch, int
    # return: (W_list, K_list)
    # W_list: list of numpy.ndarrays containing all the W parameters after each epoch
    # K_list: list of numpy.ndarrays containing all the K parameters after each epoch
    if len(net) > 0:    
        trainer = torch.optim.SGD(net.parameters(), lr=lr)
    loss = nn.MSELoss(reduction='sum')
    W_list, K_list = [], []
    if isinstance(net, torch.nn.Module):
        net = net.double()
        net = net.apply(init_weights)
        net.train()
    print_net_params_and_acc(net, dataset_X, dataset_y, before_training=True)
    dataset_size = len(dataset_y)
    for epoch in range(num_epochs):
        for batch_idx in range(int(np.ceil(dataset_size/batch_size))):
            start_idx = batch_idx * batch_size
            end_idx = min((batch_idx+1)*batch_size, dataset_size-1)
            X = torch.from_numpy(dataset_X[start_idx:end_idx]).double()
            y = torch.from_numpy(dataset_y[start_idx:end_idx, np.newaxis]).double()
            # Compute gradients and update parameters
            ####################################################
            #        YOUR IMPLEMENTATION HERE         [5pts]   #
            ####################################################
            #  We expect serveral lines of code in doing the   #
            #  gradient decent operations and updating net     #
            #  parameters.                                     #
            ####################################################
            # Your implementation starts from here             #
            

            # Your implmentation ends here                     #
            ####################################################
        if len(net) >= 2:
            W_list.append(net[0].weight.detach().numpy())
            K_list.append(net[2].weight.detach().numpy()[0])
    return W_list, K_list

##################################################################################################################

##################################################################################################################
#                                            Other helper functions                                              #

def print_net_params_and_acc(net, dataset_X, dataset_y, before_training=True):
    if len(net) == 0:
        return
    if before_training:
        print("Before training: \nThe initial W is:\n")
        print(net[0].weight.detach().numpy())
        print("\nThe initial K is:\n")
        print(net[2].weight.detach().numpy()[0])
        print("The accuracy before training is:", 
              accuracy(net(torch.from_numpy(dataset_X).double()), 
                       torch.from_numpy(dataset_y[:, np.newaxis]).double()), end='\n\n')
    else:
        print("After training: \nThe trained W is:\n")
        print(net[0].weight.detach().numpy())
        print("\nThe trained K is:\n")
        print(net[2].weight.detach().numpy()[0])
        print("The accuracy after training is:", 
              accuracy(net(torch.from_numpy(dataset_X).double()), 
                       torch.from_numpy(dataset_y[:, np.newaxis]).double()), end='\n\n')

def accuracy(y_hat, y):
    if y_hat.min() == 0:
        y_hat[y_hat >  0] = 1
        y_hat[y_hat <= 0] = -1
    else:
        y_hat[y_hat >= 0] = 1
        y_hat[y_hat <  0] = -1
    return float((y_hat == y).sum())/len(y)

def init_weights(m):
    if type(m) == nn.Linear:
        torch.nn.init.uniform_(m.weight, -0.2, 0.2)

def get_correct_DNN_shape_str():
    return """Linear output shape: 	 torch.Size([10, 2])
ReLU output shape: 	 torch.Size([10, 2])
Linear output shape: 	 torch.Size([10, 1])"""
##################################################################################################################