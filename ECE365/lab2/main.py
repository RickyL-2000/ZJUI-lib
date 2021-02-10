# %%
# %pylab inline
import numpy as np
import scipy.spatial.distance as dist
from scipy import stats
from sklearn import neighbors
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import time

class Question1(object):
    def bayesClassifier(self,data,pi,means,cov):
        cov_inv = np.linalg.inv(cov)
        delta_y = np.log(pi) + data.dot(cov_inv).dot(means.T) - 0.5 * means.dot(cov_inv).dot(means.T).diagonal()
        y_hat = np.argmax(delta_y, axis=1)
        return y_hat

    def classifierError(self,truelabels,estimatedlabels):
        return np.sum(truelabels != estimatedlabels) / (1.0 * len(truelabels))


class Question2(object):
    def trainLDA(self,trainfeat,trainlabel):
        nlabels = int(trainlabel.max())+1                         # Assuming all labels up to nlabels exist.
        pi = np.zeros(nlabels)                                    # (l, ) Store your prior in here
        means = np.zeros((nlabels,trainfeat.shape[1]))            # (l, d) Store the class means in here
        cov = np.zeros((trainfeat.shape[1],trainfeat.shape[1]))   # (d, d) Store the covariance matrix in here
        # Put your code below
        nsamples = trainfeat.shape[0]
        for label in range(nlabels):
            pi[label] = trainfeat[trainlabel==label].shape[0] / nsamples
            means[label] = trainfeat[trainlabel==label].sum(axis=0) / trainfeat[trainlabel==label].shape[0]
            cov += (trainfeat[trainlabel==label] - means[label]).T.dot((trainfeat[trainlabel==label] - means[label]))
        cov /= nsamples - nlabels
        # Don't change the output!
        return (pi,means,cov)

    def estTrainingLabelsAndError(self,trainingdata,traininglabels):
        q1 = Question1()
        # You can use results from Question 1 by calling q1.bayesClassifier(...), etc.
        # If you want to refer to functions under the same class, you need to use self.fun(...)
        pi, means, cov = self.trainLDA(trainingdata, traininglabels)
        esttrlabels = q1.bayesClassifier(trainingdata, pi, means, cov)
        trerror = q1.classifierError(esttrlabels, traininglabels)
        # Don't change the output!
        return (esttrlabels, trerror)

    def estValidationLabelsAndError(self,trainingdata,traininglabels,valdata,vallabels):
        q1 = Question1()
        # You can use results from Question 1 by calling q1.bayesClassifier(...), etc.
        # If you want to refer to functions under the same class, you need to use self.fun(...)
        pi, means, cov = self.trainLDA(trainingdata, traininglabels)
        estvallabels = q1.bayesClassifier(valdata, pi, means, cov)
        valerror = q1.classifierError(vallabels, estvallabels)
        # Don't change the output!
        return (estvallabels, valerror)


class Question3(object):
    def kNN(self,trainfeat,trainlabel,testfeat, k):
        dists = dist.cdist(testfeat, trainfeat, metric='euclidean')
        knearest_idx = np.argpartition(dists, k, axis=1)[:, :k]
        klabels = trainlabel[knearest_idx]
        labels = stats.mode(klabels, axis=1)[0].squeeze()
        return labels

    def kNN_errors(self,trainingdata, traininglabels, valdata, vallabels):
        q1 = Question1()
        trainingError = np.zeros(4)
        validationError = np.zeros(4)
        k_array = [1,3,4,5]

        for i in range(len(k_array)):
            # Please store the two error arrays in increasing order with k
            # This function should call your previous self.kNN() function.
            # Put your code below
            esttrlabels = self.kNN(trainingdata, traininglabels, trainingdata, k_array[i])
            trainingError[i] = q1.classifierError(esttrlabels, traininglabels)
            estvallabels = self.kNN(trainingdata, traininglabels, valdata, k_array[i])
            validationError[i] = q1.classifierError(estvallabels, vallabels)

        # Don't change the output!
        return (trainingError, validationError)

class Question4(object):
    def sklearn_kNN(self,traindata,trainlabels,valdata,vallabels):
        fit_start = time.time()
        classifier = neighbors.KNeighborsClassifier(n_neighbors=1, algorithm='kd_tree').fit(traindata, trainlabels)
        fit_end = time.time()
        fitTime = fit_end - fit_start

        eval_start = time.time()
        estvallabels = classifier.predict(valdata)
        eval_end = time.time()
        predTime = eval_end - eval_start

        q1 = Question1()
        valerror = q1.classifierError(estvallabels, vallabels)

        # Don't change the output!
        return (classifier, valerror, fitTime, predTime)

    def sklearn_LDA(self,traindata,trainlabels,valdata,vallabels):
        fit_start = time.time()
        classifier = LinearDiscriminantAnalysis().fit(traindata, trainlabels)
        fit_end = time.time()
        fitTime = fit_end - fit_start

        eval_start = time.time()
        estvallabels = classifier.predict(valdata)
        eval_end = time.time()
        predTime = eval_end - eval_start

        q1 = Question1()
        valerror = q1.classifierError(estvallabels, vallabels)

        # Don't change the output!
        return (classifier, valerror, fitTime, predTime)

###

'''

# %%
# Load the data needed for Problems 1-3 

# Read the data
traindata_tmp= genfromtxt('train.csv', delimiter=',')
valdata_tmp= genfromtxt('val.csv', delimiter=',')

#The data which you will use to train LDA and kNN is called "trainingdata"
trainingdata=traindata_tmp[:,:2]
#The corresponding labels are in "traininglabels"
traininglabels=traindata_tmp[:,2]

#The data which you will use to validate LDA, kNN and the Bayes Classifier
#is called "valdata"
valdata=valdata_tmp[:,:2]
#The corresponding labels are in "vallabels"
vallabels=valdata_tmp[:,2]

adp=np.vstack([trainingdata,valdata])
xmin,xmax = adp[:,0].min()-1, adp[:,0].max()+1
ymin,ymax = adp[:,0].min()-1, adp[:,0].max()+1
xx, yy = np.meshgrid(np.arange(xmin, xmax, 0.05),np.arange(ymin, ymax, 0.05))
drdata= np.c_[xx.ravel(), yy.ravel()]

# %%
# Q1
# The prior information
pi=np.array([1/4,1/4,1/2])
means=np.array([[1,5],[5,0],[-2,-2]])
cov=np.array([[5,1],[1,5]])
# The data which you will use to test the classifier is called "data"
data=np.copy(valdata)
# The labels are in "truelabels"
truelabels=np.copy(vallabels)
# Create an object for Problem 1 from main.py
q1 = Question1()

estimatedlabels = q1.bayesClassifier(data,pi,means,cov)
print ("The Bayes classifier error rate is %.4f" % q1.classifierError(truelabels,estimatedlabels))
drB = q1.bayesClassifier(drdata,pi,means,cov)

# %%
# q2
q2 = Question2()
lpi, lmeans, lcov = q2.trainLDA(trainingdata,traininglabels)
print("The estimated priors are:")
print(lpi)
print("The estimated means are:")
print(lmeans)
print("The estimated covariance matrices are:")
print(lcov)
print("")
esttrlabels, trerror = q2.estTrainingLabelsAndError(trainingdata,traininglabels)
print("The training error for LDA is: %.4f" % trerror)
estvallabels, valerror = q2.estValidationLabelsAndError(trainingdata,traininglabels,valdata,vallabels)
print("The validation error for LDA is: %.4f" % valerror)
drLDA = q1.bayesClassifier(drdata,lpi,lmeans,lcov)

# %%

'''
