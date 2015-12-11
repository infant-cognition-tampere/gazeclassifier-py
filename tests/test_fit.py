# -*- coding: utf-8 -*-
import training_data
import gazeclassifier as gaze
import unittest2 as unittest  # to support Python 2.6

class TestFit(unittest.TestCase):

    def test_run(self):
        '''
        should be capable to learn from test set
        '''
        X, y = training_data.load('simple')
        gc = gaze.GazeClassifier()
        gc.fit(X, y)

        for pointlist, gazeclass in zip(X, y):
            pred = gc.predict(pointlist)
            self.assertEqual(pred, gazeclass)

    # def test_gaps(self):
    #     '''
    #     '''
    #     saccademodel.fit([])

if __name__ == '__main__':
    unittest.main()
