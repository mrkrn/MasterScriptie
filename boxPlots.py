# Import libraries
import matplotlib.pyplot as plt
import numpy as np


# rank1 = np.array([1, 4, 4, 2, 1, 5])
# rank2 = np.array([3, 2, 2, 5, 3, 1])
# rank3 = np.array([4, 3, 3, 3, 4, 2])
# rank4 = np.array([2, 5, 5, 1, 2, 4])
# rank5 = np.array([5, 1, 1, 4, 5, 3])

rank1 = np.array([6, 3, 4, 3, 5, 6])
rank2 = np.array([3, 3, 1, 3, 5, 2])
rank3 = np.array([1, 4, 2, 2, 2, 1])
rank4 = np.array([4, 1, 4, 5, 6, 3])
rank5 = np.array([5, 2, 1, 6, 6, 5])
rank6 = np.array([2, 4, 5, 6, 1, 4])

data = [rank1, rank2, rank3, rank4, rank5, rank6]

fig = plt.figure(figsize=(10, 7))


plt.boxplot(data)
plt.xticks([1, 2, 3, 4, 5, 6], ["Rank1", "Rank2", "Rank3", "Rank4", "Rank5", "Rank6"])
# show plot
plt.show()
