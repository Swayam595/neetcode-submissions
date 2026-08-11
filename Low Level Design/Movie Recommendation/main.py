from user import User
from movie import Movie
from rating_register import RatingRegister
from movie_recommendation import MovieRecommendation
from movie_rating import MovieRating

user1 = User('User 1')
user2 = User('User 2')
user3 = User('User 3')
user4 = User('User 4')

movie1 = Movie('Batman Begins')
movie2 = Movie('Liar Liar')
movie3 = Movie('The Godfather')

ratings = RatingRegister()

ratings.add_rating(user1, movie1, MovieRating.FIVE)
ratings.add_rating(user1, movie2, MovieRating.TWO)
ratings.add_rating(user2, movie2, MovieRating.TWO)
ratings.add_rating(user2, movie3, MovieRating.FOUR)

recommender = MovieRecommendation(ratings)

print(recommender.recommend_movie(user1)) # The Godfather
print(recommender.recommend_movie(user2)) # Batman Begins
print(recommender.recommend_movie(user3)) # Batman Begins
