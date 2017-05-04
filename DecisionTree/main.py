from random import seed
from random import randrange
from csv import reader
import os


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







