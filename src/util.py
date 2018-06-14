import csv
import os
import numpy as np

def parse_csv(filename):
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, filename)
    with open(path) as csv_file:
        return list(csv.DictReader(csv_file))

def get_book_ratings_train():
    return parse_csv('../data/book_ratings_test.csv')

def get_book_ratings_train():
    return parse_csv('../data/book_ratings_train.csv')

def get_implicit_ratings():
    return parse_csv('../data/implicit_ratings.csv')

def get_books():
    return parse_csv('../data/books.csv')

def get_users():
    return parse_csv('../data/users.csv')

# 兩個參數型別皆爲 numpy array
def MAE_error(guess, answer):
    return np.average(np.absolute(guess - answer))


# 兩個參數型別皆爲 numpy array
def MAPE_error(guess, answer):
    return np.average(np.absolute((guess - answer) / answer)) * 100
