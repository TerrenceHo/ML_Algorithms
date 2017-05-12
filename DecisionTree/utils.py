# various utility functions that can be used for many ml problems

from random import seed
from random import randrange
from csv import reader

def load_csv(filename):
    # returns lines of dataset as a list
    file = open(filename, 'r')
    lines = reader(file)
    dataset = list(lines)
    return dataset

def str_column_to_float(dataset, column):
    # transforms our strings into floats
    for row in dataset:
        row[column] = float(row[column].strip())

def cross_validation_split(dataset, n_folds):
    # Splits data into n number of folds for training
    dataset_split = list()
    dataset_copy = list(dataset)
    fold_size = int(len(dataset) / n_folds)
    for i in range(n_folds):
        fold = list()
        while len(fold) < fold_size:
            index = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))

        dataset_split.append(fold)
    return dataset_split

def accuracy_metric(actual, predicted):
    # Calculates how correct our predictions were
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0



