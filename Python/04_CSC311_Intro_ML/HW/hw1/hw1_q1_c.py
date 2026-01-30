import numpy as np
import matplotlib.pyplot as plt


def together():
    # Given dimensions
    dimensions = [2 ** i for i in range(11)]

    # Number of samples
    n_samples = 100

    # Mean and standard deviation lists
    l1_means = []
    l2_means = []
    l1_stds = []
    l2_stds = []


    # Function to calculate L1 and L2 distances
    def calculate_distances(samples):
        l1_distances = []
        l2_distances = []
        for i in range(len(samples)):
            for j in range(i + 1, len(samples)):
                l1_distances.append(np.sum(np.abs(samples[i] - samples[j])))
                l2_distances.append(np.sum((samples[i] - samples[j]) ** 2))
        return np.mean(l1_distances), np.std(l1_distances), np.mean(l2_distances), np.std(l2_distances)


    # Generate data and calculate distances for each dimension
    for d in dimensions:
        # Generate random samples in [0, 1]^d
        samples = np.random.rand(n_samples, d)

        # Calculate mean and std of distances
        l1_mean, l1_std, l2_mean, l2_std = calculate_distances(samples)

        # Append to the lists
        l1_means.append(l1_mean)
        l1_stds.append(l1_std)
        l2_means.append(l2_mean)
        l2_stds.append(l2_std)

    # Plotting
    plt.figure(figsize=(12, 8))

    # Mean Distance vs Dimension
    plt.subplot(2, 1, 1)
    plt.plot(dimensions, l1_means, 'bo-', label='L1 Mean')
    plt.plot(dimensions, l2_means, 'ro-', label='L2 Mean')
    plt.xlabel('Dimension')
    plt.ylabel('Distance')
    plt.title('l1 Mean and l2 Mean Distance vs Dimension')
    plt.legend()
    plt.grid(True)

    # Standard Deviation vs Dimension
    plt.subplot(2, 1, 2)
    plt.plot(dimensions, l1_stds, 'bo-', label='L1 Std')
    plt.plot(dimensions, l2_stds, 'ro-', label='L2 Std')
    plt.xlabel('Dimension')
    plt.ylabel('Standard Deviation')
    plt.title('l1 Mean and l2 Standard Deviation vs Dimension')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def separate():
    # Given dimensions
    dimensions = [2 ** i for i in range(11)]

    # Number of samples
    n_samples = 100

    # Mean and standard deviation lists
    l1_means = []
    l2_means = []
    l1_stds = []
    l2_stds = []

    # Function to calculate L1 and L2 distances
    def calculate_distances(samples):
        l1_distances = []
        l2_distances = []
        for i in range(len(samples)):
            for j in range(i + 1, len(samples)):
                l1_distances.append(np.sum(np.abs(samples[i] - samples[j])))
                l2_distances.append(np.sum((samples[i] - samples[j]) ** 2))
        return np.mean(l1_distances), np.std(l1_distances), np.mean(l2_distances), np.std(l2_distances)

    # Generate data and calculate distances for each dimension
    for d in dimensions:
        # Generate random samples in [0, 1]^d
        samples = np.random.rand(n_samples, d)

        # Calculate mean and std of distances
        l1_mean, l1_std, l2_mean, l2_std = calculate_distances(samples)

        # Append to the lists
        l1_means.append(l1_mean)
        l1_stds.append(l1_std)
        l2_means.append(l2_mean)
        l2_stds.append(l2_std)

    # Plotting separate figures

    # Plot L1 Mean vs Dimension
    plt.figure(figsize=(8, 6))
    plt.plot(dimensions, l1_means, 'bo-', label='L1 Mean')
    plt.xlabel('Dimension')
    plt.ylabel('Distance')
    plt.title('L1 Mean Distance vs Dimension')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot L2 Mean vs Dimension
    plt.figure(figsize=(8, 6))
    plt.plot(dimensions, l2_means, 'ro-', label='L2 Mean')
    plt.xlabel('Dimension')
    plt.ylabel('Distance')
    plt.title('L2 Mean Distance vs Dimension')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot L1 Std vs Dimension
    plt.figure(figsize=(8, 6))
    plt.plot(dimensions, l1_stds, 'bo-', label='L1 Std')
    plt.xlabel('Dimension')
    plt.ylabel('Standard Deviation')
    plt.title('L1 Standard Deviation vs Dimension')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot L2 Std vs Dimension
    plt.figure(figsize=(8, 6))
    plt.plot(dimensions, l2_stds, 'ro-', label='L2 Std')
    plt.xlabel('Dimension')
    plt.ylabel('Standard Deviation')
    plt.title('L2 Standard Deviation vs Dimension')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    separate()
