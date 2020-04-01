#Euclidean Distance = Sqrt of (x2 - x1)^2 + (y2 - y1)^2
#Or Sqrt(n, i=0, (qi - pi))2)
import numpy as np
from collections import Counter

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1-x2)**2))

class kNN:
    def __init__(self, k = 3): #default as three
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predicted_labels = [self._predict(x) for x in X]
        return np.array(predicted_labels)

    def _predict(self, x): #calculate distance from x to the training samples
        #compute distances
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        #get k nearest neighbors, labels,
        k_indicies = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indicies]
        #majority vote, most common class label
        most_common = Counter(k_nearest_labels).most_common(1) #[(number that occurs most, count of it)]
        return most_common[0][0]


