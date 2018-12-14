# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import datetime
from contextlib import contextmanager
import random
import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
# from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error

from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
from matplotlib import pyplot as plt

#Import own script
import base_methods as base


def adaboost():
    prefix = 'Data/'

    # ------------------------------- Learning ------------------------------- #
    # Load training data
    R = pd.read_csv('predicted_matrix.txt', sep=" ", header=None)
    user_movie_pairs = base.load_from_csv(os.path.join(prefix, 'data_train.csv'))
    training_labels = base.load_from_csv(os.path.join(prefix, 'output_train.csv'))

    # Build the training learning matrix
    X_train = base.create_learning_matrices(R.values, user_movie_pairs)

    # Build the model
    y_train = training_labels

    # Best estimator after hyperparameter tuning
    base_model = DecisionTreeRegressor()
    model =  AdaBoostRegressor(base_model)
    with base.measure_time('Training'):
        print("Training with adaboost...")
        model.fit(X_train, y_train)

    #Check for overfitting
    y_pred_train = model.predict(X_train)
    MSE_train = mean_squared_error(y_train, y_pred_train)
    print("MSE for adaboost: {}".format(MSE_train))

    # -----------------------Submission: Running model on provided test_set---------------------------- #
    # #Load test data
    # X_test = base.load_from_csv(os.path.join(prefix, 'test_user_movie_merge.csv'))
    # X_test_user_movie_pairs = base.load_from_csv(os.path.join(prefix, 'data_test.csv'))

    # #Predict
    # print("Predicting...")
    # y_pred = model.predict(X_test)

    # fname = base.make_submission(y_pred, X_test_user_movie_pairs, 'AdaboostMF')
    # print('Submission file "{}" successfully written'.format(fname))

if __name__ == '__main__':

    adaboost()
    