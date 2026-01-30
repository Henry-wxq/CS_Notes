"""
Question 4 Skeleton Code

Here you should implement and evaluate the Conditional Gaussian classifier.
NOTE: Do not modify or add any more import statements.
"""

import data
import numpy as np
import scipy.special  # might be useful!

# Import pyplot - plt.imshow is useful!
import matplotlib.pyplot as plt


def compute_mean_mles(train_data, train_labels):
    """
    Compute the mean estimate for each digit class

    Should return a numpy array of size (10,64)
    The ith row will correspond to the mean estimate for digit class i
    """
    means = np.zeros((10, 64))
    # Compute means
    for i in range(0, 10):
        digits = data.get_digits_by_label(train_data, train_labels, i)
        means[i] = np.mean(digits, axis=0)

    return means


def compute_sigma_mles(train_data, train_labels):
    """
    Compute the covariance estimate for each digit class

    Should return a three dimensional numpy array of shape (10, 64, 64)
    consisting of a covariance matrix for each digit class
    """
    covariances = np.zeros((10, 64, 64))

    means = compute_mean_mles(train_data, train_labels)

    for i in range(10):
        digits = data.get_digits_by_label(train_data, train_labels, i)

        centered_data = digits - means[i]

        covariances[i] = (centered_data.T @ centered_data) / digits.shape[0] + 0.01 * np.eye(64)

    return covariances


def generative_likelihood(digits, means, covariances):
    """
    Compute the generative log-likelihood:
        log p(x|y,mu,Sigma)

    Should return an n x 10 numpy array
    """
    n, d = digits.shape
    log_likelihood = np.zeros((n, 10))

    for i in range(10):
        mean = means[i]
        covariance = covariances[i]
        inv_covariance = np.linalg.inv(covariance)
        det_covariance = np.linalg.det(covariance)

        norm_factor = -0.5 * (d * np.log(2 * np.pi) + np.log(det_covariance))

        for j in range(n):
            diff = digits[j] - mean
            exponent = -0.5 * np.dot(diff.T, np.dot(inv_covariance, diff))
            log_likelihood[j, i] = norm_factor + exponent

    return log_likelihood


def conditional_likelihood(digits, means, covariances):
    """
    Compute the conditional likelihood:

        log p(y|x, mu, Sigma)

    This should be a numpy array of shape (n, 10)
    Where n is the number of datapoints and 10 corresponds to each digit class
    """
    log_p_x_y = generative_likelihood(digits, means, covariances) + np.log(0.1)

    log_p_x = np.logaddexp.reduce(log_p_x_y, axis=1).reshape(-1, 1)

    log_p_y_x = log_p_x_y - log_p_x

    return log_p_y_x


def avg_conditional_likelihood(digits, labels, means, covariances):
    """
    Compute the average conditional likelihood over the true class labels

        AVG( log p(y_i|x_i, mu, Sigma) )

    i.e. the average log likelihood that the model assigns to the correct class label
    """
    cond_likelihood = conditional_likelihood(digits, means, covariances)

    # Compute as described above and return
    n = digits.shape[0]
    correct = 0
    for i in range(n):
        correct_label = labels[i]
        correct += cond_likelihood[i][int(correct_label)]

    num = correct / n

    return num


def classify_data(digits, means, covariances):
    """
    Classify new points by taking the most likely posterior class
    """
    cond_likelihood = conditional_likelihood(digits, means, covariances)
    # Compute and return the most likely class

    return np.argmax(cond_likelihood, axis=1)


def main():
    train_data, train_labels, test_data, test_labels = data.load_all_data("data")

    # Fit the model
    means = compute_mean_mles(train_data, train_labels)
    covariances = compute_sigma_mles(train_data, train_labels)

    # Evaluation: Parts (a) - (c)
    # print train, test log-likelihoods and accuracies
    train_avg = avg_conditional_likelihood(train_data, train_labels, means, covariances)
    test_avg = avg_conditional_likelihood(test_data, test_labels, means, covariances)
    print(f"The average conditional log-likelihood for the train dataset: {train_avg:.3}.")
    print(f"The average conditional log-likelihood for the test dataset: {test_avg:.3}.")

    train_acc = np.mean(classify_data(train_data, means, covariances) == train_labels)
    test_acc = np.mean(classify_data(test_data, means, covariances) == test_labels)
    print(f"The accuracy for the train dataset: {train_acc:.3}.")
    print(f"The accuracy for the test dataset: {test_acc:.3}.")

    diag_cov_matrix = []
    for i in range(10):
        cov = covariances[i]
        diag_cov = np.diag(np.diag(cov))
        diag_cov_matrix.append(diag_cov)
    diag_covs = np.array(diag_cov_matrix)

    train_avg = avg_conditional_likelihood(train_data, train_labels, means, diag_covs)
    test_avg = avg_conditional_likelihood(test_data, test_labels, means, diag_covs)
    print(
        f"The average conditional log-likelihood for the training dataset by assuming Diagonal-Covariance Matrix: {train_avg:.3}.")
    print(
        f"The average conditional log-likelihood for the test datasetby assuming Diagonal-Covariance Matrix: {test_avg:.3}.")

    train_acc = np.mean(classify_data(train_data, means, diag_covs) == train_labels)
    test_acc = np.mean(classify_data(test_data, means, diag_covs) == test_labels)
    print(f"The accuracy for the training dataset by assuming Diagonal-Covariance Matrix: {train_acc:.3f}.")
    print(f"The accuracy for the test dataset by assuming Diagonal-Covariance Matrix: {test_acc:.3f}.")


if __name__ == "__main__":
    main()
