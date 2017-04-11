import numpy as np
import itertools
from scipy import linalg
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import mixture


# uses a Gaussian mixture model (https://en.wikipedia.org/wiki/Mixture_model)
# for building models that fit inputted attribute distribution
# Selects best fitting model using Bayesian Information Criterion, then draws samples from that model
def __sampleData(inputDataSet, outputSize):
    X = inputDataSet
    # Bayesian Information Criterion is a way of scoring performance of the model
    lowest_bic = np.infty
    bic = []
    # We have a range of models which will vary in performance for a given dataset
    # let's iterate through them and use the one which works best
    n_components_range = range(1, 7)
    cv_types = ['spherical', 'tied', 'diag', 'full']
    for cv_type in cv_types:
        for n_components in n_components_range:
            # Fit a Gaussian mixture with EM
            gmm = mixture.GaussianMixture(n_components=n_components,
                                          covariance_type=cv_type)
            gmm.fit(X)
            bic.append(gmm.bic(X))
            if bic[-1] < lowest_bic:
                lowest_bic = bic[-1]
                best_gmm = gmm
    clf = best_gmm
    # Draw a bunch of random samples from the best-fitting distribution
    no_synthetic_samples = outputSize
    synthetic_data = clf.sample(no_synthetic_samples)
    x_synth = synthetic_data[0]
    return x_synth
