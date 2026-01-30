from utils import Array, load_train, load_valid, load_test
import matplotlib.pyplot as plt
import numpy as np


# helper function
def l2_distance(A: Array, B: Array) -> Array:
    """
    Input: A is a Nxd matrix
           B is a Mxd matirx
    Output: dist is a NxM matrix where dist[i,j] is the 2-norm between A[i,:] and B[j,:]
    i.e. dist[i,j] = ||A[i,:]-B[j,:]||_2
    """
    A_norm = (A**2).sum(axis=1).reshape(A.shape[0], 1)
    B_norm = (B**2).sum(axis=1).reshape(1, B.shape[0])
    dist = np.sqrt(A_norm + B_norm - 2 * A.dot(B.transpose()))
    return dist


def knn(k: int, train_data: Array, train_labels: Array, valid_data: Array) -> Array:
    """Uses the supplied training inputs and labels to make
    predictions for validation data using the K-nearest neighbours
    algorithm.

    Note: N_TRAIN is the number of training examples,
          N_VALID is the number of validation examples,
          M is the number of features per example.

    :param k: The number of neighbours to use for classification
    of a validation example.
    :param train_data: N_TRAIN x M array of training data.
    :param train_labels: N_TRAIN x 1 vector of training labels
    corresponding to the examples in train_data (must be binary).
    :param valid_data: N_VALID x M array of data to
    predict classes for validation data.
    :return: N_VALID x 1 vector of predicted labels for
    the validation data.
    """
    dist = l2_distance(valid_data, train_data)
    nearest = np.argsort(dist, axis=1)[:, :k]

    train_labels = train_labels.reshape(-1)
    valid_labels = train_labels[nearest]

    # Note this only works for binary labels:
    valid_labels = (np.mean(valid_labels, axis=1) >= 0.5).astype(int)
    valid_labels = valid_labels.reshape(-1, 1)

    return valid_labels


def run_knn(k_vals: list[int]) -> None:
    train_inputs, train_targets = load_train()
    valid_inputs, valid_targets = load_valid()
    test_inputs, test_targets = load_test()

    #####################################################################
    # TODO:                                                             #
    # Implement a function that runs kNN for different values of k,     #
    # plots the classification rate on the validation set, and etc.     #
    # as required for Q3.1 (a) and (b).                                 #
    #####################################################################
    # Lists to store accuracy values
    val_acc_lst = []
    test_acc_lst = []

    for k in k_vals:
        pred_val = knn(k, train_inputs, train_targets, valid_inputs)

        # Index
        num_sum_val = 0
        for i in range(len(pred_val)):
            if pred_val[i] == valid_targets[i]:
                num_sum_val += 1

        # Accuracy
        acc_val = num_sum_val / len(pred_val)
        val_acc_lst.append(acc_val)

        pred_val = knn(k, train_inputs, train_targets, test_inputs)

        num_sum_test = 0
        for i in range(len(pred_val)):
            if pred_val[i] == test_targets[i]:
                num_sum_test += 1

        acc_test = num_sum_test / len(pred_val)
        test_acc_lst.append(acc_test)

    # Plot the figure
    plt.plot(k_vals, val_acc_lst)
    plt.title("The classification accuracy as a function of k")
    plt.xlabel('k')
    plt.ylabel('validation accuracy')
    #####################################################################
    #                       END OF YOUR CODE                            #
    #####################################################################
    # This function needs to save a plot (with the appropriate Information)
    # named "knn.png" to be used for automated grading. Do NOT change it!
    plt.savefig("knn.png")


if __name__ == "__main__":
    #####################################################################
    #                       DO NOT MODIFY CODE BELOW                   #
    #####################################################################
    run_knn([1, 3, 5, 7, 9])
