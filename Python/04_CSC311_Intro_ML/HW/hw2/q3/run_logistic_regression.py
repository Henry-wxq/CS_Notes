from check_grad import check_grad
from utils import load_train, load_train_small, load_valid, load_test
from logistic import logistic, logistic_predict, evaluate

import matplotlib.pyplot as plt
import numpy as np


def run_logistic_regression():
    train_inputs_1, train_targets_1 = load_train()
    train_inputs_2, train_targets_2 = load_train_small()
    valid_inputs, valid_targets = load_valid()

    N_1, M_1 = train_inputs_1.shape
    N_2, M_2 = train_inputs_2.shape
    #####################################################################
    # TODO:                                                             #
    # Set the hyperparameters for the learning rate, the number         #
    # of iterations, and the way in which you initialize the weights.   #
    #####################################################################
    hyperparameters_1 = {
        "learning_rate": 0.08,
        "weight_regularization": 0.0,
        "num_iterations": 500,
    }
    weights_1 = np.zeros((M_1 + 1, 1))

    hyperparameters_2 = {
        "learning_rate": 0.08,
        "weight_regularization": 0.0,
        "num_iterations": 500,
    }
    weights_2 = np.zeros((M_2 + 1, 1))
    #####################################################################
    #                       END OF YOUR CODE                            #
    #####################################################################

    # Verify that your logistic function produces the right gradient.
    # diff should be very close to 0.
    run_check_grad(hyperparameters_1)
    run_check_grad(hyperparameters_2)

    # Begin learning with gradient descent
    #####################################################################
    # TODO:                                                             #
    # Modify this section to perform gradient descent, create plots,    #
    # and compute test error.                                           #
    #####################################################################
    test_inputs, test_targets = load_test()

    train_loss = []
    val_loss = []
    for i in range(hyperparameters_1["num_iterations"]):
        tr_func, tr_df, tr_y = logistic(weights_1, train_inputs_1, train_targets_1, hyperparameters_1)
        v_func, v_df, v_y = logistic(weights_1, valid_inputs, valid_targets, hyperparameters_1)

        train_loss.append(tr_func)
        val_loss.append(v_func)

        weights_1 = weights_1 - hyperparameters_1["learning_rate"] * tr_df

        if i == hyperparameters_1["num_iterations"] - 1:
            te_f, te_df, te_y = logistic(weights_1, test_inputs, test_targets, hyperparameters_1)

            tr_ce, tr_accuracy = evaluate(train_targets_1, tr_y)
            v_ce, v_accuracy = evaluate(valid_targets, v_y)
            te_ce, te_accuracy = evaluate(test_targets, te_y)

            print(f"Training Set: Cross Entropy = {tr_ce}, Classification Accuracy = {tr_accuracy}")
            print(f"Validation Set: Cross Entropy = {v_ce}, Classification Accuracy = {v_accuracy}")
            print(f"Test set: Cross Entropy = {te_ce}, Classification Accuracy = {te_accuracy}")

    x = list(range(0, hyperparameters_1["num_iterations"]))
    plt.title("Cross Entropy Changes in mnist_train")
    plt.plot(x, train_loss, label="Training Set")
    plt.plot(x, val_loss, label="Validation Set")
    plt.xlabel("Iteration Number")
    plt.ylabel("Cross Entropy")
    plt.legend()
    plt.show()

    test_inputs, test_targets = load_test()

    train_loss = []
    val_loss = []
    for i in range(hyperparameters_2["num_iterations"]):
        tr_func, tr_df, tr_y = logistic(weights_2, train_inputs_2, train_targets_2, hyperparameters_2)
        v_func, v_df, v_y = logistic(weights_2, valid_inputs, valid_targets, hyperparameters_2)

        train_loss.append(tr_func)
        val_loss.append(v_func)

        weights_2 = weights_2 - hyperparameters_2["learning_rate"] * tr_df

        if i == hyperparameters_2["num_iterations"] - 1:
            te_f, te_df, te_y = logistic(weights_2, test_inputs, test_targets, hyperparameters_2)

            tr_ce, tr_accuracy = evaluate(train_targets_2, tr_y)
            v_ce, v_accuracy = evaluate(valid_targets, v_y)
            te_ce, te_accuracy = evaluate(test_targets, te_y)

            print(f"Training Set: Cross Entropy = {tr_ce}, Classification Accuracy = {tr_accuracy}")
            print(f"Validation Set: Cross Entropy = {v_ce}, Classification Accuracy = {v_accuracy}")
            print(f"Test set: Cross Entropy = {te_ce}, Classification Accuracy = {te_accuracy}")

    x = list(range(0, hyperparameters_2["num_iterations"]))
    plt.title("Cross Entropy Changes in mnist_train_small")
    plt.plot(x, train_loss, label="Training Set")
    plt.plot(x, val_loss, label="Validation Set")
    plt.xlabel("Iteration Number")
    plt.ylabel("Cross Entropy")
    plt.legend()
    plt.show()
    # #####################################################################
    #                       END OF YOUR CODE                            #
    #####################################################################


def run_check_grad(hyperparameters):
    """Performs gradient check on logistic function.
    :return: None
    """
    # This creates small random data with 20 examples and
    # 10 dimensions and checks the gradient on that data.
    num_examples = 20
    num_dimensions = 10

    weights = np.random.randn(num_dimensions + 1, 1)
    data = np.random.randn(num_examples, num_dimensions)
    targets = np.random.rand(num_examples, 1)

    diff = check_grad(logistic, weights, 0.001, data, targets, hyperparameters)

    print("diff =", diff)


if __name__ == "__main__":
    run_logistic_regression()
