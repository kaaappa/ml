import numpy as np
from scipy.spatial.distance import cdist


def prod_non_zero_diag(x):
    return np.prod(np.diag(x)[np.diag(x)!=0])


def are_multisets_equal(x, y):
    return np.array_equal(np.sort(x), np.sort(y))


def max_after_zero(x):
    return np.max(x[1:][np.nonzero(x[:-1] == 0)])


def convert_image(img, coefs):
    return np.dot(img, coefs)


def run_length_encoding(x):
    return (x[np.nonzero(np.diff(np.concatenate((x, np.array([x[-1] - 1])))))],
            np.diff(np.nonzero(np.diff(np.concatenate((np.array([0]), x, np.array([x.shape[0]])))))))


def pairwise_distance(x, y):
    return np.vectorize(np.sqrt)(np.dot(np.vectorize(np.square)(np.repeat(x, len(y), axis=0).reshape((len(x), len(y), 2)) -
                                                                np.tile(y.reshape((len(y) * 2,)), len(x)).reshape((len(x), len(y), 2))), np.array([1, 1])))


def pairwise_distance_scipy(x, y):
    return cdist(x, y, metric='euclidean')

