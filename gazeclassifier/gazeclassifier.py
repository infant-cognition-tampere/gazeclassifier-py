from sklearn import svm
import numpy as np
from .features import extract_features
from .classes import convert_to_integers, convert_to_strings

class GazeClassifier(object):

    def __init__(self):
        # Load default pretrained state
        # TODO
        self.learner = svm.SVC()

    def fit(self, pointlistlist, classes):

        # Convert pointlists to numeric features
        fl = list([extract_features(pl) for pl in pointlistlist])

        # Convert classes to integers
        cl = list(convert_to_integers(classes))

        # Convert to numpy arrays
        numfl = np.array(fl, dtype=np.float64)
        numcl = np.array(cl, dtype=np.int16)

        self.learner.fit(numfl, numcl)

    def predict(self, pointlist_or_raw_features):
        feat = extract_features(pointlist_or_raw_features)

        # Convert to numpy arrays
        numfeat = np.array(feat, dtype=np.float64)

        c = self.learner.predict([numfeat])
        sc = list(convert_to_strings(c))
        return sc[0]
