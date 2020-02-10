# _*_ coding: utf-8 _*_
import sklearn.datasets
import sklearn.svm
import sklearn.linear_model
import numpy as np
import matplotlib.pyplot as plt
import itertools

iris = sklearn.datasets.load_iris()

X = iris.data[:, [2, 3]]
y = iris.target

clf1 = sklearn.svm.SVC(kernel="rbf")
clf1.fit(X, y)

clf2 = sklearn.svm.SVC(kernel="poly")
clf2.fit(X, y)

clf3 = sklearn.svm.SVC(kernel="linear")
clf3.fit(X, y)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))

f, axarr = plt.subplots(1, 3, sharex='col', sharey='row', figsize=(20, 5))

for idx, clf, title in zip([0, 1, 2], [clf1, clf2, clf3], ['rbf', 'poly', 'linear']):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    axarr[idx].contourf(xx, yy, Z, alpha=0.4, cmap=plt.cm.RdYlBu)
    axarr[idx].scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.brg)
    axarr[idx].set_title(title)
plt.show()
