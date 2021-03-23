# %%
# %pylab inline
import numpy as np
from sklearn import neighbors
from sklearn import svm
from sklearn import model_selection
from numpy import genfromtxt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import glob
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

# %%
# Get list of emails
base_dir = '/ECE365/lab3'
spamfiles = glob.glob(base_dir + '/Data/Spam/*')
hamfiles = glob.glob(base_dir + '/Data/Ham/*')

# %%
# First, we will split the files into the training, validation and test sets.

np.random.seed(seed=222017)  # seed the RNG for repeatability

fnames = np.asarray(spamfiles+hamfiles)
nfiles = fnames.size
labels = np.ones(nfiles)
labels[len(spamfiles):]=-1

# Randomly permute the files we have
idx = np.random.permutation(nfiles)
fnames = fnames[idx]
labels = labels[idx]

# Split the file names into which set they belong to
tname = fnames[:int(nfiles/2)]
trainlabels = labels[:int(nfiles/2)]
vname = fnames[int(nfiles/2):int(nfiles*3/4)]
vallabels = labels[int(nfiles/2):int(nfiles*3/4)]
tename = fnames[int(3/4*nfiles):]
testlabels = labels[int(3/4*nfiles):]

# %%
from sklearn.feature_extraction.text import CountVectorizer

# Get our Bag of Words Features from the data
bow = CountVectorizer(input='filename', encoding='iso-8859-1', binary=False)
traindata = bow.fit_transform(tname)
valdata = bow.transform(vname)
testdata = bow.transform(tename)

# %%
error = lambda y, yhat: np.mean(y != yhat)

# %%
classifier = BernoulliNB()
classifier.fit(traindata, trainlabels)
y_hat = classifier.predict(traindata)

# %%
print(error(trainlabels, y_hat))
print(1 - classifier.score(traindata, trainlabels))
