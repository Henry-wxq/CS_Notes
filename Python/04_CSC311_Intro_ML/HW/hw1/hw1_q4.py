from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn import tree
import graphviz
from math import log


def load_data(real_news_path, fake_news_path):
    """
    This function loads the data, pre-processes it using a vectorizer, and splits the
    entire dataset randomly into 70% training, 15% validation, and 15% test examples.
    """
    with open(real_news_path, 'r') as real_news_file:
        r_data = real_news_file.readlines()
        r_labels = [1] * len(r_data)

    with open(fake_news_path, 'r') as fake_news_file:
        f_data = fake_news_file.readlines()
        f_labels = [0] * len(f_data)

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(r_data + f_data)
    t = r_labels + f_labels

    # Split into train (70%) + validation (15%) + test (15%)
    X_train, X_temp, y_train, y_temp = train_test_split(X, t, test_size=0.3, random_state=1)

    X_valid, X_test, y_valid, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=1)

    return X_train, X_valid, X_test, y_train, y_valid, y_test, vectorizer.get_feature_names_out()


def select_model(X_train, y_train, X_valid, y_valid):
    """
    This function trains the decision tree classifier using at least 5 different values
    of max_depth, as well as three different split criteria (information gain, log loss
    and Gini coefficient), evaluates the performance of each one on the validation set,
    and prints the resulting accuracies of each model.
    """
    # Get the 5 different max depths
    max_depths = [5 * n for n in range(1, 6)]

    entropy_scores = []
    gini_scores = []
    log_loss_scores = []

    for d in max_depths:
        entropy_tree = DecisionTreeClassifier(criterion="entropy", max_depth=d)
        gini_tree = DecisionTreeClassifier(criterion="gini", max_depth=d)
        log_loss_tree = DecisionTreeClassifier(criterion="log_loss", max_depth=d)

        entropy_tree.fit(X_train, y_train)
        gini_tree.fit(X_train, y_train)
        log_loss_tree.fit(X_train, y_train)

        entropy_score = entropy_tree.score(X_valid, y_valid)
        gini_score = gini_tree.score(X_valid, y_valid)
        log_loss_score = log_loss_tree.score(X_valid, y_valid)

        print(f"Depth {d}: ")
        print("Validation Accuracy using entropy:", entropy_score)
        print("Validation Accuracy using Gini:", gini_score)
        print("Validation Accuracy using log loss:", log_loss_score)

        entropy_scores.append(entropy_score)
        gini_scores.append(gini_score)
        log_loss_scores.append(log_loss_score)

    plt.plot(max_depths, entropy_scores, 'b', label='Information Gain')
    plt.plot(max_depths, gini_scores, 'g', label='Gini Coefficient')
    plt.plot(max_depths, log_loss_scores, 'r', label='Log Loss')

    plt.title('Validation Accuracy vs. max_depth')
    plt.xlabel('max_depth')
    plt.ylabel('Validation Accuracy')

    plt.legend()
    plt.show()


def visualize_tree(model, feature_names):
    """
    This function generates and returns an image representing a Sklearn decision tree.
    """
    # Export to .dot
    dot_data = tree.export_graphviz(model,
                                       feature_names=feature_names,
                                       max_depth=2,
                                       class_names=["Class 0", "Class 1"],
                                       filled=True, rounded=True)
    # Generate graph
    graph = graphviz.Source(dot_data)
    graph.format = 'png'
    graph.render(filename='tree_visualization', cleanup=True)

    print("Decision Tree visualization saved as 'tree_visualization.png'.")


def compute_information_gain(X_data, y_labels, feature_names, keyword):
    """
    This function computes the information gain of a split on the training data.
    """
    # Real and fake counter
    count_real = 0
    count_fake = 0

    for label in y_labels:
        if label == 1:
            count_real += 1
        else:
            count_fake += 1

    # Probabilities of class
    prob_real = count_real / len(y_labels)
    prob_fake = count_fake / len(y_labels)

    # Initial entropy
    initial_entropy = -(log(prob_real, 2) * prob_real) - (log(prob_fake, 2) * prob_fake)

    feature_idx = feature_names.tolist().index(keyword)

    # Counters for conditional distributions
    count_real_with_keyword = 0
    count_fake_with_keyword = 0
    count_real_without_keyword = 0
    count_fake_without_keyword = 0

    for i in range(len(y_labels)):
        if X_data[i, feature_idx] == 0:
            if y_labels[i] == 1:
                count_real_without_keyword += 1
            else:
                count_fake_without_keyword += 1
        else:
            if y_labels[i] == 1:
                count_real_with_keyword += 1
            else:
                count_fake_with_keyword += 1

    # Ratios of keyword
    prob_real_with_keyword = count_real_with_keyword / len(y_labels)
    prob_fake_with_keyword = count_fake_with_keyword / len(y_labels)
    prob_real_without_keyword = count_real_without_keyword / len(y_labels)
    prob_fake_without_keyword = count_fake_without_keyword / len(y_labels)

    # Probability of keyword
    prob_keyword_present = (count_real_with_keyword + count_fake_with_keyword) / len(y_labels)
    prob_keyword_absent = (count_real_without_keyword + count_fake_without_keyword) / len(y_labels)

    # Conditional probabilities of keyword
    cond_prob_real_w_keyword = prob_real_with_keyword / prob_keyword_present
    cond_prob_fake_w_keyword = prob_fake_with_keyword / prob_keyword_present
    cond_prob_real_wo_keyword = prob_real_without_keyword / prob_keyword_absent
    cond_prob_fake_wo_keyword = prob_fake_without_keyword / prob_keyword_absent

    cond_entropy = -(log(cond_prob_real_w_keyword, 2) * prob_real_with_keyword) \
                          - (log(cond_prob_fake_w_keyword, 2) * prob_fake_with_keyword) \
                          - (log(cond_prob_real_wo_keyword, 2) * prob_real_without_keyword) \
                          - (log(cond_prob_fake_wo_keyword, 2) * prob_fake_without_keyword)

    # Information gain
    info_gain = initial_entropy - cond_entropy
    print(f"Information Gain for feature '{keyword}': {info_gain}")


if __name__ == "__main__":
    # Q4a
    X_train, X_valid, X_test, y_train, y_valid, y_test, feature_names = load_data("./clean_real.txt",
                                                                                  "./clean_fake.txt")

    # Q4b
    select_model(X_train, y_train, X_valid, y_valid)

    # Q4c
    log_loss_tree = DecisionTreeClassifier(criterion="log_loss", max_depth=25)
    log_loss_tree.fit(X_train, y_train)
    visualize_tree(log_loss_tree, feature_names)

    # Q4d
    compute_information_gain(X_train, y_train, feature_names, "donald")
    compute_information_gain(X_train, y_train, feature_names, "trumps")
    compute_information_gain(X_train, y_train, feature_names, "the")
    compute_information_gain(X_train, y_train, feature_names, "hillary")
    compute_information_gain(X_train, y_train, feature_names, "coal")
