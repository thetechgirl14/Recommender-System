import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

def read_book_data():
    books = pd.read_csv('Books.csv')
    return books


def read_users_data():
    users = pd.read_csv('Users.csv')
    return users


def read_ratings_data():
    ratings = pd.read_csv('Ratings.csv')
    return ratings


def check_null_values_books():
    
    books = read_book_data()
    
    null_values_books = books.isnull().sum()
    return null_values_books


def check_null_values_users():
    
    users = read_users_data()
    
    null_values_users = users.isnull().sum()
    return null_values_users


def check_null_values_ratings():
    
    ratings = read_ratings_data()
    
    null_values_ratings = ratings.isnull().sum()
    return null_values_ratings
