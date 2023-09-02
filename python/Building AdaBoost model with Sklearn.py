import numpy as np
import sklearn
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split

def train_ada_boost(X, target, estimators = 3, random_seed = None):
    if random_seed is None:
        random_seed = 0
        
    # Split the train set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, target, random_state = random_seed)
    
    clf = AdaBoostClassifier(
        n_estimators=estimators,
        random_state = random_seed,
        algorithm = 'SAMME.R',
        learning_rate = 1.0
    )
    
    clf.fit(X_train.reshape(-1, 1), y_train)
    
    return (clf, X_test, y_test)
