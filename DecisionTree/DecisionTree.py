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
        return 0

    def prune_tree(self, max_depth):
        current_tree = self.tree

    def predict(x):
    # function to make a prediction from said tree
        return 0

    def gini_index(self, groups, class_values): #cost function to split data
        gini = 0
        for class_value in class_values:
            for group in groups:
                size=len(group)
                if size == 0:
                    continue
                proportion = [row[-1] for row in group].count(class_value) / float(size)
                gini += proportion* (1.0 - proportion)
        return gini


Tree = DecisionTree()
print(Tree.gini_index([[[1, 1], [1, 0]], [[1, 1], [1, 0]]], [0, 1]))
print(Tree.gini_index([[[1, 0], [1, 0]], [[1, 1], [1, 1]]], [0, 1]))
