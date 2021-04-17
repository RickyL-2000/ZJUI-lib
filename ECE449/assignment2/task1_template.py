##################################################################################################################
##      ECE449 assignment 2, task 1: simple and small DNN from scratch.                                         ##
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

import numpy as np
import time

##################################################################################################################
#                                       NN basic implementations                                                 #

# define the relu function
def relu(X):
    # X: A numpy.ndarray object
    ####################################################
    #        YOUR IMPLEMENTATION HERE         [3pts]   #
    ####################################################
    #  Change the line below to your implementation    #
    ####################################################
    ret = np.zeros(X.shape)
    return ret

# define the partial derivative of relu function
def prelu(X):
    # X: A numpy.ndarray object
    # return: gradient of relu function with respect to its input
    ####################################################
    #        YOUR IMPLEMENTATION HERE         [2pts]   #
    ####################################################
    #  Change the line below to your implementation    #
    ####################################################
    ret = np.zeros(X.shape)
    return ret

# define the forward propagation
def DNNforward(X, W, K):
    # X: dataset input features, numpy.ndarray
    # W: current weight matrix W, numpy.ndarray of shape (2,3)
    # K: current weight matrix K, numpy.ndarray of shape (2,)
    # return: (H, A, O)
    # H: current hidden layer output value H, numpy.ndarray
    # A: current activation layer output A, numpy.ndarray
    # O: current DNN model output O, numpy.ndarray
    ####################################################
    #        YOUR IMPLEMENTATION HERE         [5pts]   #
    ####################################################
    #  Change the lines below to your implementation   #
    ####################################################
    H = np.zeros((2,X.shape[0]))
    A = np.zeros((2,X.shape[0]))
    O = np.zeros(X.shape[0])
    return H, A, O

# define the backward propagation
def DNNbackward(X, y, W, K, H, A, O):
    # X: dataset input features, numpy.ndarray
    # y: dataset labels, numpy.ndarray
    # W: current weight matrix W, numpy.ndarray
    # K: current weight matrix K, numpy.ndarray
    # H: current hidden layer output value H, numpy.ndarray
    # A: current activation layer output A, numpy.ndarray
    # O: current DNN model output O, numpy.ndarray
    # return: (pLpW, pLpK)
    # pLpW: current gradient of Loss with respect to W
    # pLpK: current gradient of Loss with respect to K
    ####################################################
    #        YOUR IMPLEMENTATION HERE         [5pts]   #
    ####################################################
    #  Change the lines below to your implementation   #
    ####################################################
    pLpW = np.zeros(W.shape)
    pLpK = np.zeros(K.shape)
    return pLpW, pLpK

# gradient decent function in batches
def train(X, y, W, K, lr, num_epochs=10, batch_size=10, print_loss=False):
    # X: dataset input features, numpy.ndarray
    # y: dataset labels, numpy.ndarray
    # W: current weight matrix W, numpy.ndarray
    # K: current weight matrix K, numpy.ndarray
    # lr: learning rate, float or int
    # nump_epochs: total number of epochs we train our NN model, int
    # batch_size: number of samples in each batch, int
    # print_loss: whether we print loss in each epoch during training, bool
    # return: (W_list, K_list)
    # W_list: list of numpy.ndarrays containing all the W parameters after each epoch
    # K_list: list of numpy.ndarrays containing all the K parameters after each epoch
    W_list, K_list = [], []
    dataset_size = len(y)
    for epoch in range(num_epochs):
        for batch_idx in range(int(np.ceil(dataset_size/batch_size))):
            start_idx = batch_idx * batch_size
            end_idx = min((batch_idx+1)*batch_size, dataset_size-1)
            H, A, O = DNNforward(X[start_idx:end_idx], W, K)
            if print_loss:
                print("Epoch "+str(epoch+1)+", batch "+str(batch_idx+1)+", loss = "+str(loss(y[start_idx:end_idx], O)), end='\n')
            # update W and K
            ####################################################
            #        YOUR IMPLEMENTATION HERE         [5pts]   #
            ####################################################
            #  We expect 2-3 lines of code in calculating      #
            #  partial derivatives and updating W and K below  #
            ####################################################
            # Your implementation starts from here             #
            

            # Your implmentation ends here                     #
            ####################################################
        W_list.append(W)
        K_list.append(K)
    return W_list, K_list

# define the loss function
def loss(y, O):
    # we use squared loss
    return np.mean(1/2 * (y-O)**2)

# obtain model inference results
def DNNinference(X, W, K):
    # X: dataset input features, numpy.ndarray
    # y: dataset labels, numpy.ndarray
    # W: current weight matrix W, numpy.ndarray
    # K: current weight matrix K, numpy.ndarray
    _,_, y_pred = DNNforward(X, W, K) 
    if np.min(y_pred) == 0:
        y_pred = np.array(y_pred>0,dtype=int)
    else:
        y_pred = np.array(y_pred>=0,dtype=int)
    y_pred[y_pred==0] = -1
    return y_pred

# obtain the train accuracy
def trainAcc(X, y, W, K):
    # X: dataset input features, numpy.ndarray
    # y: dataset labels, numpy.ndarray
    # W: current weight matrix W, numpy.ndarray
    # K: current weight matrix K, numpy.ndarray
    return np.mean(DNNinference(X, W, K) == y)

##################################################################################################################

##################################################################################################################
#     Other helper functions for implementation check, visualization, dataset generation, and preprocessing      #

def computeNumericalGradient(J,theta):
    # theta: function input.
    # J: a python function object with theta as its parameter.
    # returns the numerical gradient approximation value of J at theta.
    numgrad = np.zeros(np.shape(theta))
    EPSILON = 10**(-6)
    if len(theta.shape) == 2:
        for i in range(theta.shape[0]):
            for j in range(theta.shape[1]):
                epsi = np.zeros(np.shape(theta))
                epsi[i,j] = EPSILON
                numgrad[i,j] = (J(theta+epsi)-J(theta))/EPSILON
    elif len(theta.shape) == 1:
        for i in range(np.size(theta)):
            epsi = np.zeros(np.shape(theta))
            epsi[i] = EPSILON/2
            numgrad[i] = (J(theta+epsi)-J(theta-epsi))/EPSILON
    else:
        print("Theta has shape:", theta.shape,", numerical gradient calculations not implemented for this shape.")
        print("Only numerical gradient calculations for 1-d and 2-d arrays are implemented.")
    return numgrad

def generate_random_dataset(num_samples=400):
    # generate a random dataset of two classes that can be perfectly separated in Euclidean space.
    num_samples = 400
    cluster_r = 1
    num_cls_1_samples = int(np.ceil(num_samples/2))

    cls_1_center = np.random.uniform(low=-3, high=6, size=3)
    cls_2_center = cls_1_center - np.random.choice([-1,1], 3, replace=True) * np.random.uniform(low=2, high=4, size=3)

    cls_1_samples = np.random.uniform(low=-cluster_r, high=cluster_r, size=(num_cls_1_samples, 3)) + cls_1_center
    cls_2_samples = np.random.uniform(low=-cluster_r, high=cluster_r, size=(num_samples-num_cls_1_samples, 3)) + cls_2_center

    cls_tags = np.ones(shape=(num_samples, 1))
    cls_tags[int(np.ceil(num_samples/2)):] = -1

    dataset = np.hstack([np.vstack([cls_1_samples,cls_2_samples]), cls_tags])
    dataset = dataset[np.random.choice([i for i in range(len(dataset))], len(dataset), replace=False)]
    return dataset

def normalize_dataset(dataset):
    # normalize dataset features 
    from sklearn import preprocessing
    dataset[:, :3] = preprocessing.scale(dataset[:, :3])
    return dataset

def visualize_dataset(dataset, window_title=""):
    # visualize dataset using 3D plot
    from matplotlib import pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure(num=window_title)
    ax = Axes3D(fig)
    ax.scatter(dataset[:, 0][dataset[:,3]==1], dataset[:, 1][dataset[:,3]==1], dataset[:, 2][dataset[:,3]==1], label="class 1")
    ax.scatter(dataset[:, 0][dataset[:,3]==-1], dataset[:, 1][dataset[:,3]==-1], dataset[:, 2][dataset[:,3]==-1], label="class 2")
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.set_zlabel("$x_3$")
    ax.legend()
    plt.show()

def plotDNNInferenceEpoch(epoch_idx, dataset, W_list, K_list):
    # plot DNN inference boundary in 3D for each epoch
    # this function requires a correct implementation of DNNforward to work correctly
    from matplotlib import pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    mesh_res=(40, 40, 40)
    y_pred = DNNinference(dataset[:,:3], W_list[epoch_idx], K_list[epoch_idx])
    print("Current train accuracy is:", trainAcc(dataset[:,:3], dataset[:,3], W_list[epoch_idx], K_list[epoch_idx]))
    
    X_mesh = np.array(np.meshgrid(
                         np.linspace(np.min(dataset[:,:3][:, 0]), np.max(dataset[:,:3][:, 0]), mesh_res[0]), 
                         np.linspace(np.min(dataset[:,:3][:, 1]), np.max(dataset[:,:3][:, 1]), mesh_res[1]), 
                         np.linspace(np.min(dataset[:,:3][:, 2]), np.max(dataset[:,:3][:, 2]), mesh_res[2]))).reshape(3, mesh_res[0]*mesh_res[1]*mesh_res[2]).T
    _, _, y_mesh = DNNforward(X_mesh, W_list[epoch_idx], K_list[epoch_idx])
    X_mesh = X_mesh[(0 < np.abs(y_mesh)) *(np.abs(y_mesh) < 0.05)]

    fig = plt.figure(figsize=(10,7))
    ax = Axes3D(fig)
    ax.scatter(dataset[:,:3][:, 0][y_pred==-1], dataset[:,:3][:, 1][y_pred==-1], dataset[:,:3][:, 2][y_pred==-1], s=20, label='class 1 (predicted)')
    ax.scatter(dataset[:,:3][:, 0][y_pred==1], dataset[:,:3][:, 1][y_pred==1], dataset[:,:3][:, 2][y_pred==1], s=20, label='class 2 (predicted)')
    if len(X_mesh) > 0: 
        surf = ax.plot_trisurf(X_mesh[:, 0], X_mesh[:, 1], X_mesh[:, 2], label='DNN inference boundary (approx)',  edgecolor='none', color=[1, 0, 0, 0.3])
        surf._facecolors2d=surf._facecolors3d
        surf._edgecolors2d=surf._edgecolors3d
    else:
        print("No visual boundaries are generated.")
    #surf = ax.scatter(X_mesh[:, 0], X_mesh[:, 1], X_mesh[:, 2], label='DNN inference boundary', s=10, color='cyan')
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.set_zlabel("$x_3$")
    ax.view_init(elev=30, azim=260)
    ax.legend()
    plt.show()
##################################################################################################################