class TreeNode(object):
    """A node for the decision tree"""
    def __init__(self, isLeaf=False):
        self.data = None
        self.isLeaf = False


class DecisionTree(object):
    # needs entropy critierion
    def __init__(self):
        self.root = None


    def fit(self, X, y):
    # function to make decision tree

    def prune_tree(self, max_depth):
        current_tree = self.tree

    def predict(x):
    # function to make a prediction from said tree
