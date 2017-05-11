from DecisionTree import DecisionTree
from utils import *
class RandomForest(object):
    def __init__(self, num_trees, max_depth, min_size):
        self.tree_list = list()
        self.max_depth = max_depth
        self.min_size = min_size
        self.num_trees = num_trees



