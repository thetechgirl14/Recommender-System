import process_ratings
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

import warnings
warnings.filterwarnings('ignore')



def filter():
    
    popular_df = process_ratings.merge2()
    books = process_ratings.preprocess_book()

    popular_df = popular_df[popular_df['num_ratings'] >= 250]
    popular_df = popular_df.sort_values('avg_rating', ascending=False)

    popular_df = pd.merge(popular_df, books, on='Book-Title', how='inner')
    popular_df = popular_df.drop_duplicates('Book-Title')
    popular_df = popular_df[['Book-Title', 'Book-Author', 'Image-URL-M', 'num_ratings', 'avg_rating']]

    return popular_df

def filter2():
    
    ratings_with_name = process_ratings.merge()

    user_rating_counts = ratings_with_name.groupby('User-ID').size()

    users_a = user_rating_counts[user_rating_counts > 200].index

    filtered_rating = ratings_with_name[ratings_with_name['User-ID'].isin(users_a)]

    return filtered_rating


def final_rating():
    
    filtered_rating = filter2()

    book_rating_counts = filtered_rating.groupby('Book-Title').size()

    famous_books = book_rating_counts[book_rating_counts >= 50].index

    final_ratings = filtered_rating[filtered_rating['Book-Title'].isin(famous_books)]

    pt = final_ratings.pivot_table(index='Book-Title', columns='User-ID', values='Book-Rating')

    pt.fillna(0, inplace=True)

    return pt


def model():

    pt = final_rating()

    similarity_scores = cosine_similarity(pt)

    return similarity_scores