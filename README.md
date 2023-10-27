# Recommender System

This is a simple recommendation system that suggests books to users based on their preferences and the preferences of similar users. It uses collaborative filtering and cosine similarity to generate book recommendations.

## Project Structure

The project is divided into several modules, each handling a specific task:

1. `preprocess_data.py`: Contains functions for reading and checking null values in the dataset.

2. `process_ratings.py`: Includes functions for preprocessing the books and users data and merging it with the ratings data.

3. `filter_model.py`: Implements functions to filter and process the data for the recommendation model.

4. `recommender.py`: This file contains the recommendation algorithm and the main function to recommend books to users.

## Usage

1. Ensure you have the necessary datasets in the same directory as the python files.

2. Run the files in the following order:

   - `preprocess_data.py`
   - `process_ratings.py`
   - `filter_model.py`
   - `recommender.py`

3. The `recommender.py` file will recommend books based on the user's preferences and the existing data.

## Dependencies

Ensure you have the necessary Python packages installed. You can install them using the following command:

```
pip install -r requirements.txt
```


## Additional Notes

- Change the name of the book you're looking to get recommendations for in the `recommender.py` file.
- The dataset used in this project is for educational purposes only. Feel free to modify and extend the code for your specific needs.

For more information, please refer to the individual Python files.


