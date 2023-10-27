import preprocess_data as pre_data
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

def preprocess_book():
    
    books = pre_data.read_book_data()
    books.dropna(inplace=True)
    
    books['Year-Of-Publication'] = books['Year-Of-Publication'].astype(str)
    return books


def preprocess_users():
    
    users = pre_data.read_users_data()
    
    users.drop('Age', axis=1, inplace=True)
    return users


def merge():
    
    ratings = pre_data.read_ratings_data()
    books = preprocess_book()
    
    ratings_with_name = pd.merge(ratings, books, on='ISBN', how='inner')
    return ratings_with_name

def no_of_rating():
    
    ratings_with_name = merge()

    num_rating_df = ratings_with_name.groupby('Book-Title').size().reset_index(name='num_ratings')

    return num_rating_df



def avg_rating():
    
    ratings_with_name = merge()

    avg_rating_df = ratings_with_name.groupby('Book-Title')['Book-Rating'].mean().reset_index(name='avg_rating')

    avg_rating_df['avg_rating'] = avg_rating_df['avg_rating'].round(2)

    return avg_rating_df


def merge2():
    
    num_rating_df = no_of_rating()
    avg_rating_df = avg_rating()

    popular_df = pd.merge(num_rating_df, avg_rating_df, on='Book-Title', how='inner')

    return popular_df
