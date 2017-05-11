from DecisionTree import DecisionTree # import class and all helper functions
from utils import *
import os




def test():
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

def main():
    os.system('clear')
    print("Starting Decision Tree Algorithm")
    # parameters for the DecisionTree
    n_folds = 5
    max_depth = 5
    min_size = 10
    Tree = DecisionTree(max_depth, min_size)

    seed(1) # initialize Python's psuedorandom state
    dataset = load_csv('data_banknote_authentication.csv')
    # convert strings to floats
    for i in range(len(dataset[0])):
        str_column_to_float(dataset, i)

    print("Data Loaded")
    print("""Beginning Evaluating Cross Validation Splits, with %d folds, a max depth of %d, and a minimum size of %d""" % (n_folds, max_depth, min_size))
    folds = cross_validation_split(dataset, n_folds)
    scores = list()
    i = 0 # keep track of which fold during execution
    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])
        test_set = list()
        for row in fold:
            row_copy = list(row)
            test_set.append(row_copy)
            row_copy[-1] = None
        Tree.fit(train_set)
        predictions = list()
        for row in test_set:
            prediction = Tree.predict(row)
            predictions.append(prediction)
        actual = [row[-1] for row in fold]
        accuracy = accuracy_metric(actual, predictions)
        scores.append(accuracy)

        print("Evaluating Split: %d" % i)
        i += 1

    print('Scores: %s' % scores)
    print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))

if __name__ == '__main__':
    # test()
    main()






