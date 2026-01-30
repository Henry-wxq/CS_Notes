# -*- coding: utf-8 -*-
from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

#####################################################################
# NOTE: Here LAM is the hard-coded value of lambda for LRLS
# NOTE: Feel free to play with lambda as well if you wish
#####################################################################
LAM = 1e-5


# For tpye contracts
Array = np.ndarray


# helper function
def l2(A: Array, B: Array) -> Array:
    """
    Input: A is a Nxd matrix
           B is a Mxd matirx
    Output: dist is a NxM matrix where dist[i,j] is the square norm between A[i,:] and B[j,:]
    i.e. dist[i,j] = ||A[i,:]-B[j,:]||^2
    """
    A_norm = (A**2).sum(axis=1).reshape(A.shape[0], 1)
    B_norm = (B**2).sum(axis=1).reshape(1, B.shape[0])
    dist = A_norm + B_norm - 2 * A.dot(B.transpose())
    return dist


# to implement
def LRLS(
    test_datum: Array,
    x_train: Array,
    y_train: Array,
    tau: float,
    lam: float = LAM,
) -> Array:
    """
    Input: test_datum is a dx1 test vector
           x_train is the N_train x d design matrix
           y_train is the N_train x 1 targets vector
           tau is the local reweighting parameter
           lam is the regularization parameter
    output is y_hat the prediction on test_datum
    """
    #####################################################################
    # TODO: Implement LRLS function in Q4(b).
    #####################################################################
    dim = test_datum.shape[0]
    dist = l2(test_datum.reshape(1, dim), x_train)

    # Numerator and Denominator
    num = np.exp(-1 * dist / (2 * tau ** 2))
    denom = 0
    for i in range(len(x_train)):
        denom += num[0][i]
    a = (num + 1e-6) / (denom + 1e-6)

    w = np.linalg.solve((np.matmul(np.matmul(x_train.transpose(),
                                             np.diag(a.flatten())), x_train) + lam * np.eye(dim, dim)),
                        np.matmul(np.matmul(x_train.transpose(), np.diag(a.flatten())), y_train))

    y_hat = np.dot(test_datum.transpose(), w)
    #####################################################################
    #                       END OF YOUR CODE                            #
    #####################################################################
    return y_hat


def run_validation(
    x: Array, y: Array, taus: Array, val_frac: float
) -> tuple[list[float], list[float]]:
    """
    Input: x is the N x d design matrix
           y is the 1-dimensional vector of size N
           taus is a vector of tau values to evaluate
           val_frac is the fraction of examples to use as validation data
    output is
           a vector of training losses, one for each tau value
           a vector of validation losses, one for each tau value
    """
    #####################################################################
    # TODO: Complete the rest of the code for Q4(c).
    #####################################################################
    train_losses = []
    validation_losses = []

    train_inputs, valid_inputs, train_targets, valid_targets = train_test_split(x, y, test_size=val_frac)

    for tau in taus:
        train_loss = 0
        valid_loss = 0

        # Training loss
        for j in range(len(train_inputs)):
            pred = LRLS(train_inputs[j], train_inputs, train_targets, tau)
            target = train_targets[j]
            train_loss += (pred - target) ** 2

        # Validation loss
        for j in range(len(valid_inputs)):
            pred = LRLS(valid_inputs[j], train_inputs, train_targets, tau)
            target = valid_targets[j]
            valid_loss += (pred - target) ** 2

        # From piazza and lecture
        train_losses.append(train_loss / (2 * len(train_inputs)))
        validation_losses.append(valid_loss / (2 * len(valid_inputs)))
    #####################################################################
    #                       END OF YOUR CODE                            #
    #####################################################################
    return train_losses, validation_losses


if __name__ == "__main__":
    # feel free to change this number depending on resource usage
    import os

    NUM_TAUS = os.environ.get("NUM_TAUS", 200)
    #####################################################################
    #                       DO NOT MODIFY CODE BELOW                   #
    #####################################################################
    from sklearn.datasets import fetch_california_housing

    np.random.seed(0)
    # load boston housing prices dataset
    housing = fetch_california_housing()
    n_samples = 500
    x = housing["data"][:n_samples]
    N = x.shape[0]
    # add constant one feature - no bias needed
    x = np.concatenate((np.ones((N, 1)), x), axis=1)
    d = x.shape[1]
    y = housing["target"][:N]
    taus = np.logspace(1, 3, NUM_TAUS)
    train_losses, test_losses = run_validation(x, y, taus, val_frac=0.3)
    plt.semilogx(taus, train_losses, label="Training Loss")
    plt.semilogx(taus, test_losses, label="Validation Loss")
    plt.legend(loc="upper right")
    plt.xlabel("Tau values (log scale)")
    plt.ylabel("Average squared error loss")
    plt.title("Training and Validation Loss w.r.t Tau")
    plt.savefig("q4.png")
