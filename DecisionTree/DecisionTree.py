import os


# class TreeNode(object):
#     """A node for the decision tree"""
#     def __init__(self, isLeaf=False):
#         self.data = None
#         self.isLeaf = False


class DecisionTree(object):
    # needs entropy critierion
    def __init__(self):
        self.root = None

    def prune_tree(self, max_depth): # Future function to prune tree
        current_tree = self.tree

    def predict(self, node, row):
    # function to make a prediction from said tree
        if row[node['index']] < node['value']:
            if isinstance(node['left'], dict):
                return self.predict(node['left'], row)
            else:
                return node['left']

        else:
            if isinstance(node['right'], dict):
                return self.predict(node['right'], row)
            else:
                return node['right']

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

    def test_split(self, index, value, dataset):
        left, right = list(), list()
        for row in dataset:
            if row[index] < value:
                left.append(row)
            else:
                right.append(row)
        return left, right

    def get_split(self, dataset):
        class_values = list(set(row[-1] for row in dataset))
        b_index, b_value, b_score, b_groups = 999,999,999,None
        for index in range(len(dataset[0]) -1):
            for row in dataset:
                groups = self.test_split(index, row[index], dataset)
                gini = self.gini_index(groups, class_values)
                print('X%d < %.3f Gini=%.3f' % ((index+1), row[index], gini))
                if gini < b_score:
                    b_index, b_value, b_score, b_groups = index, row[index], gini, groups
        return {'index':b_index, 'value':b_value, 'groups':b_groups}

    def to_terminal(self,group):
        outcomes = [row[-1] for row in group]
        return max(set(outcomes), key=outcomes.count)

    def split(self, node, max_depth, min_size, depth):
        left, right = node['groups']
        del(node['groups'])
        # check of no splits, BASE case
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

    def build_tree(self, train, max_depth, min_size):
        root = self.get_split(train)
        self.split(root, max_depth, min_size, 1)
        return root

    def print_tree(self, node, depth=0):
        if isinstance(node, dict):
            print('%s[X%d < %.3f]' % ((depth*' ', (node['index']+1),
                  node['value'])))
            self.print_tree(node['left'], depth+1)
            self.print_tree(node['right'], depth+1)
        else:
            print('%s[%s]' % ((depth*' ', node)))


def main():
    # Functions to test Decision Tree as I build it
    os.system("clear")
    Tree = DecisionTree() # Build Tree Object

    # testing gini cost function
    print("Testing Gini_index(cost function)")
    input("Press Enter to continue...")
    print(Tree.gini_index([[[1, 1], [1, 0]], [[1, 1], [1, 0]]], [0, 1]))
    print(Tree.gini_index([[[1, 0], [1, 0]], [[1, 1], [1, 1]]], [0, 1]))

    # testing splitting data
    dataset = [[2.771244718,1.784783929,0],
                  [1.728571309,1.169761413,0],
                  [3.678319846,2.81281357,0],
                  [3.961043357,2.61995032,0],
                  [2.999208922,2.209014212,0],
                  [7.497545867,3.162953546,1],
                  [9.00220326,3.339047188,1],
                  [7.444542326,0.476683375,1],
                  [10.12493903,3.234550982,1],
                  [6.642287351,3.319983761,1]]

    print("Testing Splits")
    input("Press Enter to Continue")
    split = Tree.get_split(dataset)
    print('Split:[X%d < %.3f]' % ((split['index'] + 1), split['value']))


    print('Printing Trees')
    input('Press Enter to continue...')
    tree_nodes = Tree.build_tree(dataset, 3, 1)
    Tree.print_tree(tree_nodes)

    print('Testing with predictions')
    input('Press Enter to continue...')
    stump = {'index': 0, 'right':1, 'value':6.642287351, 'left':0} # random values
    for row in dataset:
        prediction = Tree.predict(stump, row)
        print('Expected = %d, Got = %d' % (row[-1], prediction))

if __name__ == '__main__':
    main()





