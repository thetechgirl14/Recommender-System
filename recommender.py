import filter_model
import process_ratings
import numpy as np
import pandas as pd

def recommend(book_name):

    pt = filter_model.final_rating()
    
    similarity_scores = filter_model.model()
    
    books = process_ratings.preprocess_book()
    
    if book_name in pt.index:
        
        book_index = pt.index.get_loc(book_name)

        similar_books = list(enumerate(similarity_scores[book_index]))

        similar_books = sorted(similar_books, key=lambda x: x[1], reverse=True)[1:5]

        data = []
        for i in similar_books:
            title = pt.index[i[0]]
            author = books[books['Book-Title'] == title]['Book-Author'].values[0]
            image_url = books[books['Book-Title'] == title]['Image-URL-M'].values[0]
            data.append([title, author, image_url])

        df = pd.DataFrame(data, columns=['Book-Title', 'Book-Author', 'Image-URL-M'])

        return df
    else:
        return None

if __name__ == "__main__":
    book_name = 'A Bend in the Road'
    df = recommend(book_name)
    print(df)