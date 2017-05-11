from DecisionTree import DecisionTree
from random import randrange


class RandomForest(object):
    def __init__(self, num_trees, max_depth, min_size):
        self.tree_list = list()
        self.max_depth = max_depth
        self.min_size = min_size
        self.num_trees = num_trees
    def split_data(self, dataset, num_trees):
        # function that splits the data randomly based on how many trees are
        # wanted.  returns a list that contains different lists of randomly
        # selected data.

        dataset_split = list()
        dataset_copy = list(dataset)
        split_size = int(len(dataset) / num_trees)
        for rand_data in range(num_trees):
            rand_data_list = list()
            while len(rand_data) < split_size:
                index = randrange(len(dataset_copy))
                rand_data_list.append(dataset_copy.pop(index))
            dataset_split.append(rand_data_list)
        return dataset_split

    def fit(self, train):
       # Takes in data as a list of lists, where each inner list is a subset of
       # data for each tree in the forest.   For each inner list, a tree is
       # created and fitted to that data.  Tree is saved the RandomForest's list
       # of trees.

        for data_set in range(len(train)):
            Tree = DecisionTree(self.max_depth, self.min_size)
            Tree.fit(data_set)
            self.tree_list.append(Tree)

    def predict(self, row):
        # For each tree in the Forest, call it's trained tree and see what it
        # predicts.  Typically, the vote that is returned the most is what is
        # selected, but that is up to the user.  Returns predictions in a list.
        predictions_list = list()
        for tree in range(len(self.tree_list)):
            prediction = tree.predict(row)
            predictions_list.append(prediction)
        return predictions_list



