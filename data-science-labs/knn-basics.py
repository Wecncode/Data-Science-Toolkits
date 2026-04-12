import numpy as np
from collections import Counter

class KNNClassifierScratch:
    """
    A pure Python/NumPy implementation of the K-Nearest Neighbors algorithm.
    No machine learning libraries allowed.
    """
    def __init__(self, k=3):
        # K is the number of voting neighbors
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X, y):
        """
        KNN is a 'lazy' learner. The training phase literally just stores the data.
        """
        self.X_train = np.array(X)
        self.y_train = np.array(y)

    def _euclidean_distance(self, point1, point2):
        """Calculates the straight-line distance between two vectors."""
        return np.sqrt(np.sum((point1 - point2) ** 2))

    def predict(self, X_test):
        """Generates predictions for an array of test data points."""
        X_test = np.array(X_test)
        predictions = [self._predict_single_point(x) for x in X_test]
        return np.array(predictions)

    def _predict_single_point(self, x):
        """Core logic: Find distances, sort, and take a majority vote."""
        # 1. Calculate distances between 'x' and all points in the training set
        distances = [self._euclidean_distance(x, x_train) for x_train in self.X_train]
        
        # 2. Get the indices of the 'k' smallest distances
        k_indices = np.argsort(distances)[:self.k]
        
        # 3. Extract the labels of those 'k' nearest neighbors
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        
        # 4. Take a majority vote (most common class wins)
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]

if __name__ == "__main__":
    # Simulated Developer Skill Data: [Hours_Studied, Projects_Built]
    X_train = [[20, 2], [50, 5], [10, 0], [60, 8], [30, 3], [80, 10]]
    # Labels: 0 = Junior, 1 = Mid-Level
    y_train = [0, 1, 0, 1, 0, 1]
    
    # Initialize our scratch-built model
    model = KNNClassifierScratch(k=3)
    model.fit(X_train, y_train)
    
    # A new developer comes along with 45 hours studied and 4 projects
    new_dev = [[45, 4]]
    
    prediction = model.predict(new_dev)
    level = "Mid-Level" if prediction[0] == 1 else "Junior"
    
    print(f"Based on our custom KNN, the new developer is classified as: {level}")
