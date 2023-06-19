# Import libraries
import matplotlib.pyplot as plt
import numpy as np

# , 5
# , 4
# , 3
# , 1
# , 2

# , 6
# , 5
# , 4
# , 3
# , 1
# , 2

# , 6
# , 5
# , 3
# , 1
# , 4
# , 2

# , 5
# , 2
# , 1
# , 4
# , 3

# , 5
# , 3
# , 2
# , 1
# , 4

# , 4
# , 1
# , 3
# , 2
# , 5
# ------------------------------------------X--X
rank1_1 = np.array([1, 4, 4, 2, 1, 5, 1, 5, 1, 1])
rank2_1 = np.array([3, 2, 2, 5, 3, 1, 2, 3, 2, 2])
rank3_1 = np.array([4, 3, 3, 3, 4, 2, 4, 2, 3, 3])
rank4_1 = np.array([2, 5, 5, 1, 2, 4, 5, 4, 5, 5])
rank5_1 = np.array([5, 1, 1, 4, 5, 3, 3, 1, 4, 4])

rank1_2 = np.array([6, 3, 4, 3, 5, 6, 4, 6, 6, 2])
rank2_2 = np.array([3, 3, 1, 3, 5, 2, 2, 4, 5, 6])
rank3_2 = np.array([1, 4, 2, 2, 2, 1, 1, 3, 4, 5])
rank4_2 = np.array([4, 1, 4, 5, 6, 3, 4, 1, 2, 3])
rank5_2 = np.array([5, 2, 1, 6, 6, 5, 6, 5, 3, 1])
rank6_2 = np.array([2, 4, 5, 6, 1, 4, 3, 2, 1, 4])

rank1_3 = np.array([6, 3, 6, 5, 3, 1, 3, 6, 6, 3])
rank2_3 = np.array([3, 4, 1, 5, 6, 2, 6, 5, 2, 6])
rank3_3 = np.array([3, 5, 1, 4, 2, 4, 5, 4, 5, 5])
rank4_3 = np.array([5, 1, 3, 4, 4, 1, 1, 3, 4, 4])
rank5_3 = np.array([5, 2, 2, 6, 6, 2, 4, 2, 1, 1])
rank6_3 = np.array([6, 5, 2, 3, 1, 4, 2, 1, 3, 2])

rank1_4 = np.array([5, 3, 4, 3, 4, 1, 4, 5, 5, 3])
rank2_4 = np.array([4, 1, 1, 1, 2, 1, 2, 2, 2, 4])
rank3_4 = np.array([2, 1, 2, 2, 2, 5, 1, 3, 1, 2])
rank4_4 = np.array([2, 3, 4, 5, 5, 3, 3, 1, 3, 5])
rank5_4 = np.array([4, 4, 3, 5, 5, 3, 5, 4, 4, 1])

rank1_4cont = np.array([1, 5, 5, 3, 1, 4, 5, 5, 4])
rank2_4cont = np.array([3, 5, 5, 5, 3, 2, 2, 4, 3])
rank3_4cont = np.array([4, 2, 4, 1, 4, 1, 3, 2, 5])
rank4_4cont = np.array([3, 2, 2, 1, 3, 3, 1, 1, 2])
rank5_4cont = np.array([2, 4, 1, 4, 2, 5, 4, 3, 1])

rank1_5 = np.array([1, 4, 5, 4, 5, 4, 5, 5, 4, 4])
rank2_5 = np.array([1, 3, 2, 2, 3, 2, 4, 2, 3, 5])
rank3_5 = np.array([5, 2, 4, 3, 1, 5, 1, 4, 5, 3])
rank4_5 = np.array([2, 2, 1, 1, 1, 4, 2, 1, 1, 2])
rank5_5 = np.array([3, 5, 3, 5, 4, 3, 3, 3, 2, 1])

data_1 = [rank1_1, rank2_1, rank3_1, rank4_1, rank5_1]
data_2 = [rank1_2, rank2_2, rank3_2, rank4_2, rank5_2, rank6_2]
data_3 = [rank1_3, rank2_3, rank3_3, rank4_3, rank5_3, rank6_3]
data_4 = [rank1_4, rank2_4, rank3_4, rank4_4, rank5_4]
data_4cont = [rank1_4cont, rank2_4cont, rank3_4cont, rank4_4cont, rank5_4cont]
data_5 = [rank1_5, rank2_5, rank3_5, rank4_5, rank5_5]

data = [data_1, data_2, data_3, data_4, data_4cont, data_5]

for index, i in enumerate(data):
    figure = plt.figure(figsize=(10, 7))

    plt.title(f"Architecture {index+1}", fontsize=20)
    plt.ylabel("Ranked at index", fontsize=18)
    plt.xlabel("Architecture partitioning", fontsize=18)
    plt.boxplot(i, medianprops=dict(color="red", linewidth=2.5))
    plt.xticks(
        range(1, len(i) + 1),
        ["Partition {}".format(x) for x in range(1, len(i) + 1)],
        fontsize=18,
    )
    plt.yticks(fontsize=18)
    plt.savefig(f"OutcomeArch{index+1}", bbox_inches="tight")
    plt.close(figure)
    # plt.show()
    # exit()

figure, axis = plt.subplots(2, int(len(data) / 2))
# plt.figure(figsize=(10, 7))
for i in range(0, len(data)):
    x = int(i / 3)
    y = int(i % 3)
    axis[x, y].boxplot(data[i], medianprops=dict(color="red", linewidth=2.5))
    axis[x, y].set_xticks(
        list(range(1, len(data[i]) + 1)),
        ["Partition {}".format(x) for x in range(1, len(data[i]) + 1)],
    )
    axis[x, y].set_title("Architecture {}".format(str(i + 1)))
    axis[x, y].set_ylabel("Rankad at index")
    axis[x, y].set_xlabel("Architecture design")
    axis[x, y].set_yticks(axis[x, y].get_yticks()[::1])
    axis[x, y].set_ybound(0.5, len(data[i]) + 0.5)


# plt.boxplot(data_1)
# plt.show()
# plt.boxplot(data_2)
plt.show()
