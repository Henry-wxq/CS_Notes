from utils import Array, sigmoid
import numpy as np


def logistic_predict(weights: Array, data: Array) -> Array:
    """Compute the probabilities predicted by the logistic classifier.

    Note: N is the number of examples
          M is the number of features per example

    :param weights: A vector of weights with dimension (M + 1) x 1, where
    the last element corresponds to the bias (intercept).
    :param data: A matrix with dimension N x M, where each row corresponds to
    one data point.
    :return: A vector of probabilities with dimension N x 1, which is the output
    to the classifier.
    """
    #####################################################################
    # TODO:                                                             #
    # Given the weights and bias, compute the probabilities predicted   #
    # by the logistic classifier.                                       #
    #####################################################################
    w = weights[:-1]
    b = weights[-1]

    z = np.matmul(data, w) + b

    y = sigmoid(z)
    #####################################################################
    #                       END OF YOUR CODE                            #
    #####################################################################
    return y


def evaluate(targets: Array, y: Array) -> tuple[float, float]:
    """Compute evaluation metrics.

    Note: N is the number of examples
          M is the number of features per example

    :param targets: A vector of targets with dimension N x 1.
    :param y: A vector of probabilities with dimension N x 1.
    :return: A tuple (ce, frac_correct)
        WHERE
        ce: (float) Averaged cross entropy
        frac_correct: (float) Fraction of inputs classified correctly
    """
    #####################################################################
    # TODO:                                                             #
    # Given targets and probabilities predicted by the classifier,      #
    # return cross entropy and the fraction of inputs classified        #
    # correctly.                                                        #
    #####################################################################
    num_acc = 0
    num_ce = 0

    for i in range(len(targets)):
        y_i = y[i]
        t_i = targets[i]
        z_i = - np.log(1 / y_i - 1)

        ce_i = t_i * np.logaddexp(0, -z_i) + (1 - t_i) * np.logaddexp(0, z_i)
        num_ce += ce_i

        if t_i == (y_i >= 0.5):
            num_acc += 1

    ce = num_ce / len(targets)
    frac_correct = num_acc / len(targets)
    #####################################################################
    #                       END OF YOUR CODE                            #
    #####################################################################
    return ce, frac_correct


def logistic(
    weights: Array, data: Array, targets: Array, hyperparameters: dict
) -> tuple[float, Array, Array]:
    """Calculate the cost and its derivatives with respect to weights.
    Also return the predictions.

    Note: N is the number of examples
          M is the number of features per example

    :param weights: A vector of weights with dimension (M + 1) x 1, where
    the last element corresponds to the bias (intercept).
    :param data: A matrix with dimension N x M, where each row corresponds to
    one data point.
    :param targets: A vector of targets with dimension N x 1.
    :param hyperparameters: The hyperparameter dictionary.
    :returns: A tuple (f, df, y)
        WHERE
        f: The average of the loss over all data points.
           This is the objective that we want to minimize.
        df: (M + 1) x 1 vector of derivative of f w.r.t. weights.
        y: N x 1 vector of probabilities.
    """
    y = logistic_predict(weights, data)

    #####################################################################
    # TODO:                                                             #
    # Given weights and data, return the averaged loss over all data    #
    # points, gradient of parameters, and the probabilities given by    #
    # logistic regression.                                              #
    #####################################################################
    f = evaluate(targets, y)[0]
    df_lst = []

    # Weights gradient calculation
    for i in range(len(weights) - 1):
        w_df = 0
        for j in range(len(targets)):
            w_df += (y[j][0] - targets[j][0]) * data[j, i]
        w_df /= len(targets)
        df_lst.append([w_df])

    # Bias gradient calculation
    b_df = 0
    for j in range(len(targets)):
        b_df += (y[j][0] - targets[j][0])
    b_df /= len(targets)
    df_lst.append([b_df])

    df = np.array(df_lst)
    #####################################################################
    #                       END OF YOUR CODE                            #
    #####################################################################
    return f, df, y
