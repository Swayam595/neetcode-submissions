from rating_register import RatingRegister
from movie import Movie
from user import User

class MovieRecommendation:
    def __init__(self, ratings: RatingRegister):
        self.__movie_ratings = ratings

    def recommend_movie(self, user: User) -> str | None:
        if len(self.__movie_ratings.get_user_movies(user)) == 0:
            return self.__recommend_movie_new_user()
        else:
            return self.__recommend_movie_existing_user(user)

    def __recommend_movie_new_user(self) -> str | None:
        best_movie = None
        best_rating = 0

        for movie in self.__movie_ratings.get_movies():
            rating = self.__movie_ratings.get_average_rating(movie)
            if rating > best_rating:
                best_rating = rating
                best_movie = movie

        return best_movie.get_title() if best_movie else None

    def __recommend_movie_existing_user(self, user: User) -> str | None:
        best_movie = None
        similarity_score = float('inf')

        for reviewer in self.__movie_ratings.get_users():
            if reviewer.get_id() == user.get_id():
                continue

            score = self.__get_similarity_score(user, reviewer)
            if score < similarity_score:
                similarity_score = score
                recommended_movie = self.__recommend_unwatched_movies(user, reviewer)
                best_movie = recommended_movie if recommended_movie else best_movie

        return best_movie.get_title() if best_movie else None

    def __get_similarity_score(self, user1: User, user2: User) -> float:
        user1_id = user1.get_id()
        user2_id = user2.get_id()

        user2_movies = self.__movie_ratings.get_user_movies(user2)
        score = float('inf')

        for movie in user2_movies:
            curr_movie_ratings = self.__movie_ratings.get_movie_ratings(movie)
            if user1_id in curr_movie_ratings:
                score = 0 if score == float('inf') else score
                score += abs(curr_movie_ratings[user1_id].value - curr_movie_ratings[user2_id].value)

        return score

    def __recommend_unwatched_movies(self, user: User, reviewer: User) -> Movie:
        user_id = user.get_id()
        reviewer_id = reviewer.get_id()

        best_movie = None
        best_rating = 0

        reviewer_movies = self.__movie_ratings.get_user_movies(reviewer)
        for movie in reviewer_movies:
            curr_movie_ratings = self.__movie_ratings.get_movie_ratings(movie)
            if user_id not in curr_movie_ratings and curr_movie_ratings[reviewer_id].value > best_rating:
                best_rating = curr_movie_ratings[reviewer_id].value
                best_movie = movie

        return best_movie