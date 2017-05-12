# Decision Tree

class DecisionTree(object):
    def __init__(self, max_depth, min_size):
        self.root = None # holds our tree
        self.max_depth = max_depth # max depth of trees
        self.min_size = min_size # min size of 

    def gini_index(self, groups, class_values):
        # Return a cost funtion between 0 <= x <= 1, where 0 means you have split
        # the data 50/50, and 1 is the best possible split (i.e., no split).  

        gini = 0.0
        for class_value in class_values:
            for group in groups:
                size = len(group)
                if size == 0:
                    continue
                proportion = [row[-1] for row in group].count(class_value) / float(size)
                gini += (proportion * (1.0 - proportion))
        return gini

    def test_split(self, index, value, dataset):
        # Generate two lists, one list where the value of the index we are looking
        # at is less than the passed in value, and the right list is greater than
        # passed in value

        left, right = list(), list()
        for row in dataset:
            if row[index] < value:
                left.append(row)
            else:
                right.append(row)
        return left, right

    def get_split(self, dataset):
        # Generate the best split, by calling test_split to repeatedly test out
        # various splits and choosing the one with the least gini_index cost.

        best_index, best_value, best_score, best_groups = 999,999,999,None
        class_values = list(set(row[-1] for row in dataset))
        for index in range(len(dataset[0]) -1):
            for row in dataset:
                groups = self.test_split(index, row[index], dataset)
                gini = self.gini_index(groups, class_values)
                if gini < best_score:
                    best_index, best_value, best_score, best_groups = index, \
                    row[index], gini, groups

        return {'index':best_index, 'value':best_value, 'groups':best_groups}

    def split(self, node, max_depth, min_size, depth):
        # Recursing splitting function to split our data.  We stop splitting when
        # we hit the maximum depth size, and/or the data does not split.
        # Otherwise, we call get_split function on the left and right side.  If
        # the groups on either side get too small, then we call the terminal node
        # to make it a leaf node.

        left, right = node['groups']
        del(node['groups'])
        # check for a no split
        if not left or not right:
            node['left'] = node['right'] = self.to_terminal(left + right)
            return
	# check for max depth
        if depth >= max_depth:
            node['left'], node['right'] = self.to_terminal(left), self.to_terminal(right)
            return
	# process left child
        if len(left) <= min_size:
            node['left'] = self.to_terminal(left)
        else:
            node['left'] = self.get_split(left)
            self.split(node['left'], max_depth, min_size, depth+1)
	# process right child
        if len(right) <= min_size:
            node['right'] = self.to_terminal(right)
        else:
            node['right'] = self.get_split(right)
            self.split(node['right'], max_depth, min_size, depth+1)

    def to_terminal(self, group):
        # Only to be used at terminal/leaf nodes of the tree, if we decide that we
        # will stop adding new splits and branches to the tree.  Sets all
        # class_values of that group to the same, whatever is max.

        outcomes = [row[-1] for row in group]
        return max(set(outcomes), key=outcomes.count)

    def fit(self, train):
        # train is the dataset
        # max_depth is how deep we want to go
        # min_size is how small the terminal node can be
        # function that recursively calls split to build a tree

        self.root = self.get_split(train)
        self.split(self.root, self.max_depth, self.min_size, 1)

    def print_tree(self, depth = 0):
        # Calls recursive function to print out how the tree looks like
        self.print_tree_func(self.root, depth)

    def print_tree_func(self, node, depth = 0):
        # Recursive function that prints out how tree looks like.  Prints out left
        # and right nodes, and if there are no more, prints out split values.
        if isinstance(node, dict):
            print('%s[X%d < %.3f]' % ((depth*' ', (node['index']+1), \
                                       node['value'])))
            self.print_tree_func(node['left'], depth+1)
            self.print_tree_func(node['right'], depth+1)
        else:
            print('%s[%s]' % ((depth*' ', node)))

    def predict(self, row, node = None):
        # function that predicts based off the node that is passed in, the default
        # of which is root node of Tree.  Recursive function that traverses the
        # tree until it hits terminal node, then returns the predicted value
        if node == None:
            node = self.root
        if row[node['index']] < node['value']:
            if isinstance(node['left'], dict):
                return self.predict(row, node['left'])
            else:
                return node['left']
        else:
            if isinstance(node['right'], dict):
                return self.predict(row, node['right'])
            else:
                return node['right']

