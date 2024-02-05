import pandas as pd
from topn.model.recommender import RecommenderSystem

sample_data = pd.read_csv("tests/resources/processed_ratings.csv")


rec_sys = RecommenderSystem(sample_data)
print(rec_sys.movie_similarity_matrix)
print(50 * "-")
print(rec_sys.user_movie_matrix)
print(50 * "-")
recommendations = rec_sys.get_top_n_recommendations(3, n=5)
print(recommendations)
